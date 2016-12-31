// require part
var express = require('express');
var app = express();
var path = require("path");
var http = require('http').createServer(app);
var io = require('socket.io')(http);
var googlediff = require('googlediff');
var dmp = new googlediff();
var changeset = require('changesets').Changeset;

app.use(express.static(path.join(__dirname, 'public')));

// data part
var client_id = 0;			// assign id to different id
var prev_user = 0;			// last user who makes change
var prev_content = "";		// information about last change
var prev_operation = null;	// last operation used for transformation


app.get('/', function(req, res){
	res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket) {
	console.log("new user connected");
	client_id += 1;
    io.emit("assign_id", client_id);

	socket.on('drawClick', function(data) {
	    socket.broadcast.emit('draw', {
	      x: data.x,
	      y: data.y,
	      type: data.type
	    });
	});

	socket.on('clear', function(data) {
	    socket.broadcast.emit('clear', {

	    });
	});

	socket.on('disconnect', function(){
		console.log('user disconnect');
		socket.disconnect();
	});

	socket.on('client_editor', function(data) {
    	console.log(data);
    	if (prev_user === 0){
    		io.emit("server_editor", data);
    		prev_user = data.id;
    		prev_operation = changeset.fromDiff(dmp.diff_main(prev_content, data.content));
    		// prev_content = data.content;
    	} else if (prev_user === data.id){
    		io.emit("server_editor", data);
    		prev_user = data.id;
    		prev_content = prev_operation.apply(prev_content);
    		prev_operation = changeset.fromDiff(dmp.diff_main(prev_content, data.content));
    		// prev_content = prev_operation.apply(prev_content);
    	} else { // prev_user !== data.id
    		var operation = changeset.fromDiff(dmp.diff_main(prev_content, data.content));
    		var new_operation = operation.transformAgainst(prev_operation);

    		prev_content = prev_operation.apply(prev_content);
    		var new_content = new_operation.apply(new_operation.apply(prev_content));

    		io.emit("server_editor",{
    			'id': data.id,
    			'content': new_content
    		});

    		prev_user = data.id;
    		prev_operation = new_operation;
    	}
    });
});

setInterval(function(){
	if (prev_user !== 0){
		prev_user = 0;
		prev_content = prev_operation.apply(prev_content);
		io.emit('server_editor', {
			'id': 0,
			'content': prev_content
		});
		prev_operation = null;
	}
}, 500);

http.listen(4000, function(){
	console.log('listening on *:4000');
}); 