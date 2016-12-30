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
var record = {
	"origin": "",
	"change1": ""
};
var prev_operation = null;
var msg_count = 0;


app.get('/', function(req, res){
	res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket) {
	console.log("new user connected");

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

	socket.on('client_editor', function(data){
		// receive client_editor message
		// 1st time record data and operation
		// 2nd time transform the operation

		var diff = dmp.diff_main(record.origin, data);
		var operation = changeset.fromDiff(diff);
		if (prev_operation === null){
			prev_operation = operation;
			record.change1 = data;
			msg_count += 1;
			console.log("1st operation: " + prev_operation);
		}
		else {
			var new_operation = operation.transformAgainst(prev_operation);
			prev_operation = new_operation;
			msg_count += 1;
			console.log("2nd operation: " + prev_operation);
		}
	});	
});

function emitServerEditor(){
	// emit server_editor message to client
	// if there is old operation not applied
	if (prev_operation !== null){
		if (msg_count === 1)
			var new_content = prev_operation.apply(record.origin);
		else if (msg_count === 2)
			var new_content = prev_operation.apply(record.change1);

		console.log("new content: " + new_content);
		io.emit("server_editor", new_content);
		prev_operation = null;
		counter = 0;
		msg_count = 0;
		record = {
			"origin": new_content,
			"change1": ""
		};
	}
}

setInterval(emitServerEditor, 200);

http.listen(4000, function(){
	console.log('listening on *:4000');
}); 