// import React, { useState } from "react";
// import { Star, Download, Heart,ArrowRight } from "lucide-react";
// import Feedback from "../components/Feedback";

// export default function Result() {
//   const [saved, setSaved] = useState(false);

//   // === Dynamic data (replace with API/Context later) ===
//   const career = {
//     title: "Software Engineer",
//     description:
//       "Design, develop, and maintain software applications and systems using various programming languages and frameworks.",
//     matchConfidence: 92,
//     salaryRange: "$95,000 - $180,000",
//     jobGrowth: "22% (Much faster than average)",
//     skills: ["Programming", "Problem Solving", "System Design", "Testing", "Collaboration"],
//   };

//   const roadmap = [
//     {
//       level: "Foundation",
//       duration: "3-6 months",
//       topics: ["Programming Basics", "Data Structures", "Algorithms"],
//     },
//     {
//       level: "Intermediate",
//       duration: "6-12 months",
//       topics: ["Web Development", "Database Management", "Version Control"],
//     },
//     {
//       level: "Advanced",
//       duration: "12-18 months",
//       topics: ["System Architecture", "Cloud Computing", "DevOps"],
//     },
//     {
//       level: "Specialization",
//       duration: "18+ months",
//       topics: ["AI/ML", "Mobile Development", "Leadership"],
//     },
//   ];

//   const resources = [
//     { title: "CS50’s Introduction to Computer Science", platform: "Harvard (edX)", rating: 4.9, logo: "📘" },
//     { title: "The Complete Web Developer Course", platform: "Udemy", rating: 4.8, logo: "💻" },
//     { title: "Programming with Python", platform: "YouTube", rating: 4.7, logo: "▶️" },
//   ];

//   return (
//     <div className="max-w-7xl mx-auto px-6 py-8">
//       {/* Header */}
//       <div className="mb-8 text-center relative">
//         <button
//           onClick={() => window.history.back()}
//           className="absolute left-0 top-0 text-gray-600 hover:text-purple-600 flex items-center gap-1"
//         >
//           ← Back to Quiz
//         </button>
//         <h1 className="text-3xl font-bold">Your Career Match Results</h1>
//         <p className="text-gray-500 mt-1">
//           Based on your responses, here&apos;s your personalized career recommendation
//         </p>
//       </div>

//       {/* Career + Roadmap + Resources */}
//       <div className="grid lg:grid-cols-3 gap-6">
//         {/* Career Info + Roadmap */}
//         <div className="lg:col-span-2 space-y-6">
//           {/* Career Info */}
//           {/* <section className="bg-white shadow-md rounded-2xl p-6 relative"> */}
//           <section className="bg-white shadow-md rounded-2xl p-6 relative transition-transform transform hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(124,58,237,0.25)]">

//             {/* Save button */}
//             <div className="absolute top-6 right-6">
//               <button
//                 onClick={() => setSaved(!saved)}
//                 className={`flex items-center gap-2 px-3 py-1 rounded-lg border transition ${
//                   saved
//                     ? "text-green-600 border-green-400 bg-green-50"
//                     : "text-gray-600 border-gray-300 hover:text-green-600 hover:border-green-400"
//                 }`}
//               >
//                 <Heart className={`w-4 h-4 ${saved ? "fill-green-500" : ""}`} />
//                 Save
//               </button>
//             </div>

//             <h1 className="text-2xl font-bold text-purple-700">{career.title}</h1>
//             <p className="text-gray-600 mt-2">{career.description}</p>

//             <div className="mt-4">
//               <p className="font-semibold">Match Confidence</p>
//               <div className="w-full bg-gray-200 rounded-full h-3 mt-2">
//                 <div
//                   className="bg-gradient-to-r from-purple-500 to-indigo-500 h-3 rounded-full"
//                   style={{ width: `${career.matchConfidence}%` }}
//                 />
//               </div>
//               <p className="mt-1 text-sm font-medium text-purple-600">{career.matchConfidence}%</p>
//             </div>

