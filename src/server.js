const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname+'/static/bundles')));

app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname+ '/../templates/index.html'));
});

app.listen(9000);