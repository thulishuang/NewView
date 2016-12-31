var client_id = 0;
var prev_content = "";

var canvas = document.createElement('canvas');
    canvas.height = 630;
    canvas.width = 1500;
document.getElementsByTagName('article')[0].appendChild(canvas);

var ctx = canvas.getContext("2d");
    ctx.fillStyle = "solid";
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 3;
    ctx.lineCap = "round";

socket = io.connect('http://138.68.25.237:4000');

socket.on('draw', function(data) {
      return draw(data.x, data.y, data.type);
    });

socket.on('clear', function(data) {
      return clear();
    });

socket.on('assign_id', function(data){
    if (client_id === 0)
        client_id = data;
});

socket.on('server_editor', function(data) {
    if (data.id !== client_id){
        $('#editor').val(data.content);
        prev_content = data.content;
        console.log("new content: " + data.content);
    }
});

socket.on('disconnect', function(){
        console.log('disconnect');
        socket.disconnect();
        $("#editor").val("");
        prev_content = "";
    });

var clear = function(data){
      ctx.clearRect(0,0,10800,19200);
    }

var draw = function(x, y, type) {
      if (type === "dragstart") {
        ctx.beginPath();
        return ctx.moveTo(x, y);
      } else if (type === "drag") {
        ctx.lineTo(x, y);
        return ctx.stroke();
      } else {
        return ctx.closePath();
      }
    };


$('canvas').live('drag dragstart dragend', function(e) {
    var offset, type, x, y;
    type = e.handleObj.type;
    offset = $(this).offset();
    e.offsetX = e.layerX - offset.left;
    e.offsetY = e.layerY - offset.top;
    x = e.offsetX;
    y = e.offsetY;
    draw(x, y, type);
    socket.emit('drawClick', {
      x: x,
      y: y,
      type: type
    });
  });

$("button").live('click',function(e){
      ctx.clearRect(0,0,10800,19200);
      socket.emit('clear',{
      })
  });

function emitClientEditor() {
    var content = $("#editor").val();
    if (content !== prev_content){
        socket.emit('client_editor', {
            'id': client_id,
            'content': content
        });
    }
}
document.getElementById("editor").addEventListener('input', emitClientEditor);

function limitArea() {
        var content = $('#editor').val();
        var limit = 15;
        var newlineCount = 0;
        for (var i = 0; i < content.length; i++) {
            if (content.charAt(i) == '\n') {
                newlineCount += 1;
                if (newlineCount == limit) {
                    content = content.substring(0, i);
                    break;
                }
            }
        }
        $('#editor').val(content);
    }
document.getElementById('editor').addEventListener('input', limitArea);