//             <div className="grid grid-cols-2 gap-6 mt-6">
//               <div>
//                 <p className="text-gray-500 text-sm">Salary Range</p>
//                 <p className="font-medium">{career.salaryRange}</p>
//               </div>
//               <div>
//                 <p className="text-gray-500 text-sm">Job Growth</p>
//                 <p className="font-medium">{career.jobGrowth}</p>
//               </div>
//             </div>

//             <div className="mt-6">
//               <p className="font-semibold">Key Skills Required</p>
//               <div className="flex flex-wrap gap-2 mt-2">
//                 {career.skills.map((skill, i) => (
//                   <span
//                     key={i}
//                     className="px-3 py-1 bg-blue-100 text-blue-600 text-sm rounded-lg"
//                   >
//                     {skill}
//                   </span>
//                 ))}
//               </div>
//             </div>
//           </section>

//           {/* Learning Roadmap */}
//           {/* <section className="bg-white shadow-md rounded-2xl p-6"> */}
//           <section className="bg-white shadow-md rounded-2xl p-6 transition-transform transform hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(124,58,237,0.25)]">

//             <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
//               <span className="text-purple-600">📘</span> Learning Roadmap
//             </h2>
//             <div className="space-y-4">
//               {roadmap.map((step, i) => (
//                 <div
//                   key={i}
//                   className="rounded-xl p-5 bg-white shadow-sm transition-transform transform hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(124,58,237,0.25)]"
//                 >
//                   <div className="flex items-center justify-between mb-3">
//                     <p className="font-semibold flex items-center gap-2">
//                       <span className="w-6 h-6 flex items-center justify-center text-sm font-bold text-white bg-gradient-to-r from-purple-500 to-indigo-500 rounded-full">
//                         {i + 1}
//                       </span>
//                       {step.level}
//                     </p>
//                     <p className="text-sm text-gray-500 flex items-center gap-1">⏱ {step.duration}</p>
//                   </div>
//                   <div className="flex flex-wrap gap-2">
//                     {step.topics.map((topic, j) => (
//                       <span
//                         key={j}
//                         className="px-3 py-1 bg-gray-100 text-gray-700 text-sm rounded-lg"
//                       >
//                         {topic}
//                       </span>
//                     ))}
//                   </div>
//                 </div>
//               ))}
//             </div>
//           </section>
//         </div>

//         {/* Recommended Resources + Next Steps */}
//         <aside className="space-y-6">
         

// {/* Resources */}

// <div className="bg-white shadow-md rounded-2xl p-6 transition-transform transform hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(124,58,237,0.25)]">

//   <h2 className="text-xl font-semibold mb-4">Recommended Resources</h2>
//   <div className="space-y-3">
//     {resources.map((r, i) => (
//       <div
//         key={i}
//         className="rounded-xl p-3 flex justify-between items-center bg-white shadow-sm hover:shadow-md transition"
//       >
//         <div>
//           <p className="font-medium">{r.title}</p>
//           <p className="text-sm text-gray-500">{r.platform}</p>
//           <div className="flex items-center gap-1 text-green-600 font-medium mt-1">
//             <Star className="w-4 h-4 fill-green-500 text-green-500" />
//             {r.rating}
//           </div>
//         </div>
//         <button
//           className="p-2 rounded-full hover:bg-purple-100 text-purple-600"
//           onClick={() => alert(`Redirect to ${r.title}`)} // placeholder for future redirect
//         >
//           <ArrowRight className="w-5 h-5" />
//         </button>
//       </div>
//     ))}
//   </div>
// </div>


//           {/* Next Steps */}
         
//           <div className="bg-white shadow-md rounded-2xl p-6 transition-transform transform hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(124,58,237,0.25)]">

//             <h2 className="text-xl font-semibold mb-4">Next Steps</h2>
           
//             <div className="flex flex-col gap-3">
//   <button className="w-full border rounded-lg py-2 transition transform hover:-translate-y-1 hover:bg-green-500 hover:text-white">
//     Retake Quiz
//   </button>
//   <button className="w-full border rounded-lg py-2 transition transform hover:-translate-y-1 hover:bg-green-500 hover:text-white">
//     View Saved Careers
//   </button>
//   <button className="w-full flex items-center justify-center gap-2 bg-gradient-to-r from-purple-500 to-indigo-500 text-white py-2 rounded-lg hover:opacity-90">
//     <Download className="w-4 h-4" />
//     Download PDF Report
//   </button>
// </div>
//   {/* Feedback*/}
//    <div className=" pt-4 mt-4">
//     <Feedback />
//   </div>

