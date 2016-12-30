var prev_content = "";

canvas = document.createElement('canvas');

    //App.button = document.createElement('button');
    //document.getElementsByTagName('article')[0].appendChild(App.button);

canvas.height = 630;
canvas.width = 1500;
document.getElementsByTagName('article')[0].appendChild(canvas);
ctx = canvas.getContext("2d");
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

socket.on('server_editor', function(data) {
        $('#editor').val(data);
        prev_content = data;
        console.log(data);
    });

socket.on('disconnect', function(){
        console.log('disconnect');
        socket.disconnect();
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
        if (content !== prev_content)
            socket.emit('client_editor', $("#editor").val());
    }

setInterval(emitClientEditor, 1000);


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
