import React, { useState } from "react";
import { Eye, Trash2, Heart } from "lucide-react";
import { useNavigate } from "react-router-dom";

export default function SavedCareers() {
  const navigate = useNavigate();
  const [careers, setCareers] = useState([
    {
      title: "Software Engineer",
      match: 92,
      savedDate: "January 15, 2024",
      description:
        "Design, develop, and maintain software applications and systems using various programming languages and frameworks.",
      salary: "₹40,000 - ₹1,80,000",
      growth: "22% growth",
      growthColor: "text-purple-600",
      salaryColor: "text-green-600",
      path: ["Programming Basics", "Web Development", "System Architecture"],
    },
    {
      title: "Data Scientist",
      match: 87,
      savedDate: "January 10, 2024",
      description:
        "Analyze complex datasets to extract insights and build predictive models for business decision-making.",
      salary: "₹40,000 - ₹1,90,000",
      growth: "35% growth",
      growthColor: "text-purple-600",
      salaryColor: "text-green-600",
      path: ["Statistics", "Machine Learning", "Data Visualization"],
    },
  ]);

  const handleDelete = (index) => {
    setCareers(careers.filter((_, i) => i !== index));
  };

  const handleViewDetails = (career) => {
   navigate("/career-details", { state: { career } });

  };

  return (
    <div className="max-w-7xl mx-auto px-6 py-10">
      {/* Header */}
      <div className="mb-8 flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold flex items-center gap-2">
            <Heart className="w-7 h-7 text-blue-600" strokeWidth={2} /> Saved Careers
          </h1>
          <p className="text-gray-500">
            Your personalized career paths and learning roadmaps
          </p>
        </div>
        {/* <button className="px-4 py-2 bg-gradient-to-r from-purple-500 to-indigo-500 text-white rounded-lg shadow hover:opacity-90">
          Take New Quiz
        </button> */}
          <button
    onClick={() => navigate("/quiz")}  // 👈 navigate to quiz page
    className="px-4 py-2 bg-gradient-to-r from-purple-500 to-indigo-500 text-white rounded-lg shadow hover:opacity-90"
  >
    Take New Quiz
  </button>
      </div>

      {/* Cards Grid */}
      <div className="grid md:grid-cols-2 gap-6">
        {careers.map((career, i) => (
          <div
            key={i}
            className="relative bg-white rounded-2xl p-6 shadow-sm transition-transform transform hover:-translate-y-2 hover:shadow-[0_8px_24px_rgba(124,58,237,0.2)] group"
          >
            {/* Title + Match */}
            <h2 className="text-xl font-bold text-blue-600">{career.title}</h2>
            <p className="text-sm text-gray-500 mt-1">
              {career.match}% match • Saved {career.savedDate}
            </p>

            {/* Description */}
            <p className="mt-3 text-gray-600">{career.description}</p>

            {/* Salary + Growth */}
            <div className="flex items-center gap-6 mt-4">
              <p className={`${career.salaryColor} font-medium`}>
                💰 {career.salary}
              </p>
              <p className={`${career.growthColor} font-medium`}>
                ⏱ {career.growth}
              </p>
            </div>

            {/* Learning Path */}
            <div className="mt-5">
              <p className="font-semibold">Learning Path Preview</p>
              <div className="flex flex-wrap gap-2 mt-2">
                {career.path.map((topic, j) => (
                  <span
                    key={j}
                    className="px-3 py-1 bg-blue-100 text-blue-600 text-sm rounded-lg"
                  >
                    {topic}
                  </span>
                ))}
              </div>
            </div>

            {/* Actions */}
            <div className="flex items-center justify-between mt-6">
              <button
                onClick={() => handleViewDetails(career)}
                className="flex items-center justify-center gap-2 w-full md:w-auto px-6 py-2 bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-lg hover:opacity-90"
              >
                <Eye className="w-4 h-4" />
                View Details
              </button>
            </div>

            {/* Hidden Delete Button - shows on hover */}
            <button
              onClick={() => handleDelete(i)}
              className="absolute bottom-6 right-6 hidden group-hover:flex items-center gap-1 px-3 py-1.5 rounded-lg bg-red-50 text-red-600 border border-red-300 hover:bg-red-100 transition"
            >
              <Trash2 className="w-4 h-4" />
              Delete
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
