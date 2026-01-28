# career_data.py
CAREER_ALIASES = {
    "cricketer": "sportsperson",
    "footballer": "sportsperson",
    "athlete": "sportsperson",
    "ui designer": "ui ux designer",
    "ux designer": "ui ux designer",
    "app designer": "ui ux designer",
    "apps designing": "ui ux designer"
}

CAREER_INFO = {

# ======================= STAGE 1 : AVIATION, HEALTHCARE, ENGINEERING, IT, MEDIA =======================

# -------- Aviation & Travel --------

"commercial pilot": {
    "domain": "Aviation & Travel",
    "tags": ["flying", "aircraft", "travel", "aviation"],
    "description": [
        "Fly commercial aircraft on domestic and international routes",
        "Ensure passenger safety and operational efficiency"
    ],
    "skills": ["Decision making", "Situational awareness", "Aircraft systems", "Communication"],
    "education": ["Commercial Pilot License (CPL)", "DGCA/FAA medical clearance"],
    "growth": "First Officer → Captain → Training Captain → Fleet Manager",
    "estimated_budget": "₹45–70 lakhs (flight training + license)",
    "estimated_salary": "₹1.5–3 LPM (First Officer) → ₹6–10 LPM (Captain)",
    "entrance_exams_required": ["DGCA CPL exams", "Class 1 Medical", "Airline selection tests"],
    "link": "https://www.iata.org/en/careers/",
    "related_careers": ["air traffic controller", "flight dispatcher", "airport operations manager"]
},

"cabin crew": {
    "domain": "Aviation & Travel",
    "tags": ["airlines", "travel", "customer service"],
    "description": [
        "Ensure passenger safety and comfort",
        "Handle in-flight emergencies"
    ],
    "skills": ["Communication", "Emergency handling", "Customer service"],
    "education": ["Cabin crew certification"],
    "growth": "Cabin Crew → Lead Crew → In-flight Manager",
    "estimated_budget": "₹50k–2 lakhs (training & grooming)",
    "estimated_salary": "₹40k–80k/month → ₹1.5 LPM (Senior crew)",
    "entrance_exams_required": ["Airline walk-in interviews", "Medical & grooming checks"],
    "link": "https://www.iata.org/en/careers/",
    "related_careers": ["commercial pilot", "flight dispatcher", "air traffic controller"]
},

"air traffic controller": {
    "domain": "Aviation & Travel",
    "tags": ["aviation", "control", "radar"],
    "description": [
        "Manage aircraft movement",
        "Ensure safe takeoff and landing"
    ],
    "skills": ["Concentration", "Decision making", "Stress management"],
    "education": ["ATC training", "Aviation degree/diploma"],
    "growth": "ATC → Senior ATC → Supervisor → Chief Controller",
    "estimated_budget": "₹1–3 lakhs (training, mostly govt-sponsored)",
    "estimated_salary": "₹60k–1.2 LPM → ₹2.5+ LPM (senior roles)",
    "entrance_exams_required": ["AAI ATC exam", "Medical fitness test"],
    "link": "https://www.faa.gov/jobs/career_fields/atc",
    "related_careers": ["commercial pilot", "cabin crew", "flight dispatcher"]
},

"aircraft maintenance engineer": {
    "domain": "Aviation & Travel",
    "tags": ["engineering", "aircraft", "maintenance"],
    "description": [
        "Inspect and repair aircraft",
        "Ensure safety compliance"
    ],
    "skills": ["Mechanical skills", "Troubleshooting", "Attention to detail"],
    "education": ["AME license", "Aeronautical/Mechanical Engineering"],
    "growth": "AME → Senior AME → Maintenance Manager",
    "estimated_budget": "₹5–10 lakhs (AME training)",
    "estimated_salary": "₹50k–1 LPM → ₹3 LPM (experienced)",
    "entrance_exams_required": ["AME CET", "DGCA module exams"],
    "link": "https://www.skybrary.aero/index.php/Aircraft_Maintenance_Engineering",
    "related_careers": ["mechanical engineer", "aerospace engineer", "aviation engineer"]
},

"airport operations manager": {
    "domain": "Aviation & Travel",
    "tags": ["airport", "operations", "management"],
    "description": [
        "Manage airport daily operations",
        "Coordinate security and logistics"
    ],
    "skills": ["Operations management", "Leadership"],
    "education": ["Aviation management degree"],
    "growth": "Operations Officer → Manager → Airport Director",
    "estimated_budget": "₹3–6 lakhs (degree/diploma)",
    "estimated_salary": "₹60k–1.5 LPM → ₹4+ LPM",
    "entrance_exams_required": ["University entrance exams", "Airport authority interviews"],
    "link": "https://www.aci.aero/careers/",
    "related_careers": ["commercial pilot", "flight dispatcher", "air traffic controller"]
},

"flight dispatcher": {
    "domain": "Aviation & Travel",
    "tags": ["flight planning", "aviation"],
    "description": [
        "Plan flight routes",
        "Monitor weather and fuel"
    ],
    "skills": ["Navigation", "Weather analysis"],
    "education": ["Dispatcher license"],
    "growth": "Dispatcher → Senior Dispatcher → Operations Head",
    "estimated_budget": "₹2–4 lakhs (dispatcher course)",
    "estimated_salary": "₹40k–90k/month → ₹2 LPM",
    "entrance_exams_required": ["DGCA Flight Dispatcher exams"],
    "link": "https://www.iata.org/en/careers/",
    "related_careers": ["air traffic controller", "commercial pilot", "airport operations manager"]
},

# -------- Healthcare & Emergency --------

"doctor": {
    "domain": "Healthcare & Emergency Services",
    "tags": ["medical", "healthcare"],
    "description": [
        "Diagnose and treat illnesses",
        "Prescribe medications"
    ],
    "skills": ["Medical expertise", "Empathy", "Diagnosis"],
    "education": ["MBBS", "Specialization"],
    "growth": "Junior Doctor → Specialist → Consultant",
    "estimated_budget": "₹8–25 lakhs (MBBS + specialization)",
    "estimated_salary": "₹60k–1.5 LPM → ₹5+ LPM",
    "entrance_exams_required": ["NEET-UG", "NEET-PG"],
    "link": "https://www.who.int/careers",
    "related_careers": ["nurse", "radiologist", "paramedic"]
},

"nurse": {
    "domain": "Healthcare & Emergency Services",
    "tags": ["patient care", "hospital"],
    "description": [
        "Care for patients",
        "Assist doctors"
    ],
    "skills": ["Patient care", "Communication"],
    "education": ["BSc Nursing / GNM"],
    "growth": "Staff Nurse → Head Nurse → Nursing Superintendent",
    "estimated_budget": "₹2–6 lakhs",
    "estimated_salary": "₹25k–60k/month → ₹1.2 LPM",
    "entrance_exams_required": ["Nursing entrance exams"],
    "link": "https://www.icn.ch/what-we-do/careers",
    "related_careers": ["doctor", "paramedic", "wardboy"]
},

"wardboy": {
    "domain": "Healthcare & Emergency Services",
    "tags": ["hospital support", "patient care"],
    "description": [
        "Assist patients and medical staff",
        "Transport patients"
    ],
    "skills": ["Physical stamina", "Compassion"],
    "education": ["Hospital training"],
    "growth": "Ward Assistant → Senior Ward Assistant",
    "estimated_budget": "₹10k–50k (training)",
    "estimated_salary": "₹12k–25k/month",
    "entrance_exams_required": ["Hospital-level interview"],
    "link": "https://www.nhp.gov.in/",
    "related_careers": ["nurse", "doctor", "paramedic"]
},

"pharmacist": {
    "domain": "Healthcare & Emergency Services",
    "tags": ["medicine", "pharmacy"],
    "description": [
        "Dispense medications",
        "Advise patients"
    ],
    "skills": ["Drug knowledge", "Accuracy"],
    "education": ["B.Pharm / D.Pharm"],
    "growth": "Pharmacist → Clinical Pharmacist → Pharmacy Manager",
    "estimated_budget": "₹3–8 lakhs",
    "estimated_salary": "₹25k–80k/month → ₹2 LPM",
    "entrance_exams_required": ["Pharmacy entrance exams", "State registration"],
    "link": "https://www.fip.org/pharmacy-education",
    "related_careers": ["doctor", "nurse", "biomedical engineer"]
},

"paramedic": {
    "domain": "Healthcare & Emergency Services",
    "tags": ["emergency", "ambulance"],
    "description": [
        "Provide emergency care",
        "Stabilize patients"
    ],
    "skills": ["Quick decisions", "Emergency care"],
    "education": ["Paramedical diploma"],
    "growth": "EMT → Paramedic → Supervisor",
    "estimated_budget": "₹50k–3 lakhs",
    "estimated_salary": "₹20k–50k/month → ₹1 LPM",
    "entrance_exams_required": ["Institute-level entrance tests"],
    "link": "https://www.nremt.org/",
    "related_careers": ["doctor", "nurse", "wardboy"]
},

"radiologist": {
    "domain": "Healthcare & Emergency Services",
    "tags": ["imaging", "diagnosis"],
    "description": [
        "Interpret medical scans",
        "Assist diagnosis"
    ],
    "skills": ["Imaging analysis", "Attention"],
    "education": ["MBBS + MD Radiology"],
    "growth": "Radiologist → Senior Radiologist → HOD",
    "estimated_budget": "₹15–30 lakhs",
    "estimated_salary": "₹1.5–4 LPM → ₹8+ LPM",
    "entrance_exams_required": ["NEET-UG", "NEET-PG"],
    "link": "https://www.radiologyinfo.org/en/info.cfm",
    "related_careers": ["doctor", "biomedical engineer", "nurse"]
},

"physiotherapist": {
    "domain": "Health & Medicine",
    "tags": ["physiotherapy", "rehabilitation", "healthcare", "patient care"],
    "description": [
        "Treat patients with physical injuries",
        "Develop rehabilitation plans"
    ],
    "skills": [
        "Anatomy knowledge",
        "Manual therapy",
        "Patient assessment"
    ],
    "education": [
        "BPT / MPT (Physiotherapy courses)"
    ],
    "growth": "Junior Physiotherapist → Senior Physiotherapist → Rehab Specialist",
    "estimated_budget": "₹3–7 lakhs",
    "estimated_salary": "₹25k–70k/month → ₹2 LPM",
    "entrance_exams_required": [
        "NEET-UG",
        "AIIMS BPT Entrance",
        "PGIMER Chandigarh BPT Entrance",
        "JIPMER BPT Entrance",
        "State-level BPT Entrance Exams (Maharashtra CET, Karnataka CET, etc.)"
    ],
    "link": "https://www.careersinhealthcare.com/",
    "related_careers": ["occupational therapist", "sports therapist", "chiropractor"]
},

# -------- Engineering --------

"mechanical engineer": {
    "domain": "Engineering",
    "tags": ["machines", "design"],
    "description": ["Design mechanical systems"],
    "skills": ["CAD", "Thermodynamics"],
    "education": ["B.Tech Mechanical"],
    "growth": "Engineer → Senior Engineer → Manager",
    "estimated_budget": "₹4–10 lakhs",
    "estimated_salary": "₹30k–80k/month → ₹4 LPM",
    "entrance_exams_required": ["JEE Main", "State CET", "Institute exams"],
    "link": "https://www.engineering.com/careers",
    "related_careers": ["civil engineer", "robotics engineer", "aerospace engineer"]
},

"civil engineer": {
    "domain": "Engineering",
    "tags": ["construction", "infrastructure"],
    "description": ["Design structures"],
    "skills": ["Structural analysis"],
    "education": ["B.Tech Civil"],
    "growth": "Site Engineer → Project Manager",
    "estimated_budget": "₹4–10 lakhs",
    "estimated_salary": "₹30k–90k/month → ₹5 LPM",
    "entrance_exams_required": ["JEE Main", "State CET"],
    "link": "https://www.asce.org/career",
    "related_careers": ["mechanical engineer", "structural engineer", "architect"]
},

"electrical engineer": {
    "domain": "Engineering",
    "tags": ["circuits", "power"],
    "description": ["Design electrical systems"],
    "skills": ["Circuit design"],
    "education": ["B.Tech Electrical"],
    "growth": "Engineer → Lead Engineer",
    "estimated_budget": "₹4–10 lakhs",
    "estimated_salary": "₹35k–1 LPM → ₹5+ LPM",
    "entrance_exams_required": ["JEE Main", "State CET"],
    "link": "https://www.ieee.org/careers/index.html",
    "related_careers": ["electronics engineer", "robotics engineer", "automation engineer"]
},

"chemical engineer": {
    "domain": "Engineering",
    "tags": ["chemicals", "process"],
    "description": ["Design chemical processes"],
    "skills": ["Process control"],
    "education": ["B.Tech Chemical"],
    "growth": "Engineer → Plant Manager",
    "estimated_budget": "₹4–10 lakhs",
    "estimated_salary": "₹40k–1 LPM → ₹6+ LPM",
    "entrance_exams_required": ["JEE Main", "State CET"],
    "link": "https://www.aiche.org/",
    "related_careers": ["biochemical engineer", "process engineer", "petroleum engineer"]
},

"aerospace engineer": {
    "domain": "Engineering",
    "tags": ["aircraft", "space"],
    "description": ["Design aircraft and spacecraft"],
    "skills": ["Aerodynamics"],
    "education": ["B.Tech Aerospace"],
    "growth": "Engineer → Scientist",
    "estimated_budget": "₹6–15 lakhs",
    "estimated_salary": "₹50k–2 LPM → ₹8+ LPM",
    "entrance_exams_required": ["JEE Advanced", "GATE"],
    "link": "https://www.aiaa.org/",
    "related_careers": ["mechanical engineer", "robotics engineer", "aeronautical engineer"]
},

"biomedical engineer": {
    "domain": "Engineering",
    "tags": ["medical devices"],
    "description": ["Develop medical equipment"],
    "skills": ["Electronics", "Biology"],
    "education": ["Biomedical Engineering"],
    "growth": "Engineer → R&D Lead",
    "estimated_budget": "₹4–10 lakhs",
    "estimated_salary": "₹40k–1.2 LPM → ₹5 LPM",
    "entrance_exams_required": ["JEE Main", "Institute exams"],
    "link": "https://www.bmes.org/",
    "related_careers": ["pharmacist", "mechanical engineer", "robotics engineer"]
},

"structural engineer": {
    "domain": "Engineering",
    "tags": ["structures", "buildings", "construction"],
    "description": [
        "Design safe and durable structures",
        "Analyze loads and materials"
    ],
    "skills": ["Structural analysis", "AutoCAD", "Problem-solving"],
    "education": ["B.Tech Civil / Structural Engineering"],
    "growth": "Engineer → Senior Engineer → Structural Consultant",
    "estimated_budget": "₹4–10 lakhs",
    "estimated_salary": "₹40k–1.5 LPM → ₹6+ LPM",
    "entrance_exams_required": ["JEE Main", "State CET", "GATE (for M.Tech)"],
    "link": "https://www.asce.org/",
    "related_careers": ["civil engineer", "construction manager"]
},

"mechatronics engineer": {
    "domain": "Engineering",
    "tags": ["mechanical", "electronics", "automation"],
    "description": [
        "Design smart mechanical systems",
        "Integrate electronics and control systems"
    ],
    "skills": ["Embedded systems", "Control systems", "Programming"],
    "education": ["B.Tech Mechatronics"],
    "growth": "Engineer → Senior Engineer → Automation Architect",
    "estimated_budget": "₹5–12 lakhs",
    "estimated_salary": "₹45k–1.5 LPM → ₹6+ LPM",
    "entrance_exams_required": ["JEE Main", "Institute exams"],
    "link": "https://www.asme.org/",
    "related_careers": ["robotics engineer", "automation engineer"]
},

"automation engineer": {
    "domain": "Engineering",
    "tags": ["automation", "plc", "industrial"],
    "description": [
        "Automate industrial processes",
        "Maintain control systems"
    ],
    "skills": ["PLC", "SCADA", "Industrial systems"],
    "education": ["Electrical / Mechatronics Engineering"],
    "growth": "Engineer → Senior Engineer → Automation Manager",
    "estimated_budget": "₹4–10 lakhs",
    "estimated_salary": "₹45k–1.8 LPM → ₹7+ LPM",
    "entrance_exams_required": ["JEE Main", "State CET"],
    "link": "https://www.ieee.org/",
    "related_careers": ["electrical engineer", "robotics engineer"]
},

"manufacturing engineer": {
    "domain": "Engineering",
    "tags": ["manufacturing", "production", "factory"],
    "description": [
        "Optimize manufacturing processes",
        "Improve production efficiency"
    ],
    "skills": ["Lean manufacturing", "Process optimization"],
    "education": ["Mechanical / Production Engineering"],
    "growth": "Engineer → Plant Engineer → Operations Manager",
    "estimated_budget": "₹4–10 lakhs",
    "estimated_salary": "₹35k–1.2 LPM → ₹6+ LPM",
    "entrance_exams_required": ["JEE Main", "State CET"],
    "link": "https://www.sme.org/",
    "related_careers": ["industrial engineer", "quality engineer"]
},

"quality engineer": {
    "domain": "Engineering",
    "tags": ["quality", "testing", "manufacturing"],
    "description": [
        "Ensure product quality standards",
        "Perform inspections and audits"
    ],
    "skills": ["Quality control", "Six Sigma"],
    "education": ["Engineering degree"],
    "growth": "Engineer → Quality Lead → QA Manager",
    "estimated_budget": "₹4–8 lakhs",
    "estimated_salary": "₹30k–1 LPM → ₹5+ LPM",
    "entrance_exams_required": ["JEE Main", "Institute exams"],
    "link": "https://asq.org/",
    "related_careers": ["manufacturing engineer", "process engineer"]
},

# -------- IT & Data --------

"software engineer": {
    "domain": "IT & Data",
    "tags": ["coding", "software"],
    "description": ["Develop software applications"],
    "skills": ["Programming", "Debugging", "Problem-solving"],
    "education": ["CS degree / Software Engineering"],
    "growth": "Developer → Tech Lead → Software Architect",
    "estimated_budget": "₹0–8 lakhs",
    "estimated_salary": "₹40k–2 LPM → ₹10+ LPM",
    "entrance_exams_required": ["Coding tests", "Technical interviews"],
    "link": "https://www.computercareers.org/",
    "related_careers": ["data scientist", "ai engineer", "cloud engineer"]
},

"data analyst": {
    "domain": "IT & Data",
    "tags": ["data", "analytics"],
    "description": ["Analyze datasets to extract insights"],
    "skills": ["SQL", "Python", "Data Visualization","Statistical analysis"],
    "education": ["Data Science / Analytics courses"],
    "growth": "Analyst → Senior Analyst → Data Scientist",
    "estimated_budget": "₹50k–5 lakhs",
    "estimated_salary": "₹35k–1 LPM → ₹4 LPM",
    "entrance_exams_required": ["Company interviews", "Analytics tests"],
    "link": "https://www.datacareer.io/",
    "related_careers": ["data scientist", "business analyst", "software engineer"]
},

"data scientist": {
    "domain": "IT & Data",
    "tags": ["ML", "AI", "statistics"],
    "description": ["Build predictive and ML models"],
    "skills": ["Python", "Machine Learning", "Statistics"],
    "education": ["CS / Data Science"],
    "growth": "Scientist → Lead Scientist → AI Architect",
    "estimated_budget": "₹1–10 lakhs",
    "estimated_salary": "₹70k–3 LPM → ₹15+ LPM",
    "entrance_exams_required": ["ML interviews", "Statistics tests"],
    "link": "https://www.kaggle.com/careers",
    "related_careers": ["ai engineer", "data analyst", "software engineer"]
},

"cybersecurity analyst": {
    "domain": "IT & Data",
    "tags": ["security", "networking"],
    "description": ["Protect systems and data from attacks"],
    "skills": ["Networking", "Ethical hacking", "Monitoring"],
    "education": ["Cybersecurity courses / degree"],
    "growth": "Analyst → Security Lead → CISO",
    "estimated_budget": "₹50k–6 lakhs",
    "estimated_salary": "₹45k–1.5 LPM → ₹6+ LPM",
    "entrance_exams_required": ["Security interviews", "Certifications (CEH, Security+)"],
    "link": "https://www.cyberseek.org/",
    "related_careers": ["network engineer", "data analyst", "ai engineer"]
},

"cloud engineer": {
    "domain": "IT & Data",
    "tags": ["cloud", "AWS", "Azure"],
    "description": ["Manage cloud infrastructure and services"],
    "skills": ["AWS/Azure/GCP", "Automation", "Monitoring"],
    "education": ["Cloud certifications"],
    "growth": "Engineer → Senior Engineer → Cloud Architect",
    "estimated_budget": "₹50k–5 lakhs",
    "estimated_salary": "₹60k–2 LPM → ₹8+ LPM",
    "entrance_exams_required": ["Cloud certification exams", "Technical interviews"],
    "link": "https://aws.amazon.com/careers/",
    "related_careers": ["software engineer", "data scientist", "ai engineer"]
},

"web developer": {
    "domain": "IT & Data",
    "tags": ["web", "frontend", "backend"],
    "description": [
        "Develop websites and web applications",
        "Maintain frontend and backend logic"
    ],
    "skills": ["HTML", "CSS", "JavaScript", "Backend frameworks"],
    "education": ["CS / Web development courses"],
    "growth": "Junior Developer → Full Stack Developer → Tech Lead",
    "estimated_budget": "₹0–3 lakhs",
    "estimated_salary": "₹25k–1 LPM → ₹4 LPM",
    "entrance_exams_required": ["Portfolio review", "Coding tests"],
    "link": "https://developer.mozilla.org/",
    "related_careers": ["software engineer", "ui ux designer"]
},

"full stack developer": {
    "domain": "IT & Data",
    "tags": ["frontend", "backend", "databases"],
    "description": [
        "Work on both client and server side",
        "Build end-to-end applications"
    ],
    "skills": ["React", "Node.js", "Databases"],
    "education": ["Computer Science / Bootcamps"],
    "growth": "Developer → Senior Developer → Architect",
    "estimated_budget": "₹50k–6 lakhs",
    "estimated_salary": "₹50k–2 LPM → ₹8+ LPM",
    "entrance_exams_required": ["Coding interviews", "System design rounds"],
    "link": "https://www.freecodecamp.org/",
    "related_careers": ["software engineer", "cloud engineer"]
},

"machine learning engineer": {
    "domain": "IT & Data",
    "tags": ["ml", "models", "ai"],
    "description": [
        "Deploy machine learning models",
        "Optimize model performance"
    ],
    "skills": ["Python", "ML algorithms", "MLOps"],
    "education": ["CS / AI / Data Science"],
    "growth": "ML Engineer → Senior ML Engineer → AI Architect",
    "estimated_budget": "₹1–8 lakhs",
    "estimated_salary": "₹70k–2.5 LPM → ₹12+ LPM",
    "entrance_exams_required": ["ML coding interviews", "Math & stats tests"],
    "link": "https://developers.google.com/machine-learning",
    "related_careers": ["data scientist", "ai engineer"]
},

"nlp engineer": {
    "domain": "IT & Data",
    "tags": ["nlp", "language", "ai"],
    "description": [
        "Build language-based AI systems",
        "Work on chatbots and text analytics"
    ],
    "skills": ["NLP", "Transformers", "Python"],
    "education": ["AI / ML specialization"],
    "growth": "Engineer → Senior NLP Engineer → Research Scientist",
    "estimated_budget": "₹1–8 lakhs",
    "estimated_salary": "₹80k–3 LPM → ₹15+ LPM",
    "entrance_exams_required": ["ML interviews", "NLP project evaluation"],
    "link": "https://huggingface.co/",
    "related_careers": ["ai engineer", "ml engineer"]
},

"computer vision engineer": {
    "domain": "IT & Data",
    "tags": ["vision", "image", "ai"],
    "description": [
        "Develop image and video analysis systems",
        "Apply deep learning to visual data"
    ],
    "skills": ["OpenCV", "Deep learning", "Python"],
    "education": ["AI / Computer Science"],
    "growth": "Engineer → Senior Engineer → Vision Architect",
    "estimated_budget": "₹1–8 lakhs",
    "estimated_salary": "₹70k–3 LPM → ₹12+ LPM",
    "entrance_exams_required": ["CV project review", "ML interviews"],
    "link": "https://opencv.org/",
    "related_careers": ["ai engineer", "robotics engineer"]
},

"data engineer": {
    "domain": "IT & Data",
    "tags": ["data pipelines", "big data"],
    "description": [
        "Build and maintain data pipelines",
        "Ensure data availability and reliability"
    ],
    "skills": ["SQL", "Spark", "ETL"],
    "education": ["CS / Data Engineering"],
    "growth": "Engineer → Senior Engineer → Data Architect",
    "estimated_budget": "₹50k–6 lakhs",
    "estimated_salary": "₹60k–2 LPM → ₹9+ LPM",
    "entrance_exams_required": ["SQL & ETL interviews"],
    "link": "https://databricks.com/",
    "related_careers": ["data scientist", "cloud engineer"]
},

"business analyst": {
    "domain": "IT & Data",
    "tags": ["business", "analysis", "requirements"],
    "description": [
        "Analyze business needs",
        "Bridge technical and business teams"
    ],
    "skills": ["Requirement analysis", "Communication"],
    "education": ["Business / IT degree"],
    "growth": "Analyst → Senior Analyst → Product Manager",
    "estimated_budget": "₹50k–4 lakhs",
    "estimated_salary": "₹40k–1.2 LPM → ₹5 LPM",
    "entrance_exams_required": ["Case interviews", "Business analysis tests"],
    "link": "https://www.iiba.org/",
    "related_careers": ["product manager", "data analyst"]
},

"devops engineer": {
    "domain": "IT & Data",
    "tags": ["devops", "ci cd", "automation"],
    "description": [
        "Automate deployments and infrastructure",
        "Ensure system reliability"
    ],
    "skills": ["Docker", "Kubernetes", "CI/CD"],
    "education": ["CS / Cloud certifications"],
    "growth": "Engineer → Senior Engineer → DevOps Architect",
    "estimated_budget": "₹50k–6 lakhs",
    "estimated_salary": "₹70k–2.5 LPM → ₹10+ LPM",
    "entrance_exams_required": ["DevOps interviews", "System design rounds"],
    "link": "https://aws.amazon.com/devops/",
    "related_careers": ["cloud engineer", "site reliability engineer"]
},

"site reliability engineer": {
    "domain": "IT & Data",
    "tags": ["sre", "systems", "reliability"],
    "description": [
        "Maintain high system availability",
        "Monitor and improve performance"
    ],
    "skills": ["Linux", "Monitoring", "Automation"],
    "education": ["Computer Science"],
    "growth": "SRE → Senior SRE → Infrastructure Lead",
    "estimated_budget": "₹50k–6 lakhs",
    "estimated_salary": "₹80k–3 LPM → ₹12+ LPM",
    "entrance_exams_required": ["Linux & systems interviews"],
    "link": "https://sre.google/",
    "related_careers": ["devops engineer", "cloud engineer"]
},

# -------- Media & Entertainment --------

"actor": {
    "domain": "Media & Entertainment",
    "tags": ["acting", "performance"],
    "description": [
        "Perform roles in TV, films, theater",
        "Portray characters through expressions and dialogue"
    ],
    "skills": ["Expression", "Voice modulation", "Acting skills", "Confidence"],
    "education": ["Acting school / Drama courses (optional)"],
    "growth": "Theatre Actor → Supporting Roles → Lead Actor → Celebrity",
    "estimated_budget": "₹50,000 – ₹5,00,000 (acting classes, auditions, portfolio)",
    "estimated_salary": "₹0–₹30,000/month (initial) → ₹5L–₹5Cr per project",
    "entrance_exams_required": ["No formal exams", "Auditions", "Screen tests"],
    "link": "https://www.backstage.com/casting/",
    "related_careers": ["film director", "producer", "cinematographer"]
},

"film director": {
    "domain": "Media & Entertainment",
    "tags": ["direction", "film", "storytelling","leadership", "vision", "directing actors", "creative control", "film production"],
    "description": [
        "Direct films and visual narratives",
        "Guide actors and technical crew"
    ],
    "skills": ["Leadership", "Storytelling", "Creative vision"],
    "education": ["Film studies / Media courses"],
    "growth": "Assistant Director → Director → Senior Director → Producer",
    "estimated_budget": "₹2L – ₹10L (film school, short films, equipment)",
    "estimated_salary": "₹30,000/month → ₹50L+ per film",
    "entrance_exams_required": ["FTII JET", "SRFTI Entrance", "Private film school tests"],
    "link": "https://www.sundance.org/careers",
    "related_careers": ["producer", "cinematographer", "video editor"]
},

"producer": {
    "domain": "Media & Entertainment",
    "tags": ["budget", "management", "film"],
    "description": [
        "Manage film budgets and schedules",
        "Oversee production from concept to release"
    ],
    "skills": ["Budgeting", "Planning", "Negotiation", "Team management"],
    "education": ["Media / Film Management"],
    "growth": "Line Producer → Producer → Executive Producer → Studio Head",
    "estimated_budget": "₹3L – ₹15L (education + initial projects)",
    "estimated_salary": "₹40,000/month → Profit-based / ₹1Cr+ per project",
    "entrance_exams_required": ["FTII", "SRFTI", "Media school entrances"],
    "link": "https://www.shootonline.com/",
    "related_careers": ["film director", "cinematographer", "video editor"]
},

"cinematographer": {
    "domain": "Media & Entertainment",
    "tags": ["camera operator", "lighting", "lenses", "cinematography", "visual storytelling", "behind the lens"],
    "description": [
        "Handle camera work and visual composition",
        "Design lighting and shot aesthetics"
    ],
    "skills": ["Lighting", "Camera operation", "Visual storytelling"],
    "education": ["Film school / Cinematography courses"],
    "growth": "Camera Assistant → Cinematographer → Director of Photography",
    "estimated_budget": "₹2L – ₹12L (courses + camera gear)",
    "estimated_salary": "₹25,000/month → ₹20L–₹1Cr per film",
    "entrance_exams_required": ["FTII", "SRFTI", "Film institute exams"],
    "link": "https://www.cinematography.com/",
    "related_careers": ["film director", "producer", "video editor"]
},

"video editor": {
    "domain": "Media & Entertainment",
    "tags": ["editing", "post-production"],
    "description": [
        "Edit raw footage into final videos",
        "Add effects, sound, and transitions"
    ],
    "skills": ["Premiere Pro", "After Effects", "Storytelling"],
    "education": ["Editing courses / Media studies"],
    "growth": "Editor → Senior Editor → Post-production Head",
    "estimated_budget": "₹30,000 – ₹2L (software + training)",
    "estimated_salary": "₹20,000/month → ₹15L/year",
    "entrance_exams_required": ["No mandatory exams", "Skill-based tests"],
    "link": "https://www.videomaker.com/",
    "related_careers": ["cinematographer", "film director", "producer"]
},

"youtuber": {
    "domain": "Media & Entertainment",
    "tags": ["youtube", "content", "digital media"],
    "description": [
        "Create and publish video content on YouTube",
        "Build and engage an online audience"
    ],
    "skills": ["Content creation", "Video editing", "Marketing"],
    "education": ["Self-learning", "Online courses"],
    "growth": "Small Creator → Monetized Channel → Influencer → Media Brand",
    "estimated_budget": "₹10,000 – ₹2L (camera, mic, basic setup)",
    "estimated_salary": "₹0–₹20,000/month → ₹10L–₹1Cr+/year",
    "entrance_exams_required": ["None"],
    "link": "https://www.youtube.com/creators/",
    "related_careers": ["content creator", "video editor", "digital marketer"]
},
"photographer": {
    "domain": "Media & Entertainment",
    "tags": [
    "photography","camera","editing","portraits","events"
    ],
    "description": [
        "Capture photographs for events, media, brands, or personal projects",
        "Edit and enhance photos using professional tools",
        "Work with clients to meet creative requirements"
    ],
    "skills": [
        "Camera handling",
        "Lighting techniques",
        "Photo editing (Lightroom, Photoshop)",
        "Creativity & composition"
    ],
    "education": [
        "Photography certification / Diploma",
        "Self-taught with portfolio (valid)"
    ],
    "growth": "Assistant Photographer → Professional Photographer → Creative Director",
    "estimated_budget": "₹30k–3 lakhs (gear + courses)",
    "estimated_salary": "₹20k/month → ₹30L+/year",
    "entrance_exams_required": [
        "No formal exams",
        "Portfolio-based selection"
    ],
    "related_careers": ["cinematographer", "photo editor", "content creator"]
},

# -------- Defense & Security --------

"army officer": {
    "domain": "Defense & Security",
    "tags": ["army", "defense", "leadership"],
    "description": [
        "Lead soldiers in military operations",
        "Ensure national security",
        "Plan and execute missions"
    ],
    "skills": ["Leadership", "Discipline", "Strategy"],
    "education": ["Any degree + NDA/CDS"],
    "growth": "Lieutenant → Captain → Major → Colonel",
    "estimated_budget": "₹50k – ₹2L (training & preparation)",
    "estimated_salary": "₹6L → ₹30L/year",
    "entrance_exams_required": [
        "NDA",
        "CDS",
        "Technical Entry Scheme (TES)"
    ],
    "link": "https://indianarmy.nic.in/",
    "related_careers": ["navy officer", "air force officer", "defense strategist"]
},

"navy officer": {
    "domain": "Defense & Security",
    "tags": ["navy", "sea", "defense"],
    "description": [
        "Operate naval ships and submarines",
        "Protect maritime borders",
        "Manage naval operations"
    ],
    "skills": ["Navigation", "Leadership", "Technical skills"],
    "education": ["Engineering/Any degree + NDA"],
    "growth": "Sub Lieutenant → Commander → Captain",
    "estimated_budget": "₹50k – ₹2L",
    "estimated_salary": "₹7L → ₹35L/year",
    "entrance_exams_required": [
        "NDA",
        "CDS",
        "INET"
    ],
    "link": "https://www.indiannavy.nic.in/",
    "related_careers": ["army officer", "air force officer", "maritime engineer"]
},

"air force officer": {
    "domain": "Defense & Security",
    "tags": ["air force", "aviation", "defense"],
    "description": [
        "Operate and manage aircraft",
        "Conduct air defense missions",
        "Ensure aerial security"
    ],
    "skills": ["Aviation", "Discipline", "Decision-making"],
    "education": ["Engineering/Any degree + NDA/AFCAT"],
    "growth": "Flying Officer → Squadron Leader → Wing Commander",
    "estimated_budget": "₹50k – ₹2L",
    "estimated_salary": "₹8L → ₹40L/year",
    "entrance_exams_required": [
        "NDA",
        "AFCAT",
        "CDS"
    ],
    "link": "https://indianairforce.nic.in/",
    "related_careers": ["army officer", "navy officer", "commercial pilot"]
},

# -------- Hospitality & Tourism --------

"hotel manager": {
    "domain": "Hospitality & Tourism",
    "tags": ["hotel", "management", "hospitality"],
    "description": [
        "Manage hotel operations",
        "Ensure guest satisfaction",
        "Supervise staff and services"
    ],
    "skills": ["Management", "Communication", "Customer service"],
    "education": ["Degree/Diploma in Hotel Management"],
    "growth": "Assistant Manager → Manager → General Manager",
    "estimated_budget": "₹1L – ₹5L",
    "estimated_salary": "₹25,000/month → ₹25L/year",
    "entrance_exams_required": [
        "NCHMCT JEE",
        "Institute-level hotel management entrances"
    ],
    "link": "https://www.ihmchennai.edu.in/",
    "related_careers": ["travel consultant", "tour guide", "event manager"]
},

"travel consultant": {
    "domain": "Hospitality & Tourism",
    "tags": ["travel", "tourism", "planning"],
    "description": [
        "Plan travel itineraries",
        "Assist customers with bookings",
        "Provide travel advice"
    ],
    "skills": ["Planning", "Communication", "Geography"],
    "education": ["Degree/Diploma in Travel & Tourism"],
    "growth": "Consultant → Senior Consultant → Travel Manager",
    "estimated_budget": "₹50k – ₹3L",
    "estimated_salary": "₹20,000/month → ₹18L/year",
    "entrance_exams_required": [
        "Institute-level tourism entrance exams",
        "Direct admission (private institutes)"
    ],
    "link": "https://www.travelandleisure.com/careers",
    "related_careers": ["travel planner", "hotel manager", "tour guide"]
},

"tour guide": {
    "domain": "Hospitality & Tourism",
    "tags": ["tourism", "guiding", "culture"],
    "description": [
        "Guide tourists at destinations",
        "Explain cultural and historical facts",
        "Ensure tourist safety"
    ],
    "skills": ["Communication", "History knowledge", "Public speaking"],
    "education": ["Tourism certification"],
    "growth": "Local Guide → National Guide → Tour Expert",
    "estimated_budget": "₹20k – ₹1.5L",
    "estimated_salary": "₹15,000/month → ₹12L/year",
    "entrance_exams_required": [
        "State tourism board certifications",
        "Institute-level guide training exams"
    ],
    "link": "https://www.worldtourism.org/",
    "related_careers": ["travel consultant", "hotel manager", "event coordinator"]
},

# -------- Design & Creative Arts --------

"interior designer": {
    "domain": "Design & Creative Arts",
    "tags": ["interior", "design", "architecture"],
    "description": [
        "Design indoor spaces",
        "Select materials and furniture",
        "Work with architects and clients"
    ],
    "skills": ["Creativity", "AutoCAD", "Space planning"],
    "education": ["Degree in Interior Design"],
    "growth": "Junior Designer → Designer → Design Consultant",
    "estimated_budget": "₹1.5L – ₹6L",
    "estimated_salary": "₹30,000/month → ₹30L/year",
    "entrance_exams_required": [
        "NIFT",
        "NID",
        "Institute-level design entrance exams"
    ],
    "link": "https://www.asid.org/",
    "related_careers": ["product designer", "architect", "ui ux designer"]
},

"ui ux designer": {
    "domain": "Design & Creative Arts",
    "tags": ["ui", "ux", "design", "technology"],
    "description": [
        "Design digital interfaces",
        "Improve user experience",
        "Collaborate with developers"
    ],
    "skills": ["UX research", "Figma", "Creativity"],
    "education": ["Design degree / Certification", "UI/UX courses"],
    "growth": "UI Designer → UX Designer → Product Designer",
    "estimated_budget": "₹30k – ₹4L",
    "estimated_salary": "₹6L → ₹40L/year",
    "entrance_exams_required": [
        "NID",
        "NIFT",
        "UCEED",
        "CEED"
    ],
    "link": "https://www.uxdesign.cc/",
    "related_careers": ["app designer", "product designer", "graphic designer"]
},

"product designer": {
    "domain": "Design & Creative Arts",
    "tags": ["product", "design", "innovation"],
    "description": [
        "Design consumer products",
        "Prototype and test designs",
        "Work with engineering teams"
    ],
    "skills": ["Creativity", "Prototyping", "Problem-solving"],
    "education": ["Design / Engineering degree"],
    "growth": "Designer → Senior Designer → Design Lead",
    "estimated_budget": "₹1L – ₹6L",
    "estimated_salary": "₹8L → ₹45L/year",
    "entrance_exams_required": [
        "NID",
        "NIFT",
        "Engineering entrance exams (optional)"
    ],
    "link": "https://www.idsa.org/",
    "related_careers": ["ui ux designer", "graphic designer", "industrial designer"]
},

"app designer": {
    "domain": "Design & Creative Arts",
    "tags": ["app", "mobile", "ui", "ux", "designing apps", "building apps"],
    "description": [
        "Design user-friendly mobile and web applications",
        "Create intuitive UI and improve user experience",
        "Collaborate with developers to implement designs"
    ],
    "skills": ["UI/UX Design", "Figma", "Prototyping", "Creativity"],
    "education": ["Design degree / Certification", "UI/UX courses"],
    "growth": "Junior App Designer → App Designer → Senior Product Designer",
    "estimated_budget": "₹30k – ₹4L",
    "estimated_salary": "₹6L → ₹35L/year",
    "entrance_exams_required": [
        "Portfolio-based hiring",
        "Design institute entrance exams"
    ],
    "link": "https://www.uxdesign.cc/",
    "related_careers": ["ui ux designer", "product designer", "graphic designer"]
},

"graphic designer": {
    "domain": "Design & Creativity",
    "tags": ["design", "graphics", "creativity", "adobe"],
    "description": [
        "Create visual concepts",
        "Design logos, brochures, and digital graphics"
    ],
    "skills": ["Adobe Photoshop", "Illustrator", "Creativity", "Typography"],
    "education": ["B.Des Graphic Design", "Certification in Digital Design"],
    "growth": "Graphic Designer → Senior Designer → Creative Director",
    "estimated_budget": "₹30k – ₹3L",
    "estimated_salary": "₹3L → ₹25L/year",
    "entrance_exams_required": [
        "NIFT",
        "NID",
        "Portfolio-based admission"
    ],
    "link": "https://www.coursera.org/specializations/graphic-design",
    "related_careers": ["illustrator", "ui ux designer", "product designer"]
},

"illustrator": {
    "domain": "Design & Creativity",
    "tags": ["illustration", "art", "design", "digital"],
    "description": [
        "Create illustrations for books, media, and digital platforms"
    ],
    "skills": ["Drawing", "Creativity", "Digital Art", "Sketching"],
    "education": ["B.Des Illustration", "Diploma in Digital Arts"],
    "growth": "Illustrator → Senior Illustrator → Art Director",
    "estimated_budget": "₹20k – ₹2L",
    "estimated_salary": "₹3L → ₹20L/year",
    "entrance_exams_required": [
        "Design institute entrance exams",
        "Portfolio-based selection"
    ],
    "link": "https://www.coursera.org/specializations/illustration",
    "related_careers": ["graphic designer", "ui ux designer", "product designer"]
},
"tattoo artist": {
    "domain": "Design & Creativity",
    "tags": ["tattoo", "body art", "illustration", "design"],
    "description": [
        "Create permanent tattoo designs on clients",
        "Consult clients on design, placement, and aftercare",
        "Maintain hygiene and safety standards"
    ],
    "skills": [
        "Drawing & illustration",
        "Tattoo machine handling",
        "Hygiene & sterilization",
        "Client communication"
    ],
    "education": [
        "Tattoo apprenticeship",
        "Professional tattoo training courses"
    ],
    "growth": "Apprentice → Tattoo Artist → Master Tattoo Artist / Studio Owner",
    "estimated_budget": "₹40k–2.5 lakhs",
    "estimated_salary": "₹25k/month → ₹40L+/year",
    "entrance_exams_required": [
        "No formal exams",
        "Apprenticeship evaluation"
    ],
    "related_careers": ["illustrator", "graphic designer", "body piercer"]
},
# -------- AI & Emerging Tech --------

"robotics engineer": {
    "domain": "AI & Robotics",
    "tags": ["robot", "ai", "automation", "engineering", "mechanical"],
    "description": [
        "Design and develop robots and automated systems",
        "Work on hardware, software, and sensors integration",
        "Test and maintain robotic systems"
    ],
    "skills": ["Mechanical Engineering", "Programming", "Electronics", "Problem Solving"],
    "education": ["Degree in Robotics / Mechanical Engineering / Mechatronics"],
    "growth": "Junior Engineer → Robotics Engineer → Senior Robotics Engineer",
    "estimated_budget": "₹2L – ₹10L",
    "estimated_salary": "₹6L → ₹45L/year",
    "entrance_exams_required": [
        "JEE Main / Advanced",
        "GATE",
        "Institute-level robotics programs"
    ],
    "link": "https://www.ieee.org/robotics",
    "related_careers": ["ai engineer", "automation engineer", "mechatronics engineer"]
},

"ai engineer": {
    "domain": "AI & Machine Learning",
    "tags": ["ai", "artificial intelligence", "machine learning", "robot", "data"],
    "description": [
        "Develop AI algorithms and models",
        "Work on machine learning, NLP, and computer vision projects",
        "Optimize and deploy AI solutions"
    ],
    "skills": ["Python", "Machine Learning", "Deep Learning", "Data Analysis", "Problem Solving"],
    "education": ["Degree in Computer Science / AI / Data Science"],
    "growth": "Junior AI Engineer → AI Engineer → Senior AI Engineer",
    "estimated_budget": "₹30k – ₹6L",
    "estimated_salary": "₹8L → ₹60L/year",
    "entrance_exams_required": [
        "JEE Main",
        "GATE",
        "University AI entrance exams"
    ],
    "link": "https://www.coursera.org/specializations/machine-learning",
    "related_careers": ["robotics engineer", "data scientist", "ml engineer"]
},

"blockchain developer": {
    "domain": "AI & Emerging Tech",
    "tags": ["blockchain", "crypto", "smart contracts"],
    "description": [
        "Develop decentralized applications",
        "Implement blockchain solutions",
        "Audit smart contracts"
    ],
    "skills": ["Solidity", "Ethereum", "Cryptography"],
    "education": ["Computer Science / Blockchain courses"],
    "growth": "Developer → Senior Developer → Blockchain Architect",
    "estimated_budget": "₹30k – ₹4L",
    "estimated_salary": "₹6L → ₹50L/year",
    "entrance_exams_required": [
        "Engineering entrance exams",
        "Blockchain certification tests",
        "Portfolio-based hiring"
    ],
    "link": "https://www.blockchain-council.org/careers",
    "related_careers": ["smart contract developer", "crypto analyst", "ai engineer"]
},

# -------- Social Media & Digital Influence --------

"social media influencer": {
    "domain": "Social Media & Digital Influence",
    "tags": ["social media", "content creation", "instagram", "youtube", "branding"],
    "description": [
        "Create engaging content for social media platforms",
        "Build and manage a personal brand",
        "Collaborate with brands for promotions"
    ],
    "skills": ["Content creation", "Creativity", "Communication", "Marketing"],
    "education": ["No formal degree required", "Digital marketing / content creation courses"],
    "growth": "Micro Influencer → Influencer → Brand Ambassador",
    "estimated_budget": "₹10k – ₹2L",
    "estimated_salary": "₹0 → ₹1Cr+/year",
    "entrance_exams_required": [
        "No formal exams",
        "Platform monetization eligibility"
    ],
    "link": "https://www.socialmediaexaminer.com/",
    "related_careers": ["digital marketer", "content creator", "brand strategist"]
},

"content creator": {
    "domain": "Social Media & Digital Influence",
    "tags": ["content", "video", "writing", "reels", "shorts"],
    "description": [
        "Create videos, blogs, and visual content",
        "Publish content across digital platforms"
    ],
    "skills": ["Video editing", "Writing", "Creativity"],
    "education": ["Media / Content creation courses"],
    "growth": "Creator → Senior Creator → Creative Director",
    "estimated_budget": "₹10k – ₹1.5L",
    "estimated_salary": "₹2L → ₹50L/year",
    "entrance_exams_required": [
        "No formal exams",
        "Portfolio & platform growth metrics"
    ],
    "link": "https://creators.google/",
    "related_careers": ["social media influencer", "video editor", "copywriter"]
},

"social media manager": {
    "domain": "Social Media & Digital Influence",
    "tags": ["social media", "management", "marketing"],
    "description": [
        "Manage social media accounts for brands",
        "Plan content calendars and campaigns"
    ],
    "skills": ["Analytics", "Marketing", "Communication"],
    "education": ["Digital Marketing / Media degree"],
    "growth": "Executive → Manager → Social Media Strategist",
    "estimated_budget": "₹30k – ₹3L",
    "estimated_salary": "₹4L → ₹25L/year",
    "entrance_exams_required": [
        "Digital marketing certification exams",
        "Institute-level media programs"
    ],
    "link": "https://buffer.com/resources/",
    "related_careers": ["digital marketer", "content strategist", "brand manager"]
},

# -------- Veterinary & Animal Care --------

"veterinary doctor": {
    "domain": "Veterinary & Animal Care",
    "tags": ["animals", "veterinary", "medicine", "pets"],
    "description": [
        "Diagnose and treat animal diseases",
        "Perform surgeries and vaccinations"
    ],
    "skills": ["Animal care", "Medical knowledge", "Compassion"],
    "education": ["BVSc & AH (Veterinary Science)"],
    "growth": "Veterinary Doctor → Senior Vet → Veterinary Specialist",
    "estimated_budget": "₹3L – ₹10L",
    "estimated_salary": "₹5L → ₹25L/year",
    "entrance_exams_required": [
        "NEET-UG",
        "State veterinary entrance exams"
    ],
    "link": "https://www.avma.org/resources-tools/careers",
    "related_careers": ["animal nutritionist", "zoologist", "pet care specialist"]
},

"veterinary assistant": {
    "domain": "Veterinary & Animal Care",
    "tags": ["animal care", "assistant", "clinic"],
    "description": [
        "Assist veterinarians in treatment",
        "Care for animals in clinics"
    ],
    "skills": ["Animal handling", "Basic medical care"],
    "education": ["Veterinary assistant certification"],
    "growth": "Assistant → Senior Assistant → Clinic Supervisor",
    "estimated_budget": "₹20k – ₹1.5L",
    "estimated_salary": "₹2L → ₹8L/year",
    "entrance_exams_required": [
        "Institute-level certification exams"
    ],
    "link": "https://www.veterinaryassistant.org/",
    "related_careers": ["veterinary doctor", "animal caretaker"]
},

"animal trainer": {
    "domain": "Veterinary & Animal Care",
    "tags": ["training", "animals", "behavior"],
    "description": [
        "Train animals for behavior and obedience",
        "Work with pets or service animals"
    ],
    "skills": ["Patience", "Animal psychology", "Training techniques"],
    "education": ["Animal training certification"],
    "growth": "Trainer → Senior Trainer → Animal Behavior Specialist",
    "estimated_budget": "₹15k – ₹1L",
    "estimated_salary": "₹3L → ₹15L/year",
    "entrance_exams_required": [
        "Animal training certification assessments"
    ],
    "link": "https://www.ccpdt.org/",
    "related_careers": ["veterinary doctor", "zoologist"]
},

# -------- Makeup, Beauty & Fashion --------

"makeup artist": {
    "domain": "Makeup & Beauty",
    "tags": ["makeup", "beauty", "fashion", "cosmetics"],
    "description": [
        "Apply makeup for events, shoots, and films",
        "Enhance facial features using cosmetic techniques"
    ],
    "skills": ["Makeup techniques", "Creativity", "Skin analysis"],
    "education": ["Professional makeup course"],
    "growth": "Junior Artist → Makeup Artist → Celebrity Makeup Artist",
    "estimated_budget": "₹20k – ₹1L",
    "estimated_salary": "₹2L → ₹20L/year",
    "entrance_exams_required": ["Beauty school entrance tests", "Portfolio submission"],
    "link": "https://www.makeupartistworldwide.com/",
    "related_careers": ["beauty influencer", "fashion stylist", "hair stylist"]
},

"beauty influencer": {
    "domain": "Makeup & Beauty",
    "tags": ["beauty", "skincare", "makeup", "social media"],
    "description": [
        "Create beauty and skincare content",
        "Review cosmetic products online"
    ],
    "skills": ["Presentation", "Content creation", "Branding"],
    "education": ["Makeup / skincare courses"],
    "growth": "Content Creator → Beauty Influencer → Brand Collaborator",
    "estimated_budget": "₹10k – ₹50k",
    "estimated_salary": "₹0 → ₹50L+/year",
    "entrance_exams_required": ["No formal exams, portfolio/online presence required"],
    "link": "https://influencermarketinghub.com/",
    "related_careers": ["makeup artist", "social media influencer"]
},

"hair stylist": {
    "domain": "Makeup & Beauty",
    "tags": ["hair", "styling", "salon"],
    "description": [
        "Style and treat hair",
        "Provide haircare consultations"
    ],
    "skills": ["Hair styling", "Creativity", "Customer service"],
    "education": ["Hair styling certification"],
    "growth": "Stylist → Senior Stylist → Salon Manager",
    "estimated_budget": "₹15k – ₹80k",
    "estimated_salary": "₹2L → ₹15L/year",
    "entrance_exams_required": ["Hair & beauty institute exams or certification"],
    "link": "https://www.beautyschools.org/",
    "related_careers": ["makeup artist", "fashion stylist"]
},

"fashion stylist": {
    "domain": "Makeup & Beauty",
    "tags": ["fashion", "styling", "clothing"],
    "description": [
        "Style outfits for clients or shoots",
        "Coordinate clothing and accessories"
    ],
    "skills": ["Fashion sense", "Creativity", "Trend analysis"],
    "education": ["Fashion styling courses"],
    "growth": "Stylist → Senior Stylist → Fashion Consultant",
    "estimated_budget": "₹25k – ₹1.2L",
    "estimated_salary": "₹3L → ₹25L/year",
    "entrance_exams_required": ["Fashion institute entrance exams or portfolio review"],
    "link": "https://www.vogue.com/careers",
    "related_careers": ["makeup artist", "fashion designer"]
},

"fashion designer": {
    "domain": "Makeup & Beauty",
    "tags": ["fashion", "design", "clothing", "apparel"],
    "description": [
        "Design clothing and accessories",
        "Develop seasonal collections",
        "Collaborate with brands and production teams"
    ],
    "skills": ["Creativity", "Pattern making", "Textile knowledge", "Sketching"],
    "education": ["Degree/Diploma in Fashion Design"],
    "growth": "Junior Designer → Fashion Designer → Senior Designer / Fashion Director",
    "estimated_budget": "₹50k – ₹3L",
    "estimated_salary": "₹4L → ₹50L/year",
    "entrance_exams_required": ["NIFT entrance", "NID entrance", "Fashion institute-specific exams"],
    "link": "https://www.nift.ac.in/careers",
    "related_careers": ["fashion stylist","fashion merchandiser", "model"]
},

"fashion_merchandiser": {
    "domain": "Makeup, Beauty & Fashion",
    "tags": ["fashion", "merchandising", "retail", "trend analysis"],
    "description": [
        "Plan and manage product assortments for fashion brands",
        "Analyze market trends and customer preferences",
        "Coordinate with design and retail teams for collections"
    ],
    "skills": ["Trend analysis", "Retail management", "Communication", "Data analysis"],
    "education": ["Degree/Diploma in Fashion Merchandising / Fashion Management"],
    "growth": "Assistant Merchandiser → Merchandiser → Senior Merchandiser / Fashion Manager",
    "estimated_budget": "₹50k – ₹3L (courses + training)",
    "estimated_salary": "₹3L → ₹25L/year",
    "entrance_exams_required": [
        "NIFT",
        "NID",
        "Institute-specific fashion & merchandising courses"
    ],
    "link": "https://www.nift.ac.in/careers",
    "related_careers": ["fashion buyer", "fashion stylist", "product designer"]
},
"model": {
    "domain": "Makeup, Beauty & Fashion",
    "tags": ["modeling", "fashion", "runway", "photography"],
    "description": [
        "Represent fashion brands and products in photoshoots, runway shows, and advertisements",
        "Maintain personal grooming and portfolio",
        "Collaborate with photographers, designers, and stylists"
    ],
    "skills": ["Posing", "Runway skills", "Confidence", "Fitness & grooming"],
    "education": ["Modeling courses (optional) / Portfolio building"],
    "growth": "Freelance Model → Professional Model → Supermodel / Brand Ambassador",
    "estimated_budget": "₹20k – ₹2L (portfolio, training, photoshoots)",
    "estimated_salary": "₹15k – ₹50k/month (entry) → ₹5L–₹50L per campaign",
    "entrance_exams_required": [
        "No formal exams",
        "Agency auditions / Talent scouting"
    ],
    "link": "https://www.models.com/",
    "related_careers": ["fashion influencer", "brand ambassador", "runway model"]
},

# -------- Environmental & Life Sciences --------

"wildlife biologist": {
    "domain": "Environmental & Life Sciences",
    "tags": ["wildlife", "biology", "conservation", "research"],
    "description": [
        "Study animals and their habitats",
        "Conduct field research and conservation projects",
        "Analyze data on wildlife populations and ecosystems"
    ],
    "skills": ["Ecology knowledge", "Field research", "Data analysis", "Report writing"],
    "education": ["B.Sc / M.Sc in Wildlife Biology, Zoology, Environmental Science"],
    "growth": "Research Assistant → Wildlife Biologist → Senior Biologist / Conservation Manager",
    "estimated_budget": "₹2–5 lakhs (education, fieldwork tools, travel)",
    "estimated_salary": "₹25k–60k/month → ₹6–12 L/year",
    "entrance_exams_required": [
        "UGC NET (Life Sciences / Zoology)",
        "CSIR NET (Life Sciences)",
        "State / University-level entrance tests for Wildlife Biology programs"
    ],
    "link": "https://www.worldwildlife.org/careers",
    "related_careers": ["ecologist", "conservation scientist", "zoologist"]
},

"environmental scientist": {
    "domain": "Environmental & Life Sciences",
    "tags": ["environment", "science", "research", "conservation"],
    "description": [
        "Analyze environmental data to solve ecological problems",
        "Study pollution, climate change, and sustainability",
        "Recommend policies and conservation strategies"
    ],
    "skills": ["Environmental analysis", "Data interpretation", "GIS", "Field research"],
    "education": ["B.Sc / M.Sc Environmental Science", "Environmental Engineering courses"],
    "growth": "Junior Researcher → Environmental Scientist → Senior Consultant / Policy Advisor",
    "estimated_budget": "₹2–6 lakhs (education, field equipment)",
    "estimated_salary": "₹30k–70k/month → ₹6–15 L/year",
    "entrance_exams_required": [
        "UGC NET (Environmental Science)",
        "GATE (Environmental Engineering)",
        "State / University-level environmental science exams"
    ],
    "link": "https://www.environmentalscience.org/careers",
    "related_careers": ["ecologist", "conservation scientist", "wildlife biologist"]
},

"ecologist": {
    "domain": "Environmental & Life Sciences",
    "tags": ["ecology", "research", "conservation", "biodiversity"],
    "description": [
        "Study ecosystems and species interactions",
        "Research environmental impacts",
        "Advise on conservation and sustainability projects"
    ],
    "skills": ["Field research", "Data analysis", "GIS", "Scientific reporting"],
    "education": ["B.Sc / M.Sc in Ecology, Environmental Science, Biology"],
    "growth": "Research Assistant → Ecologist → Senior Ecologist / Project Manager",
    "estimated_budget": "₹1.5–5 lakhs (education, fieldwork tools)",
    "estimated_salary": "₹25k–60k/month → ₹5–12 L/year",
    "entrance_exams_required": [
        "UGC NET (Life Sciences)",
        "CSIR NET (Ecology / Zoology)",
        "State-level ecology or environmental exams"
    ],
    "link": "https://www.ecology-careers.org/",
    "related_careers": ["wildlife biologist", "environmental scientist", "conservation officer"]
},

"conservation scientist": {
    "domain": "Environmental & Life Sciences",
    "tags": ["conservation", "research", "sustainability", "environment"],
    "description": [
        "Develop plans to protect natural resources",
        "Monitor conservation projects",
        "Advise on sustainable land and wildlife management"
    ],
    "skills": ["Ecology", "Policy analysis", "Project management", "Fieldwork"],
    "education": ["B.Sc / M.Sc in Environmental Science, Forestry, Ecology"],
    "growth": "Assistant Conservationist → Conservation Scientist → Senior Consultant / Policy Advisor",
    "estimated_budget": "₹2–6 lakhs (education, fieldwork equipment)",
    "estimated_salary": "₹30k–70k/month → ₹6–15 L/year",
    "entrance_exams_required": [
        "UGC NET (Environmental Science / Forestry)",
        "CSIR NET (Life Sciences)",
        "State-level conservation exams"
    ],
    "link": "https://www.conservation-careers.org/",
    "related_careers": ["wildlife biologist", "ecologist", "environmental scientist"]
},

"marine biologist": {
    "domain": "Environmental & Life Sciences",
    "tags": ["marine", "biology", "ocean", "research"],
    "description": [
        "Study ocean ecosystems and marine organisms",
        "Conduct field and lab research",
        "Develop conservation strategies for marine life"
    ],
    "skills": ["Marine biology", "Data collection", "Fieldwork", "Research techniques"],
    "education": ["B.Sc / M.Sc in Marine Biology, Oceanography, Zoology"],
    "growth": "Research Assistant → Marine Biologist → Senior Scientist / Oceanographer",
    "estimated_budget": "₹2–6 lakhs (education, field trips, lab work)",
    "estimated_salary": "₹30k–70k/month → ₹6–15 L/year",
    "entrance_exams_required": [
        "UGC NET (Life Sciences)",
        "CSIR NET (Life Sciences)",
        "University-level marine biology entrance exams"
    ],
    "link": "https://www.marinecareers.org/",
    "related_careers": ["wildlife biologist", "ecologist", "oceanographer"]
},
# -------- Sports & Fitness --------

"sports coach": {
    "domain": "Sports & Fitness",
    "tags": ["sports", "training", "athlete", "fitness"],
    "description": [
        "Train athletes and sports teams",
        "Develop fitness and skill programs"
    ],
    "skills": ["Leadership", "Strategy", "Fitness training", "Motivation"],
    "education": ["Degree in Physical Education / Sports Science"],
    "growth": "Assistant Coach → Coach → Head Coach / National Coach",
    "estimated_budget": "₹50k – ₹2L (courses, certifications)",
    "estimated_salary": "₹25k–80k/month → ₹5L+/year",
    "entrance_exams_required": ["NIS Coaching Certification", "State Sports Coaching exams"],
    "link": "https://www.nis.sports.gov.in/",
    "related_careers": ["fitness trainer", "physiotherapist", "sports analyst"]
},

"fitness trainer": {
    "domain": "Sports & Fitness",
    "tags": ["fitness", "personal trainer", "gym", "health"],
    "description": [
        "Design and conduct workout programs",
        "Assist clients in achieving fitness goals"
    ],
    "skills": ["Exercise physiology", "Nutrition knowledge", "Motivation", "Communication"],
    "education": ["Certification in Personal Training / Fitness Courses"],
    "growth": "Trainer → Senior Trainer → Fitness Manager / Gym Owner",
    "estimated_budget": "₹20k – ₹1.5L (certifications, tools, gym memberships)",
    "estimated_salary": "₹15k–50k/month → ₹3–10L/year",
    "entrance_exams_required": ["ACE Personal Trainer Certification", "NSCA CPT", "ISSA Fitness Trainer exams"],
    "link": "https://www.acefitness.org/",
    "related_careers": ["sports coach", "nutritionist", "physiotherapist"]
},

"sports analyst": {
    "domain": "Sports & Fitness",
    "tags": ["analytics", "data", "sports performance"],
    "description": [
        "Analyze sports performance data",
        "Provide insights to improve athlete performance"
    ],
    "skills": ["Data analysis", "Statistics", "Sports knowledge", "Video analysis"],
    "education": ["Degree in Sports Science / Statistics / Analytics"],
    "growth": "Junior Analyst → Analyst → Senior Sports Analyst",
    "estimated_budget": "₹50k – ₹2L (courses, software tools)",
    "estimated_salary": "₹25k–1L/month → ₹5–15L/year",
    "entrance_exams_required": ["Certification in Sports Analytics", "Institute-level analytics tests"],
    "link": "https://www.sportsanalytics.org/",
    "related_careers": ["data analyst", "sports coach", "performance trainer"]
},

"nutritionist": {
    "domain": "Sports & Fitness",
    "tags": ["nutrition", "diet", "fitness", "health"],
    "description": [
        "Plan diet programs for athletes and clients",
        "Advise on supplements and nutrition for performance"
    ],
    "skills": ["Diet planning", "Health knowledge", "Consultation", "Communication"],
    "education": ["Degree in Nutrition / Dietetics"],
    "growth": "Dietitian → Sports Nutritionist → Senior Nutrition Consultant",
    "estimated_budget": "₹50k – ₹3L (degree/certifications)",
    "estimated_salary": "₹20k–60k/month → ₹4–10L/year",
    "entrance_exams_required": ["ICMR-NIN Nutrition Entrance", "PG Diploma Nutrition exams"],
    "link": "https://www.nutrition.org/",
    "related_careers": ["fitness trainer", "physiotherapist", "sports coach"]
},
"sportsperson": {
    "domain": "Sports & Fitness",
    "tags": ["athlete", "competition", "fitness", "sports"],
    "description": [
        "Compete professionally in a chosen sport",
        "Train rigorously to improve skills and performance",
        "Participate in national and international competitions"
    ],
    "skills": ["Physical fitness", "Discipline", "Mental toughness", "Teamwork/Strategy"],
    "education": ["Degree in Physical Education / Sports Science (optional)"],
    "growth": "Junior Athlete → National Player → International Player / Olympian → Coach / Mentor",
    "estimated_budget": "₹50k – ₹10L (training, equipment, travel, coaching)",
    "estimated_salary": "₹0 → ₹50k/month (starting) → ₹20L+/year (sponsorships, prize money)",
    "entrance_exams_required": [
        "Sports Authority of India (SAI) trials",
        "National Sports Federations selection trials",
        "State-level sports quotas and championships"
    ],
    "link": "https://sportsauthorityofindia.nic.in/",
    "related_careers": ["sports coach", "fitness trainer", "sports analyst"]
},
# -------- Government Sector --------
"civil_servant": {
    "domain": "Government & Public Administration",
    "tags": ["administration", "policy", "governance"],
    "description": [
        "Formulate and implement government policies",
        "Administer public services",
        "Ensure law, order, and development at district/state/national level"
    ],
    "skills": ["Leadership", "Decision-making", "Policy analysis", "Communication"],
    "education": ["Any Bachelor's degree"],
    "growth": "IAS/IPS/IFS Officer → Senior Administrative Officer → Secretary/Principal Secretary",
    "estimated_budget": "₹50k – ₹2L (preparation & coaching)",
    "estimated_salary": "₹56k – ₹2.5L/month → ₹1.5–3L/month with seniority",
    "entrance_exams_required": [
        "UPSC Civil Services Exam (Prelims, Mains, Interview)"
    ],
    "link": "https://www.upsc.gov.in/",
    "related_careers": ["Indian Administrative Service (IAS)", "Indian Police Service (IPS)", "Indian Foreign Service (IFS)"]
},

"ias officer": {
    "domain": "Government Sector",
    "tags": ["administration", "civil services", "policy", "leadership"],
    "description": [
        "Implement government policies",
        "Manage district and state administration",
        "Advise ministers on policy matters"
    ],
    "skills": ["Leadership", "Decision-making", "Public administration"],
    "education": ["Any bachelor's degree"],
    "growth": "SDM → DM → Secretary → Chief Secretary",
    "estimated_budget": "₹50k – ₹2L (preparation & coaching)",
    "estimated_salary": "₹10L → ₹25L/year",
    "entrance_exams_required": ["UPSC Civil Services Examination"],
    "link": "https://www.upsc.gov.in/",
    "related_careers": ["ips officer", "ifs officer", "state civil services officer"]
},

"ips officer": {
    "domain": "Government Sector",
    "tags": ["police", "law enforcement", "security"],
    "description": [
        "Maintain law and order",
        "Lead police forces",
        "Handle crime prevention and investigation"
    ],
    "skills": ["Leadership", "Crisis management", "Discipline"],
    "education": ["Any bachelor's degree"],
    "growth": "ASP → SP → DIG → DGP",
    "estimated_budget": "₹50k – ₹2L",
    "estimated_salary": "₹10L → ₹30L/year",
    "entrance_exams_required": ["UPSC Civil Services Examination"],
    "link": "https://www.upsc.gov.in/",
    "related_careers": ["ias officer", "intelligence officer", "army officer"]
},

"ifs officer": {
    "domain": "Government Sector",
    "tags": ["foreign service", "diplomacy", "international relations"],
    "description": [
        "Represent India in foreign countries",
        "Handle international diplomacy",
        "Promote bilateral relations"
    ],
    "skills": ["Communication", "Negotiation", "Cultural awareness"],
    "education": ["Any bachelor's degree"],
    "growth": "Third Secretary → Ambassador → Foreign Secretary",
    "estimated_budget": "₹50k – ₹2L",
    "estimated_salary": "₹15L → ₹35L/year",
    "entrance_exams_required": ["UPSC Civil Services Examination"],
    "link": "https://mea.gov.in/",
    "related_careers": ["ias officer", "diplomat", "policy advisor"]
},

"government engineer": {
    "domain": "Government Sector",
    "tags": ["engineering", "public works", "infrastructure"],
    "description": [
        "Design and maintain public infrastructure",
        "Work in government departments like PWD, Railways",
        "Supervise construction projects"
    ],
    "skills": ["Engineering knowledge", "Project management"],
    "education": ["B.Tech / BE"],
    "growth": "Junior Engineer → Assistant Engineer → Executive Engineer",
    "estimated_budget": "₹1L – ₹4L",
    "estimated_salary": "₹6L → ₹18L/year",
    "entrance_exams_required": [
        "GATE",
        "SSC JE",
        "State engineering service exams"
    ],
    "link": "https://ssc.nic.in/",
    "related_careers": ["civil engineer", "railway engineer", "psu engineer"]
},

"bank po": {
    "domain": "Government Sector",
    "tags": ["banking", "finance", "public sector"],
    "description": [
        "Manage bank operations",
        "Handle customer accounts and loans",
        "Supervise clerical staff"
    ],
    "skills": ["Finance", "Communication", "Management"],
    "education": ["Any bachelor's degree"],
    "growth": "PO → Assistant Manager → Branch Manager",
    "estimated_budget": "₹20k – ₹1L",
    "estimated_salary": "₹6L → ₹15L/year",
    "entrance_exams_required": [
        "IBPS PO",
        "SBI PO"
    ],
    "link": "https://www.ibps.in/",
    "related_careers": ["bank clerk", "finance officer", "accounts officer"]
},

"ssc officer": {
    "domain": "Government Sector",
    "tags": ["clerical", "administration", "central government"],
    "description": [
        "Perform administrative duties",
        "Handle government documentation",
        "Assist senior officers"
    ],
    "skills": ["Organization", "Communication", "Basic computer skills"],
    "education": ["Any bachelor's degree"],
    "growth": "Assistant → Section Officer → Under Secretary",
    "estimated_budget": "₹10k – ₹50k",
    "estimated_salary": "₹4L → ₹12L/year",
    "entrance_exams_required": [
        "SSC CGL",
        "SSC CHSL",
        "SSC MTS"
    ],
    "link": "https://ssc.nic.in/",
    "related_careers": ["government clerk", "office superintendent"]
},

"railway officer": {
    "domain": "Government Sector",
    "tags": ["railways", "transport", "public service"],
    "description": [
        "Manage railway operations",
        "Oversee safety and logistics",
        "Handle railway administration"
    ],
    "skills": ["Management", "Technical knowledge", "Coordination"],
    "education": ["Engineering / Any degree (post-specific)"],
    "growth": "Officer → Divisional Officer → General Manager",
    "estimated_budget": "₹20k – ₹1.5L",
    "estimated_salary": "₹7L → ₹20L/year",
    "entrance_exams_required": [
        "RRB NTPC",
        "RRB JE",
        "UPSC Engineering Services"
    ],
    "link": "https://indianrailways.gov.in/",
    "related_careers": ["government engineer", "transport officer"]
},

"state civil services officer": {
    "domain": "Government Sector",
    "tags": ["state administration", "governance"],
    "description": [
        "Manage state-level administration",
        "Implement state policies",
        "Handle district governance"
    ],
    "skills": ["Administration", "Leadership", "Public policy"],
    "education": ["Any bachelor's degree"],
    "growth": "Deputy Collector → Collector → Principal Secretary",
    "estimated_budget": "₹30k – ₹1.5L",
    "estimated_salary": "₹8L → ₹20L/year",
    "entrance_exams_required": [
        "State PSC exams (MPSC, UPPSC, TNPSC, etc.)"
    ],
    "link": "https://www.upsc.gov.in/",
    "related_careers": ["ias officer", "ips officer"]
},
# -------- Finance & Accounting --------

"chartered accountant": {
    "domain": "Finance & Accounting",
    "tags": ["accounts", "audit", "tax"],
    "description": [
        "Manage accounts, audits, and taxation",
        "Provide financial compliance and reporting",
        "Advise businesses on financial strategy"
    ],
    "skills": ["Accounting", "Taxation", "Audit", "Compliance"],
    "education": ["CA qualification (ICAI)"],
    "growth": "CA → Senior CA → Finance Consultant / CFO",
    "estimated_budget": "₹3L – ₹6L (CA coaching + exams)",
    "estimated_salary": "₹6L → ₹1Cr+/year",
    "entrance_exams_required": ["CA Foundation", "CA Intermediate", "CA Final"],
    "link": "https://www.icai.org/",
    "related_careers": ["financial analyst", "auditor", "tax consultant"]
},

"financial analyst": {
    "domain": "Finance & Accounting",
    "tags": ["finance", "analysis", "investment"],
    "description": [
        "Analyze financial data and trends",
        "Prepare reports to support business decisions",
        "Forecast financial performance"
    ],
    "skills": ["Financial modeling", "Excel", "Analysis"],
    "education": ["Degree in Finance/Economics"],
    "growth": "Junior Analyst → Analyst → Senior Analyst / FP&A Lead",
    "estimated_budget": "₹1L – ₹4L",
    "estimated_salary": "₹5L → ₹35L/year",
    "entrance_exams_required": ["University entrance exams", "CFA Level 1 (optional)"],
    "link": "https://www.cfainstitute.org/",
    "related_careers": ["investment banker", "portfolio manager"]
},

"investment banker": {
    "domain": "Finance & Accounting",
    "tags": ["banking", "investment", "capital markets"],
    "description": [
        "Help companies raise capital and advise on deals",
        "Work on mergers & acquisitions",
        "Analyze corporate valuations"
    ],
    "skills": ["Financial modeling", "Valuation", "Negotiation"],
    "education": ["Finance / MBA / CFA"],
    "growth": "Analyst → Associate → Vice President → Director",
    "estimated_budget": "₹5L – ₹25L (MBA + certifications)",
    "estimated_salary": "₹10L → ₹2Cr+/year",
    "entrance_exams_required": ["CAT / GMAT / CFA (optional)"],
    "link": "https://www.investopedia.com/financial-careers-4427771",
    "related_careers": ["financial analyst", "private equity associate"]
},

"auditor": {
    "domain": "Finance & Accounting",
    "tags": ["audit", "compliance", "accounts"],
    "description": [
        "Review financial records and controls",
        "Ensure legal and regulatory compliance",
        "Identify financial risks and discrepancies"
    ],
    "skills": ["Attention to detail", "Accounting standards", "Risk assessment"],
    "education": ["Degree in Accounting / Commerce"],
    "growth": "Audit Associate → Senior Auditor → Audit Manager",
    "estimated_budget": "₹50k – ₹3L",
    "estimated_salary": "₹4L → ₹20L/year",
    "entrance_exams_required": ["CA/CPA/CMA basics (optional)"],
    "link": "https://opentuition.com/",  # Free accounting training resources :contentReference[oaicite:1]{index=1}
    "related_careers": ["chartered accountant", "internal auditor"]
},

"tax consultant": {
    "domain": "Finance & Accounting",
    "tags": ["tax", "finance", "law"],
    "description": [
        "Advise on tax planning and compliance",
        "Prepare tax returns",
        "Structure transactions for tax efficiency"
    ],
    "skills": ["Tax laws", "Accounting", "Advisory"],
    "education": ["Degree in Commerce / Law"],
    "growth": "Tax Associate → Tax Consultant → Tax Partner",
    "estimated_budget": "₹50k – ₹3L",
    "estimated_salary": "₹5L → ₹30L/year",
    "entrance_exams_required": ["Commerce entrance exams"],
    "link": "https://www.coursera.org/specializations/tax-planning",
    "related_careers": ["chartered accountant", "financial advisor"]
},

"risk analyst": {
    "domain": "Finance & Accounting",
    "tags": ["risk", "finance", "analytics"],
    "description": [
        "Identify and evaluate financial risks",
        "Support risk mitigation planning",
        "Monitor risk metrics and reporting"
    ],
    "skills": ["Risk modeling", "Statistics", "Finance"],
    "education": ["Degree in Finance/Economics/Statistics"],
    "growth": "Risk Analyst → Senior Risk Analyst → Risk Manager",
    "estimated_budget": "₹1L – ₹4L",
    "estimated_salary": "₹6L → ₹30L/year",
    "entrance_exams_required": ["FRM / Risk certification (optional)"],
    "link": "https://www.garp.org/#!/frm",  # FRM professional certification :contentReference[oaicite:2]{index=2}
    "related_careers": ["credit analyst", "financial analyst"]
},

"credit analyst": {
    "domain": "Finance & Accounting",
    "tags": ["credit", "analysis", "banking"],
    "description": [
        "Assess creditworthiness of clients/businesses",
        "Support loan and credit decisions",
        "Monitor loan performance"
    ],
    "skills": ["Data analysis", "Financial statements", "Risk assessment"],
    "education": ["Degree in Finance / Accounting"],
    "growth": "Junior Analyst → Credit Analyst → Senior Credit Analyst",
    "estimated_budget": "₹50k – ₹3L",
    "estimated_salary": "₹5L → ₹25L/year",
    "entrance_exams_required": ["Banking entrance tests"],
    "link": "https://en.wikipedia.org/wiki/Credit_analyst",  # Role overview :contentReference[oaicite:3]{index=3}
    "related_careers": ["risk analyst", "financial analyst"]
},

"financial advisor": {
    "domain": "Finance & Accounting",
    "tags": ["wealth", "planning", "investment"],
    "description": [
        "Advise individuals/organizations on financial planning",
        "Recommend investment strategies",
        "Assist in retirement and tax planning"
    ],
    "skills": ["Financial planning", "Communication", "Tax knowledge"],
    "education": ["Degree in Finance / CFP certification"],
    "growth": "Financial Advisor → Senior Advisor → Wealth Manager",
    "estimated_budget": "₹50k – ₹3L",
    "estimated_salary": "₹5L → ₹30L/year",
    "entrance_exams_required": ["CFP certification"],
    "link": "https://www.coursera.org/specializations/financial-planning",
    "related_careers": ["portfolio manager", "tax consultant"]
},
# -------- Arts & Humanities --------

"civil services officer": {
    "domain": "Arts & Humanities",
    "tags": ["upsc", "government", "administration", "policy"],
    "description": [
        "Formulate and implement government policies",
        "Manage administrative departments",
        "Serve in leadership roles for public welfare"
    ],
    "skills": ["Decision making", "Leadership", "Policy analysis"],
    "education": ["Any Bachelor's degree (Arts preferred)"],
    "growth": "Officer → District Magistrate → Secretary → Cabinet-level roles",
    "estimated_budget": "₹50k – ₹2L (coaching + preparation)",
    "estimated_salary": "₹10L → ₹60L+/year (incl. perks)",
    "entrance_exams_required": ["UPSC CSE"],
    "link": "https://www.upsc.gov.in/",
    "related_careers": ["policy analyst", "diplomat", "public administrator"]
},

"psychologist": {
    "domain": "Arts & Humanities",
    "tags": ["psychology", "mental health", "counseling"],
    "description": [
        "Assess and treat mental health issues",
        "Provide counseling and therapy",
        "Conduct psychological assessments"
    ],
    "skills": ["Empathy", "Observation", "Communication"],
    "education": ["BA/BSc Psychology → MA/MSc Psychology"],
    "growth": "Psychologist → Clinical Psychologist → Consultant",
    "estimated_budget": "₹1L – ₹5L",
    "estimated_salary": "₹4L → ₹30L/year",
    "entrance_exams_required": [
        "CUET",
        "University-specific psychology entrances"
    ],
    "link": "https://www.apa.org/careers",
    "related_careers": ["counselor", "psychiatrist", "social worker"]
},

"sociologist": {
    "domain": "Arts & Humanities",
    "tags": ["sociology", "research", "society"],
    "description": [
        "Study social behavior and structures",
        "Conduct social research and surveys",
        "Advise on social policy"
    ],
    "skills": ["Research", "Critical thinking", "Data interpretation"],
    "education": ["BA / MA Sociology"],
    "growth": "Researcher → Senior Sociologist → Policy Advisor",
    "estimated_budget": "₹50k – ₹3L",
    "estimated_salary": "₹3L → ₹20L/year",
    "entrance_exams_required": ["CUET", "University entrance exams"],
    "link": "https://www.asanet.org/careers/",
    "related_careers": ["policy analyst", "social researcher"]
},

"economist": {
    "domain": "Arts & Humanities",
    "tags": ["economics", "policy", "finance"],
    "description": [
        "Analyze economic data and trends",
        "Support government and corporate policy decisions",
        "Forecast economic outcomes"
    ],
    "skills": ["Data analysis", "Statistics", "Research"],
    "education": ["BA/MA Economics"],
    "growth": "Economist → Senior Economist → Chief Economic Advisor",
    "estimated_budget": "₹1L – ₹6L",
    "estimated_salary": "₹6L → ₹50L/year",
    "entrance_exams_required": ["CUET", "ISI Entrance", "University economics entrances"],
    "link": "https://www.worldbank.org/en/about/careers",
    "related_careers": ["policy analyst", "financial analyst"]
},

"journalist": {
    "domain": "Arts & Humanities",
    "tags": ["media", "journalism", "writing", "news"],
    "description": [
        "Research and report news stories",
        "Interview sources",
        "Write articles and reports"
    ],
    "skills": ["Writing", "Research", "Communication"],
    "education": ["BA Journalism / Mass Communication"],
    "growth": "Reporter → Senior Journalist → Editor",
    "estimated_budget": "₹30k – ₹3L",
    "estimated_salary": "₹3L → ₹25L/year",
    "entrance_exams_required": [
        "CUET",
        "IIMC Entrance",
        "Media institute entrances"
    ],
    "link": "https://www.iimc.gov.in/",
    "related_careers": ["editor", "content writer", "news anchor"]
},

"content writer": {
    "domain": "Arts & Humanities",
    "tags": ["writing", "content", "digital"],
    "description": [
        "Create articles, blogs, and website content",
        "Write marketing and informational content",
        "Optimize content for SEO"
    ],
    "skills": ["Writing", "SEO", "Creativity"],
    "education": ["BA English / Journalism (preferred)"],
    "growth": "Writer → Senior Writer → Content Strategist",
    "estimated_budget": "₹10k – ₹1L",
    "estimated_salary": "₹3L → ₹20L/year",
    "entrance_exams_required": ["No formal exams", "Portfolio-based hiring"],
    "link": "https://www.coursera.org/specializations/content-marketing",
    "related_careers": ["copywriter", "editor", "digital marketer"]
},

"copywriter": {
    "domain": "Arts & Humanities",
    "tags": ["advertising", "copywriting", "marketing"],
    "description": [
        "Write persuasive advertising content",
        "Develop brand messaging",
        "Support marketing campaigns"
    ],
    "skills": ["Creative writing", "Marketing psychology", "Branding"],
    "education": ["BA English / Advertising / Marketing"],
    "growth": "Junior Copywriter → Copywriter → Creative Director",
    "estimated_budget": "₹20k – ₹2L",
    "estimated_salary": "₹4L → ₹30L/year",
    "entrance_exams_required": ["Portfolio-based selection"],
    "link": "https://www.hubspot.com/resources/copywriting",
    "related_careers": ["content writer", "brand strategist"]
},

"history researcher": {
    "domain": "Arts & Humanities",
    "tags": ["history", "research", "academia"],
    "description": [
        "Research historical events and sources",
        "Publish academic papers",
        "Teach or work in archives/museums"
    ],
    "skills": ["Research", "Critical analysis", "Writing"],
    "education": ["BA / MA History → PhD (optional)"],
    "growth": "Researcher → Senior Researcher → Historian",
    "estimated_budget": "₹50k – ₹3L",
    "estimated_salary": "₹3L → ₹15L/year",
    "entrance_exams_required": ["CUET", "University history entrances"],
    "link": "https://www.historians.org/jobs-and-professional-development",
    "related_careers": ["archaeologist", "museum curator"]
},

"philosophy scholar": {
    "domain": "Arts & Humanities",
    "tags": ["philosophy", "ethics", "research"],
    "description": [
        "Study philosophical theories and ethics",
        "Teach philosophy or conduct academic research",
        "Contribute to ethical policy discussions"
    ],
    "skills": ["Critical thinking", "Logic", "Writing"],
    "education": ["BA / MA Philosophy"],
    "growth": "Scholar → Lecturer → Professor",
    "estimated_budget": "₹50k – ₹2L",
    "estimated_salary": "₹4L → ₹18L/year",
    "entrance_exams_required": ["CUET", "University philosophy entrances"],
    "link": "https://www.apaonline.org/page/careers",
    "related_careers": ["ethics consultant", "policy analyst"]
},
# -------- Space & Astronomy --------

"astrophysicist": {
    "domain": "Space & Astronomy",
    "tags": ["space", "physics", "astrophysics", "research"],
    "description": [
        "Study celestial objects like stars, galaxies, and black holes",
        "Analyze space data using physics and mathematics"
    ],
    "skills": ["Physics", "Mathematics", "Data analysis", "Research"],
    "education": ["BSc Physics", "MSc Astrophysics", "PhD (optional)"],
    "growth": "Research Assistant → Astrophysicist → Senior Scientist",
    "estimated_budget": "₹3–10 lakhs (India) → ₹15+ lakhs (abroad)",
    "estimated_salary": "₹50k–1.2 LPM → ₹4+ LPM",
    "entrance_exams_required": [
        "GATE (Physics)",
        "CSIR-NET "
    ],
    "link": "https://www.isro.gov.in/",
    "related_careers": ["astronomer", "cosmologist", "space scientist"]
},


"astronomer": {
    "domain": "Space & Astronomy",
    "tags": ["astronomy", "space observation", "telescopes"],
    "description": [
        "Observe and study celestial bodies",
        "Conduct space observations using telescopes"
    ],
    "skills": ["Observation", "Data interpretation", "Scientific writing"],
    "education": ["BSc Physics/Astronomy", "MSc Astronomy"],
    "growth": "Junior Astronomer → Astronomer → Observatory Scientist",
    "estimated_budget": "₹3–8 lakhs",
    "estimated_salary": "₹40k–1 LPM → ₹3+ LPM",
    "entrance_exams_required": [
        "IISER IAT",
        "JAM",
        "University-specific entrances"
    ],
    "link": "https://www.iau.org/",
    "related_careers": ["astrophysicist", "space researcher"]
},


"space scientist": {
    "domain": "Space & Astronomy",
    "tags": ["space research", "satellites", "missions"],
    "description": [
        "Work on satellite and space missions",
        "Research space technologies and planetary science"
    ],
    "skills": ["Research", "Programming", "Problem-solving"],
    "education": ["BTech / MSc", "PhD (preferred)"],
    "growth": "Scientist SC → Scientist SD → Senior Space Scientist",
    "estimated_budget": "₹4–12 lakhs",
    "estimated_salary": "₹60k–1.5 LPM → ₹5+ LPM",
    "entrance_exams_required": [
        "ISRO Centralised Recruitment Board (ICRB)",
        "GATE",
        "NET"
    ],
    "link": "https://www.isro.gov.in/Careers.html",
    "related_careers": ["aerospace engineer", "astrophysicist"]
},


"aerospace engineer": {
    "domain": "Space & Astronomy",
    "tags": ["aerospace", "rockets", "spacecraft"],
    "description": [
        "Design spacecraft and launch vehicles",
        "Work on propulsion and aerodynamics"
    ],
    "skills": ["Engineering design", "Physics", "CAD tools"],
    "education": ["BTech Aerospace Engineering", "MTech (optional)"],
    "growth": "Graduate Engineer → Aerospace Engineer → Lead Engineer",
    "estimated_budget": "₹6–15 lakhs",
    "estimated_salary": "₹70k–2 LPM → ₹6+ LPM",
    "entrance_exams_required": [
        "JEE Advanced",
        "GATE"
    ],
    "link": "https://www.nasa.gov/careers/",
    "related_careers": ["space scientist", "satellite engineer"]
},


"satellite engineer": {
    "domain": "Space & Astronomy",
    "tags": ["satellites", "communication", "space systems"],
    "description": [
        "Develop and maintain satellite systems",
        "Work on communication and navigation satellites"
    ],
    "skills": ["Electronics", "Embedded systems", "Signal processing"],
    "education": ["BTech ECE / Aerospace", "MTech (optional)"],
    "growth": "Systems Engineer → Satellite Engineer → Mission Lead",
    "estimated_budget": "₹5–12 lakhs",
    "estimated_salary": "₹60k–1.8 LPM → ₹5+ LPM",
    "entrance_exams_required": [
        "GATE",
        "ISRO recruitment exams"
    ],
    "link": "https://www.isro.gov.in/",
    "related_careers": ["aerospace engineer", "space scientist"]
},
# -------- Education & Training --------

"school teacher": {
    "domain": "Education & Training",
    "tags": ["teaching", "school", "education", "students"],
    "description": [
        "Teach academic subjects to school students",
        "Plan lessons and assess student performance"
    ],
    "skills": ["Subject knowledge", "Communication", "Classroom management"],
    "education": ["D.El.Ed / B.Ed + Subject Degree"],
    "growth": "Teacher → Senior Teacher → Head of Department → Principal",
    "estimated_budget": "₹50k – ₹3 lakhs",
    "estimated_salary": "₹25k–80k/month",
    "entrance_exams_required": [
        "CTET",
        "State TETs",
        "School-level recruitment exams"
    ],
    "link": "https://ctet.nic.in/",
    "related_careers": ["academic coordinator", "education administrator"]
},

"college professor": {
    "domain": "Education & Training",
    "tags": ["professor", "higher education", "research"],
    "description": [
        "Teach undergraduate and postgraduate students",
        "Conduct academic research and publish papers"
    ],
    "skills": ["Research", "Teaching", "Curriculum design"],
    "education": ["Master’s Degree", "PhD (preferred)"],
    "growth": "Assistant Professor → Associate Professor → Professor",
    "estimated_budget": "₹1–6 lakhs",
    "estimated_salary": "₹60k–2.5 LPM",
    "entrance_exams_required": [
        "UGC NET",
        "SET",
        "CSIR NET"
    ],
    "link": "https://ugcnet.nta.nic.in/",
    "related_careers": ["education researcher", "academic consultant"]
},

"online educator": {
    "domain": "Education & Training",
    "tags": ["online teaching", "edtech", "digital learning"],
    "description": [
        "Create and deliver online courses",
        "Teach via video platforms and learning portals"
    ],
    "skills": ["Content creation", "Presentation", "Subject expertise"],
    "education": ["Any degree + subject expertise"],
    "growth": "Educator → Lead Instructor → Course Director",
    "estimated_budget": "₹10k – ₹1.5 lakhs",
    "estimated_salary": "₹30k/month → ₹40L+/year",
    "entrance_exams_required": [
        "No formal exams",
        "Platform-based selection"
    ],
    "link": "https://www.coursera.org/teach",
    "related_careers": ["instructional designer", "content creator"]
},

"corporate trainer": {
    "domain": "Education & Training",
    "tags": ["training", "corporate", "soft skills"],
    "description": [
        "Train employees in technical or soft skills",
        "Design corporate learning programs"
    ],
    "skills": ["Public speaking", "Facilitation", "Domain expertise"],
    "education": ["Any degree + Training certifications"],
    "growth": "Trainer → Senior Trainer → L&D Manager",
    "estimated_budget": "₹30k – ₹2 lakhs",
    "estimated_salary": "₹5L → ₹30L/year",
    "entrance_exams_required": [
        "Certification-based entry",
        "Company-level interviews"
    ],
    "link": "https://www.atd.org/",
    "related_careers": ["hr consultant", "organizational coach"]
},

"instructional designer": {
    "domain": "Education & Training",
    "tags": ["curriculum", "learning design", "edtech"],
    "description": [
        "Design structured learning programs",
        "Create digital and classroom-based curricula"
    ],
    "skills": ["Curriculum design", "LMS tools", "Pedagogy"],
    "education": ["Education / Psychology / Instructional Design certification"],
    "growth": "Designer → Learning Architect → Education Strategist",
    "estimated_budget": "₹50k – ₹4 lakhs",
    "estimated_salary": "₹6L → ₹35L/year",
    "entrance_exams_required": [
        "Institute-level admissions",
        "Portfolio-based selection"
    ],
    "link": "https://www.edx.org/learn/instructional-design",
    "related_careers": ["online educator", "education consultant"]
},

"career counsellor": {
    "domain": "Education & Training",
    "tags": ["counselling", "career guidance", "students"],
    "description": [
        "Guide students on academic and career choices",
        "Conduct aptitude and interest assessments"
    ],
    "skills": ["Psychology", "Communication", "Analysis"],
    "education": ["Psychology / Education degree + counseling certification"],
    "growth": "Counsellor → Senior Counsellor → Career Strategist",
    "estimated_budget": "₹40k – ₹2 lakhs",
    "estimated_salary": "₹4L → ₹20L/year",
    "entrance_exams_required": [
        "Institute-level counseling program admissions"
    ],
    "link": "https://www.ncda.org/",
    "related_careers": ["education advisor", "life coach"]
},

"special education teacher": {
    "domain": "Education & Training",
    "tags": ["special education", "inclusive education", "disabilities"],
    "description": [
        "Teach students with special learning needs",
        "Design individualized education plans"
    ],
    "skills": ["Patience", "Behavioral therapy", "Adaptive teaching"],
    "education": ["Special Education Degree / Certification"],
    "growth": "Special Educator → Inclusion Specialist → Program Head",
    "estimated_budget": "₹60k – ₹3 lakhs",
    "estimated_salary": "₹30k–1 LPM",
    "entrance_exams_required": [
        "RCI-approved institute entrance exams"
    ],
    "link": "https://rehabcouncil.nic.in/",
    "related_careers": ["child psychologist", "occupational therapist"]
},

#-------- Agriculture & Food Science --------
"agricultural scientist": {
    "domain": "Agriculture & Food Science",
    "tags": ["agriculture", "research", "crop science"],
    "description": [
        "Research crop improvement techniques",
        "Develop sustainable farming practices"
    ],
    "skills": ["Plant science", "Data analysis", "Research methods"],
    "education": ["BSc Agriculture", "MSc/PhD (optional)"],
    "growth": "Research Assistant → Scientist → Senior Scientist",
    "estimated_budget": "₹2–6 lakhs",
    "estimated_salary": "₹40k–1 LPM → ₹3+ LPM",
    "entrance_exams_required": [
        "ICAR AIEEA",
        "State Agriculture Entrance Exams"
    ],
    "related_careers": ["soil scientist", "food technologist", "agronomist"]
},

"food technologist": {
    "domain": "Agriculture & Food Science",
    "tags": ["food", "processing", "quality"],
    "description": [
        "Develop and test food products",
        "Ensure food quality and safety standards"
    ],
    "skills": ["Food chemistry", "Quality control", "Process optimization"],
    "education": ["BTech Food Technology", "MTech (optional)"],
    "growth": "Quality Analyst → Food Technologist → R&D Manager",
    "estimated_budget": "₹3–7 lakhs",
    "estimated_salary": "₹35k–1.2 LPM → ₹4 LPM",
    "entrance_exams_required": [
        "JEE Main",
        "ICAR AIEEA",
        "GATE (PG level)"
    ],
    "related_careers": ["nutritionist", "food safety officer"]
},

"agronomist": {
    "domain": "Agriculture & Food Science",
    "tags": ["soil", "crop management", "farming"],
    "description": [
        "Improve crop yield and soil health",
        "Advise farmers on best practices"
    ],
    "skills": ["Soil science", "Crop planning", "Field research"],
    "education": ["BSc Agriculture"],
    "growth": "Field Officer → Agronomist → Senior Consultant",
    "estimated_budget": "₹2–5 lakhs",
    "estimated_salary": "₹30k–90k/month → ₹3 LPM",
    "entrance_exams_required": [
        "ICAR AIEEA",
        "State agriculture CETs"
    ],
    "related_careers": ["agricultural scientist", "soil scientist"]
},

"food safety officer": {
    "domain": "Agriculture & Food Science",
    "tags": ["food safety", "inspection", "regulation"],
    "description": [
        "Inspect food production units",
        "Ensure compliance with food safety laws"
    ],
    "skills": ["Food laws", "Inspection", "Reporting"],
    "education": ["BSc Food Technology / Agriculture"],
    "growth": "Food Inspector → Food Safety Officer → Senior Officer",
    "estimated_budget": "₹3–6 lakhs",
    "estimated_salary": "₹5L–₹12L/year",
    "entrance_exams_required": [
        "State PSC Exams",
        "FSSAI Recruitment Exams"
    ],
    "related_careers": ["food technologist", "quality analyst"]
},

#-------- Cybersecurity & Protection --------
"cybersecurity analyst": {
    "domain": "Cybersecurity & Protection",
    "tags": ["security", "networks", "threat analysis"],
    "description": [
        "Monitor systems for security threats",
        "Respond to cyber incidents"
    ],
    "skills": ["Networking", "Threat detection", "SIEM tools"],
    "education": ["BTech CS / Cybersecurity certification"],
    "growth": "Security Analyst → Senior Analyst → Security Manager",
    "estimated_budget": "₹50k–6 lakhs",
    "estimated_salary": "₹45k–1.5 LPM → ₹6+ LPM",
    "entrance_exams_required": [
        "Company security interviews",
        "Certification exams (Security+, CEH)"
    ],
    "related_careers": ["ethical hacker", "soc analyst", "network security engineer"]
},

"ethical hacker": {
    "domain": "Cybersecurity & Protection",
    "tags": ["hacking", "penetration testing", "security"],
    "description": [
        "Identify vulnerabilities in systems",
        "Perform penetration testing legally"
    ],
    "skills": ["Linux", "Pen-testing tools", "Scripting"],
    "education": ["Cybersecurity courses", "Certifications"],
    "growth": "Junior Pentester → Ethical Hacker → Red Team Lead",
    "estimated_budget": "₹40k–5 lakhs",
    "estimated_salary": "₹50k–2 LPM → ₹8+ LPM",
    "entrance_exams_required": [
        "CEH",
        "OSCP",
        "Company hacking challenges"
    ],
    "related_careers": ["cybersecurity analyst", "bug bounty hunter"]
},

"soc analyst": {
    "domain": "Cybersecurity & Protection",
    "tags": ["soc", "monitoring", "incident response"],
    "description": [
        "Monitor security operations center alerts",
        "Analyze and respond to incidents"
    ],
    "skills": ["Log analysis", "SIEM", "Incident handling"],
    "education": ["BTech CS / Cybersecurity training"],
    "growth": "SOC Level 1 → SOC Level 2 → SOC Lead",
    "estimated_budget": "₹30k–4 lakhs",
    "estimated_salary": "₹35k–1.2 LPM → ₹5 LPM",
    "entrance_exams_required": [
        "Security analyst interviews",
        "SOC skill assessments"
    ],
    "related_careers": ["cybersecurity analyst", "incident responder"]
},

"digital forensics expert": {
    "domain": "Cybersecurity & Protection",
    "tags": ["forensics", "investigation", "cybercrime"],
    "description": [
        "Investigate cybercrime cases",
        "Recover and analyze digital evidence"
    ],
    "skills": ["Forensics tools", "Cyber law basics", "Analytical thinking"],
    "education": ["Cyber Forensics / CS degree"],
    "growth": "Forensics Analyst → Senior Expert → Cybercrime Consultant",
    "estimated_budget": "₹1–6 lakhs",
    "estimated_salary": "₹6L–₹20L/year",
    "entrance_exams_required": [
        "Law enforcement recruitment exams",
        "Cyber forensics certifications"
    ],
    "related_careers": ["cybersecurity analyst", "cyber law consultant"]
},

# ---------- Law & Justice -------
"lawyer": {
    "domain": "Law & Justice",
    "tags": ["legal practice", "litigation", "advocacy"],
    "description": [
        "Represent clients in courts and legal proceedings",
        "Provide legal advice and draft legal documents"
    ],
    "skills": ["Legal research", "Argumentation", "Drafting"],
    "education": ["LLB (3-year / 5-year)"],
    "growth": "Junior Advocate → Senior Advocate → Legal Consultant",
    "estimated_budget": "₹3–8 lakhs",
    "estimated_salary": "₹30k–1.5 LPM → ₹10+ LPM",
    "entrance_exams_required": [
        "CLAT",
        "AILET",
        "State Bar Council Enrollment"
    ],
    "related_careers": ["judge", "legal advisor", "public prosecutor"]
},

"judge": {
    "domain": "Law & Justice",
    "tags": ["judiciary", "justice", "constitutional law"],
    "description": [
        "Preside over court proceedings",
        "Interpret laws and deliver judgments"
    ],
    "skills": ["Legal reasoning", "Impartial decision-making", "Deep law knowledge"],
    "education": ["LLB + Judicial Services Training"],
    "growth": "Civil Judge → District Judge → High Court Judge",
    "estimated_budget": "₹5–10 lakhs",
    "estimated_salary": "₹80k–2.5 LPM → ₹4+ LPM",
    "entrance_exams_required": [
        "Judicial Services Examination",
        "Higher Judicial Service Exams"
    ],
    "related_careers": ["lawyer", "legal scholar"]
},

"legal advisor": {
    "domain": "Law & Justice",
    "tags": ["corporate law", "compliance", "advisory"],
    "description": [
        "Advise organizations on legal matters",
        "Ensure compliance with laws and regulations"
    ],
    "skills": ["Contract drafting", "Corporate law", "Risk assessment"],
    "education": ["LLB", "LLM (optional)"],
    "growth": "Legal Executive → Legal Advisor → General Counsel",
    "estimated_budget": "₹4–9 lakhs",
    "estimated_salary": "₹50k–2 LPM → ₹12+ LPM",
    "entrance_exams_required": [
        "Company legal interviews",
        "Bar Council Enrollment"
    ],
    "related_careers": ["corporate lawyer", "compliance officer"]
},

"public prosecutor": {
    "domain": "Law & Justice",
    "tags": ["criminal law", "prosecution", "public service"],
    "description": [
        "Represent the state in criminal cases",
        "Prosecute accused in courts"
    ],
    "skills": ["Criminal law", "Courtroom advocacy", "Case analysis"],
    "education": ["LLB"],
    "growth": "Assistant Public Prosecutor → Public Prosecutor → Special Prosecutor",
    "estimated_budget": "₹3–7 lakhs",
    "estimated_salary": "₹40k–1.5 LPM → ₹5+ LPM",
    "entrance_exams_required": [
        "State Public Prosecutor Exams",
        "Judicial / State Recruitment Exams"
    ],
    "related_careers": ["criminal lawyer", "judge"]
},

"cyber law consultant": {
    "domain": "Law & Justice",
    "tags": ["cyber law", "it act", "digital crimes"],
    "description": [
        "Handle legal issues related to cybercrime",
        "Advise on IT laws and data protection"
    ],
    "skills": ["Cyber laws", "Legal research", "Technology awareness"],
    "education": ["LLB", "PG Diploma in Cyber Law"],
    "growth": "Legal Associate → Cyber Law Consultant → Policy Advisor",
    "estimated_budget": "₹2–6 lakhs",
    "estimated_salary": "₹50k–2 LPM → ₹8+ LPM",
    "entrance_exams_required": [
        "Law degree admissions",
        "Cyber law certification exams"
    ],
    "related_careers": ["digital forensics expert", "it compliance officer"]
},
# -------- Creative Technology ------------
"interaction designer": {
    "domain": "Creative Technology",
    "tags": ["interaction design", "HCI", "prototyping"],
    "description": [
        "Create engaging digital interactions",
        "Design system behavior and animations"
    ],
    "skills": ["HCI", "Prototyping", "Animation", "UX"],
    "education": ["Design degree / Creative technology courses"],
    "growth": "Interaction Designer → Senior Designer → Experience Architect",
    "estimated_budget": "₹40k – ₹5 lakhs",
    "estimated_salary": "₹7L → ₹45L/year",
    "entrance_exams_required": ["Portfolio review"],
    "related_careers": ["ui ux designer", "motion graphics artist"]
},

"game developer": {
    "domain": "Creative Technology",
    "tags": ["gaming", "interactive", "development"],
    "description": [
        "Design and build video games",
        "Implement gameplay mechanics and interactive features"
    ],
    "skills": ["Unity/Unreal", "C#/C++", "3D math", "Game design"],
    "education": ["Computer Science / Game development courses"],
    "growth": "Junior Game Dev → Game Developer → Lead Developer",
    "estimated_budget": "₹50k – ₹8 lakhs",
    "estimated_salary": "₹5L → ₹40L/year",
    "entrance_exams_required": ["Technical interviews", "Portfolio review"],
    "related_careers": ["game designer", "vr/ar developer"]
},

"vr ar developer": {
    "domain": "Creative Technology",
    "tags": ["vr", "ar", "immersive", "interactive"],
    "description": [
        "Build virtual and augmented reality experiences",
        "Create immersive interactive environments"
    ],
    "skills": ["Unity/Unreal", "3D modeling", "C#/C++", "UX"],
    "education": ["Game dev / VR/AR specialization"],
    "growth": "VR Developer → Immersive Tech Lead → XR Architect",
    "estimated_budget": "₹60k – ₹10 lakhs",
    "estimated_salary": "₹6L → ₹50L/year",
    "entrance_exams_required": ["Portfolio review", "Skill tests"],
    "related_careers": ["game developer", "interaction designer"]
},

"motion graphics artist": {
    "domain": "Creative Technology",
    "tags": ["motion graphics", "animation", "video"],
    "description": [
        "Create animated graphics and visual effects",
        "Work on ads, films, and digital content"
    ],
    "skills": ["After Effects", "Cinema 4D", "Animation"],
    "education": ["Animation / Motion graphics courses"],
    "growth": "Motion Artist → Senior Motion Artist → Creative Director",
    "estimated_budget": "₹30k – ₹6 lakhs",
    "estimated_salary": "₹4L → ₹35L/year",
    "entrance_exams_required": ["Portfolio-based selection"],
    "related_careers": ["video editor", "ui ux designer"]
},

"creative coder": {
    "domain": "Creative Technology",
    "tags": ["coding", "creative coding", "interactive art"],
    "description": [
        "Use code as a creative medium for art and interaction",
        "Develop interactive installations and generative art"
    ],
    "skills": ["Processing", "p5.js", "WebGL", "Creative scripting"],
    "education": ["CS / Creative tech courses"],
    "growth": "Junior Creative Coder → Creative Technologist → Experiential Lead",
    "estimated_budget": "₹40k – ₹7 lakhs",
    "estimated_salary": "₹5L → ₹30L/year",
    "entrance_exams_required": ["Portfolio review"],
    "related_careers": ["interaction designer", "vr ar developer"]
},

# --------- Music & Performing Arts----------
"singer": {
    "domain": "Music & Performing Arts",
    "tags": ["vocals", "performance", "stage"],
    "description": [
        "Perform songs using vocal techniques",
        "Record vocals for live shows, albums, or digital platforms"
    ],
    "skills": ["Voice control", "Pitch accuracy", "Stage presence"],
    "education": ["Music training / Vocal courses"],
    "growth": "Backup Singer → Lead Singer → Professional Artist",
    "estimated_budget": "₹20k – ₹3 lakhs",
    "estimated_salary": "₹15k/month → ₹1Cr+/year",
    "entrance_exams_required": [
        "Auditions",
        "Reality show selections"
    ],
    "related_careers": ["music composer", "performing artist"]
},

"music composer": {
    "domain": "Music & Performing Arts",
    "tags": ["composition", "melody", "creation"],
    "description": [
        "Compose original music pieces",
        "Create melodies for films, games, and albums"
    ],
    "skills": ["Music theory", "Composition", "Instrument knowledge"],
    "education": ["Music composition courses"],
    "growth": "Assistant Composer → Composer → Music Director",
    "estimated_budget": "₹30k – ₹5 lakhs",
    "estimated_salary": "₹4L → ₹50L/year",
    "entrance_exams_required": [
        "Portfolio review",
        "Music auditions"
    ],
    "related_careers": ["music producer", "songwriter"]
},

"music producer": {
    "domain": "Music & Performing Arts",
    "tags": ["production", "recording", "studio"],
    "description": [
        "Manage music production from recording to final output",
        "Work with artists and sound engineers"
    ],
    "skills": ["DAWs", "Sound design", "Mixing basics"],
    "education": ["Music production courses"],
    "growth": "Assistant Producer → Producer → Executive Producer",
    "estimated_budget": "₹40k – ₹6 lakhs",
    "estimated_salary": "₹6L → ₹60L/year",
    "entrance_exams_required": [
        "Portfolio-based hiring"
    ],
    "related_careers": ["sound engineer", "music composer"]
},

"sound engineer": {
    "domain": "Music & Performing Arts",
    "tags": ["audio", "sound", "engineering"],
    "description": [
        "Handle sound recording and live audio systems",
        "Ensure sound quality during events and recordings"
    ],
    "skills": ["Audio equipment", "Mixing", "Acoustics"],
    "education": ["Sound engineering courses"],
    "growth": "Junior Engineer → Sound Engineer → Audio Director",
    "estimated_budget": "₹35k – ₹5 lakhs",
    "estimated_salary": "₹4L → ₹30L/year",
    "entrance_exams_required": [
        "Technical skill tests"
    ],
    "related_careers": ["music producer", "live sound technician"]
},

"songwriter": {
    "domain": "Music & Performing Arts",
    "tags": ["lyrics", "writing", "songs"],
    "description": [
        "Write lyrics for songs across genres",
        "Collaborate with composers and singers"
    ],
    "skills": ["Creative writing", "Rhyming", "Storytelling"],
    "education": ["Songwriting / Creative writing courses"],
    "growth": "Lyric Writer → Songwriter → Creative Lead",
    "estimated_budget": "₹10k – ₹2 lakhs",
    "estimated_salary": "₹2L → ₹25L/year",
    "entrance_exams_required": [
        "Portfolio submission"
    ],
    "related_careers": ["music composer", "content writer"]
},

"instrumental musician": {
    "domain": "Music & Performing Arts",
    "tags": ["instrument", "playing", "practice"],
    "description": [
        "Perform music using musical instruments",
        "Play solo or as part of bands and orchestras"
    ],
    "skills": ["Instrument mastery", "Timing", "Music reading"],
    "education": ["Instrument-specific training"],
    "growth": "Session Musician → Performer → Music Mentor",
    "estimated_budget": "₹15k – ₹2.5 lakhs",
    "estimated_salary": "₹3L → ₹30L/year",
    "entrance_exams_required": [
        "Auditions",
        "Music school tests"
    ],
    "related_careers": ["singer", "music composer"]
},

"music teacher": {
    "domain": "Music & Performing Arts",
    "tags": ["teaching", "training", "education"],
    "description": [
        "Teach music theory or instruments",
        "Train students for performances and exams"
    ],
    "skills": ["Teaching", "Music theory", "Communication"],
    "education": ["Music degree / Teaching certification"],
    "growth": "Instructor → Senior Teacher → Music Academy Head",
    "estimated_budget": "₹20k – ₹2 lakhs",
    "estimated_salary": "₹3L → ₹15L/year",
    "entrance_exams_required": [
        "Teaching certification",
        "Skill assessment"
    ],
    "related_careers": ["instrumental musician", "vocal coach"]
},

}
# ================= Intelligent Domain Filtering & Search Functions =================

