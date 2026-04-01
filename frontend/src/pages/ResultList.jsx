// import React from "react";
// import { useLocation, useNavigate } from "react-router-dom";
// import { Doughnut } from "react-chartjs-2";
// import ChartDataLabels from "chartjs-plugin-datalabels";

// import {
//   Chart as ChartJS,
//   RadialLinearScale,
//   PointElement,
//   LineElement,
//   Filler,
//   Tooltip,
//   Legend
// } from "chart.js";

// import { ArcElement} from "chart.js";

// ChartJS.register(
//   ArcElement,
//   Tooltip,
//   Legend,
//   ChartDataLabels
// );

// export default function ResultList() {
//   const location = useLocation();
//   const navigate = useNavigate();

//   // CORRECT STATE ACCESS
//   const predictions = location.state?.predictions;
//   const riasecScores = location.state?.riasecScores;
//    const donutData = {
//   labels: [
//     "Realistic",
//     "Investigative",
//     "Artistic",
//     "Social",
//     "Enterprising",
//     "Conventional"
//   ],
//   datasets: [
//     {
//       data: [
//         riasecScores?.R || 0,
//         riasecScores?.I || 0,
//         riasecScores?.A || 0,
//         riasecScores?.S || 0,
//         riasecScores?.E || 0,
//         riasecScores?.C || 0
//       ],
//       backgroundColor: [
//   "#6366F1", // indigo
//   "#F59E0B", // amber
//   "#10B981", // emerald
//   "#EF4444", // red
//   "#8B5CF6", // violet
//   "#64748B"  // slate
// ],
//       borderWidth: 0
//     }
//   ]
// };

// const donutOptions = {
//   cutout: "60%",
//   plugins: {
//     legend: {
//       position: "right"
//     },
//     datalabels: {
//       color: "white",
//       font: {
//         weight: "bold",
//         size: 14
//       },
//       formatter: (value, context) => {
//         const data = context.chart.data.datasets[0].data;
//         const total = data.reduce((a, b) => a + b, 0);
//         const percentage = ((value / total) * 100).toFixed(1) + "%";
//         return percentage;
//       }
//     }
//   }
// };

// const getAssociation = () => {

//   const pairs = [
//     {t:["R","I"], label:"R + I → Technical orientation"},
//     {t:["I","C"], label:"I + C → Data-oriented thinking"},
//     {t:["A","I"], label:"A + I → Creative technology interest"},
//     {t:["E","S"], label:"E + S → Leadership & management"},
//     {t:["S","C"], label:"S + C → Support & QA roles"},
//     {t:["R","S"], label:"R + S → Security & cloud systems"}
//   ];

//   let best = "";
//   let score = 0;

//   pairs.forEach(p => {

//     const s = (riasecScores[p.t[0]] || 0) + (riasecScores[p.t[1]] || 0);

//     if(s > score){
//       score = s;
//       best = p.label;
//     }

//   });

//   return best;
// };

//   if (!predictions || !Array.isArray(predictions.suggestions)) {
//     return (
//       <div className="min-h-screen flex items-center justify-center">
//         <p className="text-gray-500">
//           No predictions found. Complete the quiz first.
//         </p>
//       </div>
//     );
//   }

//   return (
//     // <div className="max-w-4xl mx-auto px-6 py-10">
//     <div className="min-h-screen flex flex-col items-center justify-center bg-slate-50 px-6 py-10">

//       {/* ===== TOP 3 PREDICTIONS ===== */}
//       <div className="mb-8">
//         {/* ===== RIASEC VISUALIZATION ===== */}

// <div className="mb-10 flex flex-col items-center">

//  <h1 className="text-3xl font-bold text-slate-800 tracking-wide mb-6">
//   Your RIASEC Profile
// </h1>

//   {/* <div className="w-[420px]">
//     <Doughnut data={donutData} options={donutOptions} />
//   </div> */}
//   <div className="w-[420px] flex justify-center items-center">
//   <Doughnut data={donutData} options={donutOptions} />
// </div>

