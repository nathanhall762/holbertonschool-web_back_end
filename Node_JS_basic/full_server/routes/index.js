const express = require('express');
const router = express.Router();

// Import the controllers
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

// Route: /
router.get('/', AppController.index);

// Route: /students
router.get('/students', StudentsController.index);

// Route: /students/:major
router.get('/students/:major', StudentsController.getByMajor);

module.exports = router;
