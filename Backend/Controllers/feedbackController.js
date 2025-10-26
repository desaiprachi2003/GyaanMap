const Feedback = require("../Models/Feedback");

// POST: Add feedback for a career
exports.addFeedback = async (req, res) => {
  try {
    const userId = req.user.id; // from auth middleware
    const { careerId, rating, relevant, comment } = req.body;

    if (!careerId || !rating || relevant === undefined) {
      return res.status(400).json({ error: "All fields are required" });
    }

    const feedback = new Feedback({
      user: userId,
      career: careerId,
      rating,
      relevant,
      comment
    });

    await feedback.save();
    res.status(201).json({ message: "Feedback submitted successfully", feedback });
  } catch (err) {
    console.error("Feedback Error:", err);
    res.status(500).json({ error: "Failed to submit feedback" });
  }
};

// GET: Get all feedback for a specific career
exports.getCareerFeedback = async (req, res) => {
  try {
    const { careerId } = req.params;
    const feedbacks = await Feedback.find({ career: careerId }).populate("user", "name email");
    res.json(feedbacks);
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch feedback" });
  }
};

// GET: Get feedback submitted by logged-in user
exports.getMyFeedback = async (req, res) => {
  try {
    const userId = req.user.id;
    const feedbacks = await Feedback.find({ user: userId }).populate("career", "title");
    res.json(feedbacks);
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch user feedback" });
  }
};
