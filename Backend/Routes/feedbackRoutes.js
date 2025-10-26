const express = require("express");
const router = express.Router();
const feedbackController = require("../Controllers/feedbackController");
const auth = require("../Middleware/authMiddleware");

// Add feedback
router.post("/", auth, feedbackController.addFeedback);

// Get all feedback for a specific career
router.get("/career/:careerId", auth, feedbackController.getCareerFeedback);

// Get all feedback of logged-in user
router.get("/my", auth, feedbackController.getMyFeedback);

module.exports = router;