//   {/* <div className="mt-4 bg-gray-100 px-4 py-2 rounded-lg text-gray-700">
//     Strong Association: {getAssociation()}
//   </div> */}
//   <div className="mt-6 px-6 py-3 rounded-xl bg-indigo-100 text-indigo-800 font-semibold shadow-sm">
//   Strong Association: {getAssociation()}
// </div>

// </div>
//         {/* <h1 className="text-3xl font-bold mb-2">Career Suggestions</h1>
//         <p className="text-gray-500 mb-4">
//           Based on your responses, here are your best CS/IT career matches
//         </p> */}
        
//         <div className="text-center mt-12">
//   <h2 className="text-3xl font-bold text-slate-800">
//     Career Suggestions
//   </h2>

//   <p className="text-slate-500 mt-2">
//     Based on your responses, here are your best CS/IT career matches
//   </p>
// </div>

//         {/* <div className="flex flex-wrap gap-3">
//           {predictions.top_3_careers.map((c, index) => (
//             <div
//               key={c.interest}
//               className={`px-4 py-2 rounded-full text-sm font-semibold
//                 ${
//                   index === 0
//                     ? "bg-green-100 text-green-700"
//                     : "bg-purple-100 text-purple-700"
//                 }`}
//             >
//               {index + 1}. {c.interest} — {Math.round(c.confidence * 100)}%
//             </div>
//           ))}
//         </div> */}
//       </div>

//       {/* ===== SUGGESTION CARDS ===== */}
//       {/* <div className="grid sm:grid-cols-2 gap-6"> */}
//       <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8 max-w-5xl">
//         {predictions.suggestions.slice(0, 3).map((career) => (

//           <button
//             key={career.id}
//             onClick={() =>
//               navigate("/result-details", { state: { career } })
//             }
//             className="text-left bg-white p-6 rounded-2xl shadow-md
//                        hover:-translate-y-1 transition-transform duration-150"
//           >
//             <div className="flex items-center justify-between">
//               <h2 className="text-xl font-semibold text-purple-700">
//                 {career.title}
//               </h2>
//               <span className="text-sm text-gray-400">
//                 {career.category}
//               </span>
//             </div>

//             <p className="text-gray-600 mt-2">
//               {career.description}
//             </p>
//           </button>
//         ))}
//       </div>
//     </div>
//   );
// }
//********************************************************************************************************* */
import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { Doughnut } from "react-chartjs-2";
import ChartDataLabels from "chartjs-plugin-datalabels";

import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
} from "chart.js";

import { ArcElement} from "chart.js";

ChartJS.register(
  ArcElement,
  Tooltip,
  Legend,
  ChartDataLabels
);