def get_careers_by_domain(domain_name):
    """
    Return all careers in a given domain.
    """
    return {k: v for k, v in CAREER_INFO.items() if v["domain"].lower() == domain_name.lower()}


def search_careers_by_tag(tag_name):
    """
    Return all careers matching a tag.
    """
    return {
        k: v
        for k, v in CAREER_INFO.items()
        if tag_name.lower() in [t.lower() for t in v.get("tags", [])]
    }


def search_careers_by_keyword(keyword):
    """
    Return careers where keyword appears in:
    - Career name
    - Career description
    - Tags
    """
    result = {}
    for k, v in CAREER_INFO.items():
        if (
            keyword.lower() in k.lower()
            or any(keyword.lower() in d.lower() for d in v.get("description", []))
            or any(keyword.lower() in t.lower() for t in v.get("tags", []))
        ):
            result[k] = v
    return result


def get_related_careers(career_name):
    """
    Return related careers for a given career.
    """
    career_data = CAREER_INFO.get(career_name.lower())
    if career_data and "related_careers" in career_data:
        return career_data["related_careers"]
    return []


# ------------------ New Functions for Budget, Salary, Entrance Exams ------------------

def search_careers_by_budget(min_budget=None, max_budget=None):
    """
    Return careers that fall within the estimated budget range.
    min_budget and max_budget are in INR numeric values.
    Example: min_budget=20000, max_budget=100000
    """
    result = {}
    for k, v in CAREER_INFO.items():
        budget_str = v.get("estimated_budget", "")
        # Extract numeric values from string like '₹20k – ₹1L'
        import re
        nums = re.findall(r'\d+', budget_str.replace(',', ''))
        if not nums:
            continue
        # Convert to integer in rupees
        if "k" in budget_str.lower():
            nums = [int(n) * 1000 for n in nums]
        elif "l" in budget_str.lower():
            nums = [int(n) * 100000 for n in nums]
        career_min = nums[0]
        career_max = nums[-1] if len(nums) > 1 else nums[0]

        if (min_budget is None or career_max >= min_budget) and (max_budget is None or career_min <= max_budget):
            result[k] = v
    return result


def search_careers_by_salary(min_salary=None, max_salary=None):
    """
    Return careers that fall within the estimated salary range.
    min_salary and max_salary are in INR numeric values.
    Example: min_salary=200000, max_salary=1000000
    """
    result = {}
    for k, v in CAREER_INFO.items():
        salary_str = v.get("estimated_salary", "")
        import re
        nums = re.findall(r'\d+', salary_str.replace(',', ''))
        if not nums:
            continue
        # Convert to integer in rupees
        if "k" in salary_str.lower():
            nums = [int(n) * 1000 for n in nums]
        elif "l" in salary_str.lower():
            nums = [int(n) * 100000 for n in nums]
        career_min = nums[0]
        career_max = nums[-1] if len(nums) > 1 else nums[0]

        if (min_salary is None or career_max >= min_salary) and (max_salary is None or career_min <= max_salary):
            result[k] = v
    return result


def search_careers_by_entrance_exam(exam_name):
    """
    Return all careers that require a particular entrance exam or certification.
    """
    result = {}
    for k, v in CAREER_INFO.items():
        exams = v.get("entrance_exams", [])
        if any(exam_name.lower() in e.lower() for e in exams):
            result[k] = v
    return result
