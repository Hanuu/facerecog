var express = require("express"); 
var app = express();
var bodyParser = require('body-parser'); // for app.post 
var http = require("http");

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());



app.get('/status', function(req, res){
	var json = {
		name : "hi",
		carry: 0
		};
	//To run python code & run 
	var spawn = require('child_process').spawn
		ls = spawn('python', ['gyro_carry.py']);
	
	ls.stderr.on('data', function(data){
		console.log('stderr: '+ data);
	});
	
	ls.stdout.on('data', function(data){
		console.log('stdout: '+ data);
		var str = data.toString().trim();
		json = {
			name : "hi",
			carry: str
		}
		
		res.json(json)
		res.end()
		console.log("send On status to server");
	});
	


});

app.listen(3000, function(){
	console.log('Connected to 3000 port!');
})