export default function ResultList() {
  const location = useLocation();
  const navigate = useNavigate();

  // CORRECT STATE ACCESS
  const predictions = location.state?.predictions;
  const riasecScores = location.state?.riasecScores;
   const donutData = {
  labels: [
    "Realistic",
    "Investigative",
    "Artistic",
    "Social",
    "Enterprising",
    "Conventional"
  ],
  datasets: [
    {
      data: [
        riasecScores?.R || 0,
        riasecScores?.I || 0,
        riasecScores?.A || 0,
        riasecScores?.S || 0,
        riasecScores?.E || 0,
        riasecScores?.C || 0
      ],
      backgroundColor: [
  "#6366F1", // indigo
  "#F59E0B", // amber
  "#10B981", // emerald
  "#EF4444", // red
  "#8B5CF6", // violet
  "#64748B"  // slate
],
      borderWidth: 0
    }
  ]
};

const donutOptions = {
  cutout: "60%",
  plugins: {
    legend: {
      position: "right"
    },
    datalabels: {
      color: "white",
      font: {
        weight: "bold",
        size: 14
      },
      formatter: (value, context) => {
        const data = context.chart.data.datasets[0].data;
        const total = data.reduce((a, b) => a + b, 0);
        const percentage = ((value / total) * 100).toFixed(1) + "%";
        return percentage;
      }
    }
  }
};

// const getAssociation = () => {

//   const pairs = [
//     {t:["R","I"], label:"R + I → Technical orientation"},
//     {t:["I","C"], label:"I + C → Data-oriented thinking"},
//     {t:["A","I"], label:"A + I → Creative technology interest"},
//     {t:["E","S"], label:"E + S → Leadership & management"},
//     {t:["S","C"], label:"S + C → Support & QA roles"},
//     {t:["R","S"], label:"R + S → Security & cloud systems"}
//   ];

//   let best = "";
//   let score = 0;

//   pairs.forEach(p => {

//     const s = (riasecScores[p.t[0]] || 0) + (riasecScores[p.t[1]] || 0);

//     if(s > score){
//       score = s;
//       best = p.label;
//     }

//   });

//   return best;
// };

  if (!predictions || !Array.isArray(predictions.suggestions)) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-gray-500">
          No predictions found. Complete the quiz first.
        </p>
      </div>
    );
  }

  return (
    // <div className="max-w-4xl mx-auto px-6 py-10">
    <div className="min-h-screen flex flex-col items-center justify-center bg-slate-50 px-6 py-10">

      {/* ===== TOP 3 PREDICTIONS ===== */}
      <div className="mb-8">
        {/* ===== RIASEC VISUALIZATION ===== */}

<div className="mb-10 flex flex-col items-center">

 <h1 className="text-3xl font-bold text-slate-800 tracking-wide mb-6">
  Your RIASEC Profile
</h1>

  {/* <div className="w-[420px]">
    <Doughnut data={donutData} options={donutOptions} />
  </div> */}
  <div className="w-[420px] flex justify-center items-center">
  <Doughnut data={donutData} options={donutOptions} />
</div>

  {/* <div className="mt-4 bg-gray-100 px-4 py-2 rounded-lg text-gray-700">
    Strong Association: {getAssociation()}
  </div> */}
  {/* <div className="mt-6 px-6 py-3 rounded-xl bg-indigo-100 text-indigo-800 font-semibold shadow-sm">
  Strong Association: {getAssociation()}
</div> */}

</div>
        {/* <h1 className="text-3xl font-bold mb-2">Career Suggestions</h1>
        <p className="text-gray-500 mb-4">
          Based on your responses, here are your best CS/IT career matches
        </p> */}
        {/* ===== XAI EXPLANATION ===== */}
<div className="bg-white p-6 rounded-2xl shadow-md max-w-3xl mb-10">

  <h2 className="text-xl font-semibold text-indigo-700 mb-3">
    Why this recommendation?
  </h2>

  <p className="text-gray-700 mb-2">
    {predictions.explanation?.reason}
  </p>

  <p className="text-sm text-gray-500 mb-4">
    Confidence: {predictions.explanation?.confidence}%
  </p>

  <h3 className="font-semibold text-gray-800 mb-2">
    Your Strengths:
  </h3>

  <div className="flex gap-3 flex-wrap">
    {predictions.explanation?.top_traits?.map((t, i) => (
      <span
        key={i}
        className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm"
      >
        {t[0]}
      </span>
    ))}
  </div>

</div>

        <div className="text-center mt-12">
  <h2 className="text-3xl font-bold text-slate-800">
    Career Suggestions
  </h2>

  <p className="text-slate-500 mt-2">
    Based on your responses, here are your best CS/IT career matches
  </p>
</div>

        {/* <div className="flex flex-wrap gap-3">
          {predictions.top_3_careers.map((c, index) => (
            <div
              key={c.interest}
              className={`px-4 py-2 rounded-full text-sm font-semibold
                ${
                  index === 0
                    ? "bg-green-100 text-green-700"
                    : "bg-purple-100 text-purple-700"
                }`}
            >
              {index + 1}. {c.interest} — {Math.round(c.confidence * 100)}%
            </div>
          ))}
        </div> */}
      </div>

      {/* ===== SUGGESTION CARDS ===== */}
      {/* <div className="grid sm:grid-cols-2 gap-6"> */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8 max-w-5xl">
        {predictions.suggestions.slice(0, 3).map((career) => (

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
{/* 
            <p className="text-gray-600 mt-2">
              {career.description}
            </p> */}
            <p className="text-gray-600 mt-2">
  {career.description}
</p>

<p className="mt-2 text-sm text-indigo-600 font-semibold">
  Match: {career.match_score}%
</p>

<p className="text-xs text-gray-500 mt-1">
  {career.explanation}
</p>

          </button>
        ))}
      </div>
    </div>
  );
}
