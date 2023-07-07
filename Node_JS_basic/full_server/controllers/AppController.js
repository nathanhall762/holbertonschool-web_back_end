class AppController {
	getHomepage(req, res) {
		res.send('Hello Holberton School!');
	}
}

module.exports = AppController;