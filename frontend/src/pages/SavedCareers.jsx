
import { Eye, Trash2, Heart } from "lucide-react";
import { useNavigate } from "react-router-dom";
import React, { useEffect, useState } from "react";


export default function SavedCareers() {
  const navigate = useNavigate();
 const [careers, setCareers] = useState([]);
useEffect(() => {
  const fetchCareers = async () => {
    try {
      const res = await fetch("http://localhost:5000/api/careers/my", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });

      const data = await res.json();
      setCareers(data);
    } catch (err) {
      console.error("Failed to fetch careers", err);
    }
  };

  fetchCareers();
}, []);


  const handleDelete = (index) => {
    setCareers(careers.filter((_, i) => i !== index));
  };
const handleViewDetails = (id) => {
  navigate(`/career/${id}`);
};


 
  return (
  <div className="max-w-7xl mx-auto px-6 py-10">
    {/* Header */}
    <div className="mb-8 flex items-center justify-between">
      <div>
        <h1 className="text-3xl font-bold flex items-center gap-2">
          <Heart className="w-7 h-7 text-blue-600" strokeWidth={2} />
          Saved Careers
        </h1>
        <p className="text-gray-500">
          Your personalized career paths and learning roadmaps
        </p>
      </div>

      <button
        onClick={() => navigate("/quiz")}
        className="px-4 py-2 bg-gradient-to-r from-purple-500 to-indigo-500 text-white rounded-lg shadow hover:opacity-90"
      >
        Take New Quiz
      </button>
    </div>

    {/* Cards Grid */}
    <div className="grid md:grid-cols-2 gap-6">
      {careers.map((career) => (
        <div
          key={career._id}
          className="relative bg-white rounded-2xl p-6 shadow-sm transition-transform transform hover:-translate-y-2 hover:shadow-[0_8px_24px_rgba(124,58,237,0.2)] group"
        >
          {/* Title */}
          <h2 className="text-xl font-bold text-blue-600">
            {career.title}
          </h2>

          {/* Saved Date */}
          <p className="text-sm text-gray-500 mt-1">
            Saved {new Date(career.createdAt).toLocaleDateString()}
          </p>

          {/* Description */}
          <p className="mt-3 text-gray-600">
            {career.description || "No description available"}
          </p>

          {/* Roadmap Preview */}
          <div className="mt-5">
            <p className="font-semibold">Learning Path Preview</p>
            <div className="flex flex-wrap gap-2 mt-2">
              {career.roadmap?.[0]?.topics?.slice(0, 4).map((t, j) => (
                <span
                  key={j}
                  className="px-3 py-1 bg-blue-100 text-blue-600 text-sm rounded-lg"
                >
                  {t.title}
                </span>
              ))}
            </div>
          </div>

          {/* Actions */}
          <div className="flex items-center justify-between mt-6">
           <button onClick={() => handleViewDetails(career._id)}>View Details</button>

          </div>
        </div>
      ))}
    </div>
  </div>
);

}
