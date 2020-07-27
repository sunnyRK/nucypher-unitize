const express = require('express');
const bodyParser = require('body-parser');
const app = express();
var exec = require('child_process').exec, child;
const fs = require('fs');
var cors = require('cors');

app.use(bodyParser.json());
app.use(cors());

app.get('/encrypt', encrypt); 
app.get('/decrypt', decrypt); 
  
function encrypt(req, res) { 
      
    var spawn = require("child_process").spawn; 
    var process = spawn('python3',["./encrypt.py",
                            req.query.realnote] ); 
    
    process.stdout.on('data', function(data) { 
        console.log(data.toString())
        res.send(data.toString()); 
    }) 
} 

function decrypt(req, res) { 
      
    var spawn = require("child_process").spawn; 
    var process = spawn('python3',["./decrypt.py",
                            req.query.encryptnote] ); 
    
    process.stdout.on('data', function(data) { 
        console.log(data.toString())
        res.send(data.toString()); 
    }) 
} 

app.listen(3002, () => {
 console.log("Server running on port 3002");
});
