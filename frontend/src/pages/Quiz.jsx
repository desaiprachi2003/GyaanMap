import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";



const questions = [
  // 1
  {
    question: "I enjoy building, fixing, or repairing things.",
    options: [
      "A - Fixing technical devices or systems",
      "B - Designing or decorating something creatively",
      "C - Organizing repair tasks or coordinating people",
      "D - Examining how things work through analysis",
      "E - Practicing physical repair activities or drills",
      "F - Helping others learn repair skills"
    ]
  },

  // 2
  {
    question: "I like using tools or machines.",
    options: [
      "A - Handling tech tools or gadgets",
      "B - Using creative tools for art or design",
      "C - Managing equipment setups for tasks",
      "D - Using devices to conduct experiments",
      "E - Using sports or fitness equipment",
      "F - Helping others learn how to use tools"
    ]
  },

  // 3
  {
    question: "I prefer working outdoors rather than indoors.",
    options: [
      "A - Handling outdoor technical equipment",
      "B - Taking inspiration for outdoor creative work",
      "C - Supervising outdoor team tasks",
      "D - Observing nature for research",
      "E - Doing outdoor sports or physical training",
      "F - Helping people in outdoor community activities"
    ]
  },

  // 4
  {
    question: "I would enjoy a career involving vehicles or machinery.",
    options: [
      "A - Working on technical systems in machines",
      "B - Designing vehicle aesthetics or interiors",
      "C - Managing transportation teams or logistics",
      "D - Researching how machines operate",
      "E - Training in motorsports or athletic machinery",
      "F - Helping people learn driving or machine handling"
    ]
  },

  // 5
  {
    question: "I enjoy solving math or logic problems.",
    options: [
      "A - Solving technical or coding problems",
      "B - Using patterns creatively in design",
      "C - Applying logic to organize plans",
      "D - Solving analytical research-based problems",
      "E - Using logic in game strategies or sports planning",
      "F - Helping others understand logical concepts"
    ]
  },

  // 6
  {
    question: "I like researching how things work.",
    options: [
      "A - Analysing technical systems and processes",
      "B - Exploring creative techniques or art styles",
      "C - Understanding workflow or team processes",
      "D - Conducting deep scientific research",
      "E - Learning sports techniques or rules",
      "F - Teaching others what I learn"
    ]
  },

  // 7
  {
    question: "I am interested in scientific experiments.",
    options: [
      "A - Running technical experiments with devices",
      "B - Experimenting with creative materials",
      "C - Organizing experiment tasks or teams",
      "D - Performing scientific lab experiments",
      "E - Testing new sports techniques or drills",
      "F - Assisting others in learning experiments"
    ]
  },

  // 8
  {
    question: "I love exploring and discovering new information.",
    options: [
      "A - Exploring new technologies or software",
      "B - Discovering new creative ideas",
      "C - Learning new leadership or management methods",
      "D - Exploring research papers or data",
      "E - Learning new sports moves or strategies",
      "F - Sharing new knowledge with others"
    ]
  },

  // 9
  {
    question: "I enjoy creating art, design, or music.",
    options: [
      "A - Creating technical digital designs",
      "B - Making artistic or musical work",
      "C - Organizing creative projects",
      "D - Studying the science behind art or sound",
      "E - Performing rhythmic or artistic sports",
      "F - Helping others express creativity"
    ]
  },

  // 10
  {
    question: "I like expressing myself in unique or imaginative ways.",
    options: [
      "A - Expressing through tech projects",
      "B - Expressing through creative art or ideas",
      "C - Presenting ideas confidently as a leader",
      "D - Expressing through academic findings",
      "E - Expressing through movement or sports",
      "F - Expressing through social interactions"
    ]
  },

  // 11
  {
    question: "I prefer flexible work that lets me be creative.",
    options: [
      "A - Working flexibly on tech experiments",
      "B - Creating freely in design or art",
      "C - Managing tasks with flexible leadership styles",
      "D - Exploring flexible research directions",
      "E - Practicing sports with flexible routines",
      "F - Helping people in flexible learning environments"
    ]
  },

  // 12
  {
    question: "I’d rather create something new than follow strict rules.",
    options: [
      "A - Creating innovative tech solutions",
      "B - Creating original creative work",
      "C - Innovating new management approaches",
      "D - Proposing new research ideas",
      "E - Innovating new sports moves or training styles",
      "F - Creating new ways to support others socially"
    ]
  },

  // 13
  {
    question: "I find joy in helping others learn or grow.",
    options: [
      "A - Helping others learn technical skills",
      "B - Teaching someone creative skills",
      "C - Guiding teams to improve performance",
      "D - Helping others understand research topics",
      "E - Coaching teammates in sports",
      "F - Supporting people emotionally or socially"
    ]
  },

  // 14
  {
    question: "I enjoy teaching, mentoring, or volunteering.",
    options: [
      "A - Mentoring in technology or coding",
      "B - Mentoring in art, design, or creativity",
      "C - Leading and coaching teams",
      "D - Teaching research or science topics",
      "E - Coaching sports or fitness activities",
      "F - Volunteering to help communities"
    ]
  },

  // 15
  {
    question: "I’m comfortable working directly with people every day.",
    options: [
      "A - Explaining technical tasks to people",
      "B - Collaborating on creative projects",
      "C - Managing or leading teams daily",
      "D - Discussing research insights with others",
      "E - Working closely with teammates in sports",
      "F - Interacting socially and helping people"
    ]
  },

  // 16
  {
    question: "Helping people succeed gives me energy.",
    options: [
      "A - Helping people solve technical issues",
      "B - Encouraging creative confidence",
      "C - Supporting people through management",
      "D - Helping others succeed in research",
      "E - Helping teammates improve in sports",
      "F - Motivating or supporting others emotionally"
    ]
  },

  // 17
  {
    question: "I enjoy leading groups or organizing projects.",
    options: [
      "A - Leading tech-based projects",
      "B - Leading creative teams",
      "C - Managing full team operations",
      "D - Leading research groups",
      "E - Leading sports teams or events",
      "F - Leading community or social groups"
    ]
  },

  // 18
  {
    question: "I like convincing others or promoting ideas.",
    options: [
      "A - Promoting new technology ideas",
      "B - Pitching creative concepts",
      "C - Presenting business or project ideas",
      "D - Presenting research theories",
      "E - Motivating teammates to adopt strategies",
      "F - Persuading or inspiring people socially"
    ]
  },

  // 19
  {
    question: "I would enjoy starting or running a business.",
    options: [
      "A - A tech-based startup",
      "B - A creative studio or brand",
      "C - A business or management firm",
      "D - A research or analysis company",
      "E - A sports academy or fitness center",
      "F - A social-service or community organization"
    ]
  },

  // 20
  {
    question: "I prefer taking charge rather than following orders.",
    options: [
      "A - Leading technical decisions",
      "B - Leading creative direction",
      "C - Taking charge as a manager",
      "D - Directing research activities",
      "E - Leading sports strategies",
      "F - Taking charge of group activities socially"
    ]
  },

  // 21
  {
    question: "I prefer clear plans and structured environments.",
    options: [
      "A - Structured technical workflows",
      "B - Structured creative planning",
      "C - Planning structured team operations",
      "D - Structured research documentation",
      "E - Structured sports practice routines",
      "F - Structured teamwork with people"
    ]
  },

  // 22
  {
    question: "I like managing details and keeping things organized.",
    options: [
      "A - Managing technical system details",
      "B - Organizing creative materials",
      "C - Handling team or project details",
      "D - Keeping research data organized",
      "E - Organizing sports schedules or drills",
      "F - Organizing group activities for people"
    ]
  },

  // 23
  {
    question: "I’m good with data, schedules, or documentation.",
    options: [
      "A - Handling tech data or logs",
      "B - Creating visually creative documentation",
      "C - Managing team schedules and records",
      "D - Recording and analyzing research data",
      "E - Tracking sports stats or training logs",
      "F - Maintaining social or community records"
    ]
  },

  // 24
  {
    question: "I like consistency and predictable tasks.",
    options: [
      "A - Performing consistent technical routines",
      "B - Maintaining a consistent creative process",
      "C - Following consistent management workflows",
      "D - Running consistent research procedures",
      "E - Following consistent sports training",
      "F - Doing consistent community or social tasks"
    ]
  },

  // 25
  {
    question: "I follow instructions carefully to complete tasks accurately.",
    options: [
      "A - Technical accuracy",
      "B - Creative tasks accuracy",
      "C - Management accuracy",
      "D - Research accuracy",
      "E - Sports drills accuracy",
      "F - Social task accuracy"
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




const handleSubmit = async () => {
  try {
    const answerLabels = answers.map((idx) => String.fromCharCode(65 + idx));

    const payload = {
      answers: Object.fromEntries(
        answerLabels.map((letter, index) => [`Q${index + 1}`, letter])
      ),
      free_text: "",
    };

    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const result = await response.json();
      console.log("API Result:", result);


    navigate("/results", { state: { predictions: result } });
  } catch (error) {
    console.error("Quiz submit error:", error);
  }

};






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
    className="min-h-screen flex flex-col items-center bg-gray-50 py-4"
    initial={{ y: 50, opacity: 0 }}
    animate={{ y: 0, opacity: 1 }}
    exit={{ y: -50, opacity: 0 }}
    transition={{ type: "tween", ease: "easeOut", duration: 0.5 }}
  >
    <div className="flex flex-col items-center bg-gray-50 py-4 w-full">

      {/* Header */}
      <div className="flex items-center justify-between w-full max-w-3xl mb-4">
        <div
          onClick={handleBackToHome}
          role="button"
          tabIndex={0}
          onKeyPress={(e) => { if (e.key === 'Enter') handleBackToHome(); }}
          className="cursor-pointer text-gray-700 hover:bg-green-400 hover:text-white px-4 py-1 rounded-lg font-semibold shadow transition-colors flex items-center text-sm"
        >
          <span className="mr-2">&larr;</span> Back to Home
        </div>

        <div className="flex-1 mx-4">
          <div className="relative w-full h-1.5 rounded bg-gray-200">
            <div
              className="absolute h-1.5 rounded bg-gradient-to-r from-blue-500 to-purple-600"
              style={{
                width: `${((step + 1) / questions.length) * 100}%`,
                transition: "width 0.3s",
              }}
            ></div>
          </div>
          <div className="text-center text-gray-500 mt-1 text-sm">
            {`${Math.round(((step + 1) / questions.length) * 100)}% Complete`}
          </div>
        </div>

        <div className="text-gray-600 font-medium text-sm">
          {`Q ${step + 1} / ${questions.length}`}
        </div>
      </div>

      {/* Card */}
      <div className="w-full max-w-3xl bg-white shadow-md rounded-xl p-5">

        <h2 className="text-2xl font-bold mb-5">
          {questions[step].question}
        </h2>

        <div className="flex flex-col gap-4 mb-6">
          {questions[step].options.map((opt, idx) => (
            <button
              key={opt}
              onClick={() => handleOptionClick(idx)}
              className={`text-base border rounded-lg px-5 py-3 text-left transition-all ${
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
            className="px-4 py-2 rounded bg-gray-200 text-gray-600 text-sm"
          >
            Previous
          </button>

          {step === questions.length - 1 ? (
            <button
              onClick={handleSubmit}
              className="px-5 py-2 rounded bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold text-sm"
            >
              Submit
            </button>
          ) : (
            <button
              disabled={answers[step] === undefined}
              onClick={handleNext}
              className="px-5 py-2 rounded bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold text-sm"
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


