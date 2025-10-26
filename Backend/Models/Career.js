const mongoose = require("mongoose");

const CareerSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User", // career belongs to a specific user
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  salary: {
    type: String, // e.g. "₹40,000 - ₹1,80,000"
  },
  growth: {
    type: String, // e.g. "22% growth"
  },
  roadmap: [
    {
      level: String, // "Foundation"
      duration: String, // "6 months"
      topics: [String], // ["Programming Basics", "Web Development"]
    },
  ],
  resources: [
    {
      title: { type: String, required: true }, // e.g. "CS50 Course"
      link: { type: String, required: true },  // e.g. "https://cs50.harvard.edu"
    },
  ],
  savedAt: {
    type: Date,
    default: Date.now,
  },
});

module.exports = mongoose.model("Career", CareerSchema);