//           </div>

         
//         </aside>
//       </div>
//     </div>
//   );
// }
//********************************************************************************************************** */
import React, { useState } from "react";
import { Star, Download, Heart, ArrowRight } from "lucide-react";
import { useLocation } from "react-router-dom";
import Feedback from "../components/Feedback";

export default function ResultDetails() {
  const [saved, setSaved] = useState(false);

  // === Get Career From Navigation ===
  const location = useLocation();
  const career = location.state?.career;

  // If user visits directly without selecting a career
  if (!career) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-gray-500 text-lg">
          No career selected. Please go back and choose an option.
        </p>
      </div>
    );
  }

  // Dummy roadmap + resources (same as before)
  const roadmap = [
    {
      level: "Foundation",
      duration: "3-6 months",
      topics: ["Programming Basics", "Data Structures", "Algorithms"],
    },
    {
      level: "Intermediate",
      duration: "6-12 months",
      topics: ["Web Development", "Database Management", "Version Control"],
    },
    {
      level: "Advanced",
      duration: "12-18 months",
      topics: ["System Architecture", "Cloud Computing", "DevOps"],
    },
    {
      level: "Specialization",
      duration: "18+ months",
      topics: ["AI/ML", "Mobile Development", "Leadership"],
    },
  ];

  const resources = [
    { title: "CS50’s Introduction to Computer Science", platform: "Harvard (edX)", rating: 4.9, logo: "📘" },
    { title: "The Complete Web Developer Course", platform: "Udemy", rating: 4.8, logo: "💻" },
    { title: "Programming with Python", platform: "YouTube", rating: 4.7, logo: "▶️" },
  ];

  return (
    <div className="max-w-7xl mx-auto px-6 py-8">
      {/* Header */}
      <div className="mb-8 text-center relative">
        <button
          onClick={() => window.history.back()}
          className="absolute left-0 top-0 text-gray-600 hover:text-purple-600 flex items-center gap-1"
        >
          ← Back to Results
        </button>
        <h1 className="text-3xl font-bold">Your Career Match Results</h1>
        <p className="text-gray-500 mt-1">
          Based on your selection, here&apos;s your detailed career roadmap
        </p>
      </div>

      {/* Career + Roadmap + Resources */}
      <div className="grid lg:grid-cols-3 gap-6">
        {/* Career Info + Roadmap */}
        <div className="lg:col-span-2 space-y-6">
          {/* Career Info */}
          <section className="bg-white shadow-md rounded-2xl p-6 relative transition-transform transform hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(124,58,237,0.25)]">
            {/* Save button */}
            <div className="absolute top-6 right-6">
              <button
                onClick={() => setSaved(!saved)}
                className={`flex items-center gap-2 px-3 py-1 rounded-lg border transition ${
                  saved
                    ? "text-green-600 border-green-400 bg-green-50"
                    : "text-gray-600 border-gray-300 hover:text-green-600 hover:border-green-400"
                }`}
              >
                <Heart className={`w-4 h-4 ${saved ? "fill-green-500" : ""}`} />
                Save
              </button>
            </div>

            <h1 className="text-2xl font-bold text-purple-700">{career.title}</h1>
            <p className="text-gray-600 mt-2">{career.description}</p>

            {career.matchConfidence && (
              <div className="mt-4">
                <p className="font-semibold">Match Confidence</p>
                <div className="w-full bg-gray-200 rounded-full h-3 mt-2">
                  <div
                    className="bg-gradient-to-r from-purple-500 to-indigo-500 h-3 rounded-full"
                    style={{ width: `${career.matchConfidence}%` }}
                  />
                </div>
                <p className="mt-1 text-sm font-medium text-purple-600">
                  {career.matchConfidence}%
                </p>
              </div>
            )}

            <div className="grid grid-cols-2 gap-6 mt-6">
              {career.salaryRange && (
                <div>
                  <p className="text-gray-500 text-sm">Salary Range</p>
                  <p className="font-medium">{career.salaryRange}</p>
                </div>
              )}

              {career.jobGrowth && (
                <div>
                  <p className="text-gray-500 text-sm">Job Growth</p>
                  <p className="font-medium">{career.jobGrowth}</p>
                </div>
              )}
            </div>

            {career.skills && (
              <div className="mt-6">
                <p className="font-semibold">Key Skills Required</p>
                <div className="flex flex-wrap gap-2 mt-2">
                  {career.skills.map((skill, i) => (
                    <span
                      key={i}
                      className="px-3 py-1 bg-blue-100 text-blue-600 text-sm rounded-lg"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </section>

          {/* Learning Roadmap */}
          <section className="bg-white shadow-md rounded-2xl p-6 transition-transform transform hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(124,58,237,0.25)]">
            <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
              <span className="text-purple-600">📘</span> Learning Roadmap
            </h2>
            <div className="space-y-4">
              {roadmap.map((step, i) => (
                <div
                  key={i}
                  className="rounded-xl p-5 bg-white shadow-sm transition-transform transform hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(124,58,237,0.25)]"
                >
                  <div className="flex items-center justify-between mb-3">
                    <p className="font-semibold flex items-center gap-2">
                      <span className="w-6 h-6 flex items-center justify-center text-sm font-bold text-white bg-gradient-to-r from-purple-500 to-indigo-500 rounded-full">
                        {i + 1}
                      </span>
                      {step.level}
                    </p>
                    <p className="text-sm text-gray-500 flex items-center gap-1">
                      ⏱ {step.duration}
                    </p>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {step.topics.map((topic, j) => (
                      <span
                        key={j}
                        className="px-3 py-1 bg-gray-100 text-gray-700 text-sm rounded-lg"
                      >
                        {topic}
                      </span>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </section>
        </div>

        {/* Recommended Resources + Next Steps */}
        <aside className="space-y-6">
          <div className="bg-white shadow-md rounded-2xl p-6 transition-transform transform hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(124,58,237,0.25)]">
            <h2 className="text-xl font-semibold mb-4">Recommended Resources</h2>
            <div className="space-y-3">
              {resources.map((r, i) => (
                <div
                  key={i}
                  className="rounded-xl p-3 flex justify-between items-center bg-white shadow-sm hover:shadow-md transition"
                >
                  <div>
                    <p className="font-medium">{r.title}</p>
                    <p className="text-sm text-gray-500">{r.platform}</p>
                    <div className="flex items-center gap-1 text-green-600 font-medium mt-1">
                      <Star className="w-4 h-4 fill-green-500 text-green-500" />
                      {r.rating}
                    </div>
                  </div>
                  <button
                    className="p-2 rounded-full hover:bg-purple-100 text-purple-600"
                  >
                    <ArrowRight className="w-5 h-5" />
                  </button>
                </div>
              ))}
            </div>
          </div>

          {/* Next Steps */}
          <div className="bg-white shadow-md rounded-2xl p-6 transition-transform transform hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(124,58,237,0.25)]">
            <h2 className="text-xl font-semibold mb-4">Next Steps</h2>

            <div className="flex flex-col gap-3">
              <button className="w-full border rounded-lg py-2 transition transform hover:-translate-y-1 hover:bg-green-500 hover:text-white">
                Retake Quiz
              </button>
              <button className="w-full border rounded-lg py-2 transition transform hover:-translate-y-1 hover:bg-green-500 hover:text-white">
                View Saved Careers
              </button>
              <button className="w-full flex items-center justify-center gap-2 bg-gradient-to-r from-purple-500 to-indigo-500 text-white py-2 rounded-lg hover:opacity-90">
                <Download className="w-4 h-4" />
                Download PDF Report
              </button>
            </div>

            <div className="pt-4 mt-4">
              <Feedback />
            </div>
          </div>
        </aside>
      </div>
    </div>
  );
}
