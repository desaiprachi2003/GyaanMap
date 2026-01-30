import React from "react";
import { useLocation, useNavigate } from "react-router-dom";

export default function ResultList() {
  const location = useLocation();
  const navigate = useNavigate();

  // ✅ CORRECT STATE ACCESS
  const predictions = location.state?.predictions;

  if (!predictions || !predictions.suggestions || !predictions.top_3_careers) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-gray-500">
          No predictions found. Complete the quiz first.
        </p>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-6 py-10">

      {/* ===== TOP 3 PREDICTIONS ===== */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">Career Suggestions</h1>
        <p className="text-gray-500 mb-4">
          Based on your responses, here are your best CS/IT career matches
        </p>

        <div className="flex flex-wrap gap-3">
          {predictions.top_3_careers.map((c, index) => (
            <div
              key={c.career}
              className={`px-4 py-2 rounded-full text-sm font-semibold
                ${
                  index === 0
                    ? "bg-green-100 text-green-700"
                    : "bg-purple-100 text-purple-700"
                }`}
            >
              {index + 1}. {c.career} — {Math.round(c.confidence * 100)}%
            </div>
          ))}
        </div>
      </div>

      {/* ===== SUGGESTION CARDS ===== */}
      <div className="grid sm:grid-cols-2 gap-6">
        {predictions.suggestions.map((career) => (
          <button
            key={career.id}
            onClick={() =>
              navigate("/result-details", { state: { career } })
            }
            className="text-left bg-white p-6 rounded-2xl shadow-md
                       hover:-translate-y-1 transition-transform duration-150"
          >
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-semibold text-purple-700">
                {career.title}
              </h2>
              <span className="text-sm text-gray-400">
                {career.category}
              </span>
            </div>

            <p className="text-gray-600 mt-2">
              {career.description}
            </p>
          </button>
        ))}
      </div>
    </div>
  );
}
