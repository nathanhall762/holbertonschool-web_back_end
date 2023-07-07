// this is the server
const express = require('express');
const routes = require('./routes/index');

const app = express();
const port = 1245;

// Use the routes defined in full_server/routes/index.js
app.use('/', routes);

// Start the server
app.listen(port, () => {
	console.log(`Server is running on port ${port}`);
});
