import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";


const questions = [
  {
    question: "What type of work environment energizes you the most?",
    options: [
      "Collaborative team settings with lots of interaction",
      "Independent work with minimal supervision",
      "Dynamic environments with changing challenges",
      "Structured settings with clear processes"
    ]
  },
  {
    question: "What type of work environment energizes you the most?",
    options: [
      "Collaborative team settings with lots of interaction",
      "Independent work with minimal supervision",
      "Dynamic environments with changing challenges",
      "Structured settings with clear processes"
    ]
  },
  {
    question: "What type of work environment energizes you the most?",
    options: [
      "Collaborative team settings with lots of interaction",
      "Independent work with minimal supervision",
      "Dynamic environments with changing challenges",
      "Structured settings with clear processes"
    ]
  }
];

export default function Quiz() {

    const navigate = useNavigate();

  const [step, setStep] = useState(0);
  const [answers, setAnswers] = useState([]);

  const handleOptionClick = (optIdx) => {
    const newAnswers = [...answers];
    newAnswers[step] = optIdx;
    setAnswers(newAnswers);
  };

  const handleNext = () => {
    if (step < questions.length - 1) setStep(step + 1);
  };

  const handlePrev = () => {
    if (step > 0) setStep(step - 1);
  };


const handleSubmit = () => {
  navigate("/results", { state: { answers } });
};

// const handleSubmit = async () => {
//   try {
//     // Convert answer indices to corresponding letters
//     const answerLabels = answers.map((idx) => String.fromCharCode(65 + idx)); // 0 -> A, 1 -> B, ...

//     // Prepare payload as dictionary { Q1: "A", Q2: "C", ... }
//     const payload = {
//       answers: Object.fromEntries(
//         answerLabels.map((letter, index) => [`Q${index + 1}`, letter])
//       ),
//       free_text: "", // optional free text input
//     };

//     const response = await fetch("http://localhost:5000/api/quiz/submit", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify(payload),
//     });

//     if (!response.ok) throw new Error("Failed to get response");
    
//     const result = await response.json();
//     // Pass AI model predictions to results page
//     navigate("/results", { state: { predictions: result } });
//   } catch (error) {
//     console.error("Error submitting quiz:", error);
//   }
// };






  const handleBackToHome = () => {
  navigate("/"); // change "/" to your actual home path if different
};

const pageVariants = {
  initial: { y: 50, opacity: 0 },
  animate: { y: 0, opacity: 1 },
  exit: { y: -50, opacity: 0 }, // optional if you want exit animation
};

const pageTransition = {
  type: "tween",
  ease: "easeOut",
  duration: 0.5,
};


  return (
    <motion.div
  className="min-h-screen flex flex-col items-center bg-gray-50 py-8"
  initial={{ y: 50, opacity: 0 }}
  animate={{ y: 0, opacity: 1 }}
  exit={{ y: -50, opacity: 0 }}
  transition={{ type: "tween", ease: "easeOut", duration: 0.5 }}
>
    <div className="min-h-screen flex flex-col items-center bg-gray-50 py-8">
         {/* Header with Back button, progress bar and percent */}
    <div className="flex items-center justify-between w-full max-w-3xl mb-8">
      {/* <button
        onClick={handleBackToHome}
        className="flex items-center px-5 py-2 bg-green-400 hover:bg-green-500 text-white rounded-lg font-semibold shadow"
      >
        <span className="mr-2">&larr;</span> Back to Home
      </button> */}
        <div
    onClick={handleBackToHome}
    role="button"
    tabIndex={0}
    onKeyPress={(e) => { if (e.key === 'Enter') handleBackToHome(); }}
    className="cursor-pointer text-gray-700 hover:bg-green-400 hover:text-white px-5 py-2 rounded-lg font-semibold shadow transition-colors flex items-center"
  >
    <span className="mr-2">&larr;</span> Back to Home
  </div>

      <div className="flex-1 mx-6">
        <div className="relative w-full h-2 rounded bg-gray-200">
          <div
            className="absolute h-2 rounded bg-gradient-to-r from-blue-500 to-purple-600"
            style={{
              width: `${((step + 1) / questions.length) * 100}%`,
              transition: "width 0.3s",
            }}
          ></div>
        </div>
        <div className="text-center text-gray-500 mt-1">
          {`${Math.round(((step + 1) / questions.length) * 100)}% Complete`}
        </div>
      </div>

      <div className="text-gray-600 font-medium">{`Question ${step + 1} of ${questions.length}`}</div>
    </div>
      <div className="w-full max-w-3xl bg-white shadow-md rounded-xl p-8">
       
        <h2 className="text-3xl font-bold mb-8">
          {questions[step].question}
        </h2>
        <div className="flex flex-col gap-6 mb-10">
          {questions[step].options.map((opt, idx) => (
            <button
              key={opt}
              onClick={() => handleOptionClick(idx)}
              className={`text-lg border rounded-xl px-6 py-4 text-left transition-all ${
                answers[step] === idx
                  ? "bg-gradient-to-r from-blue-100 to-purple-100 border-blue-400"
                  : "bg-white hover:bg-gray-50"
              }`}
            >
              {opt}
            </button>
          ))}
        </div>
        <div className="flex justify-between">
          <button
            disabled={step === 0}
            onClick={handlePrev}
            className="px-5 py-2 rounded bg-gray-200 text-gray-600"
          >
            Previous
          </button>
          {step === questions.length - 1 ? (
            <button
              onClick={handleSubmit}
              className="px-6 py-2 rounded bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold"
            >
              Submit
            </button>
          ) : (
            <button
              disabled={answers[step] === undefined}
              onClick={handleNext}
              className="px-6 py-2 rounded bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold"
            >
              Next
            </button>
          )}
        </div>
      </div>
    </div>
    </motion.div>
  );
}


