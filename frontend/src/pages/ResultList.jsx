// // src/pages/ResultList.jsx
// import React from "react";
// import { useLocation, useNavigate } from "react-router-dom";

// export default function ResultList() {
//   const location = useLocation();
//   const navigate = useNavigate();

//   // predictions object must be passed via router state from Quiz
//   const predictions = location.state?.predictions;

//   if (!predictions) {
//     return (
//       <div className="min-h-screen flex items-center justify-center">
//         <p className="text-gray-500">No predictions found. Complete the quiz first.</p>
//       </div>
//     );
//   }

//   return (
//     <div className="max-w-4xl mx-auto px-6 py-10">
//       <div className="flex items-center justify-between mb-6">
//         <h1 className="text-3xl font-bold">Career Suggestions</h1>
//         <p className="text-gray-500">Click any card to view detailed roadmap & resources</p>
//       </div>

//       <div className="grid sm:grid-cols-2 gap-6">
//         {predictions.suggestions.map((career) => (
//           <button
//             key={career.id}
//              onClick={() => navigate("/result-details", { state: { career } })}
//             className="text-left bg-white p-6 rounded-2xl shadow-md hover:-translate-y-1 transition-transform duration-150"
//           >
//             <div className="flex items-center justify-between">
//               <h2 className="text-xl font-semibold text-purple-700">{career.title}</h2>
//               <span className="text-sm text-gray-400">{career.category}</span>
//             </div>
//             <p className="text-gray-600 mt-2">{career.description}</p>
//           </button>
//         ))}
//       </div>
//     </div>
//   );
// }
//**************************************************************************************************************************8 */
// src/pages/ResultList.jsx
import React from "react";
import { useLocation, useNavigate } from "react-router-dom";

export default function ResultList() {
  const location = useLocation();
  const navigate = useNavigate();

  // predictions object must be passed via router state from Quiz
  const predictions = location.state?.predictions;

  if (!predictions) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-gray-500">No predictions found. Complete the quiz first.</p>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-6 py-10">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-3xl font-bold">Career Suggestions</h1>
        <p className="text-gray-500">Click any card to view detailed roadmap & resources</p>
      </div>

      <div className="grid sm:grid-cols-2 gap-6">
        {predictions.suggestions.map((career) => (
          <button
            key={career.id}
            onClick={() => navigate("/result-details", { state: { career } })}
            className="text-left bg-white p-6 rounded-2xl shadow-md hover:-translate-y-1 transition-transform duration-150"
          >
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-semibold text-purple-700">{career.title}</h2>
              <span className="text-sm text-gray-400">{career.category}</span>
            </div>

            <p className="text-gray-600 mt-2">{career.description}</p>
          </button>
        ))}
      </div>
    </div>
  );
}
