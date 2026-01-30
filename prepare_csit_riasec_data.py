import pandas as pd
import numpy as np

np.random.seed(42)

CAREERS = {
    # CORE DEV
    "Backend Developer":         {"R":3,"I":5,"A":1,"S":1,"E":2,"C":4},
    "Frontend Developer":        {"R":2,"I":3,"A":5,"S":3,"E":2,"C":2},
    "Full Stack Developer":      {"R":3,"I":4,"A":3,"S":2,"E":2,"C":3},
    "Mobile App Developer":      {"R":2,"I":3,"A":4,"S":2,"E":2,"C":2},
    "Game Developer":            {"R":3,"I":3,"A":5,"S":1,"E":2,"C":1},

    # DATA / AI
    "Data Scientist":            {"R":2,"I":5,"A":2,"S":1,"E":2,"C":4},
    "Data Analyst":              {"R":2,"I":4,"A":2,"S":2,"E":2,"C":5},
    "Machine Learning Engineer": {"R":3,"I":5,"A":2,"S":1,"E":2,"C":3},
    "AI Engineer":               {"R":3,"I":5,"A":2,"S":1,"E":2,"C":3},
    "Big Data Engineer":         {"R":4,"I":4,"A":1,"S":1,"E":2,"C":5},

    # CLOUD / DEVOPS
    "DevOps Engineer":           {"R":4,"I":4,"A":1,"S":1,"E":3,"C":5},
    "Cloud Engineer":            {"R":4,"I":4,"A":1,"S":1,"E":3,"C":5},
    "Site Reliability Engineer": {"R":4,"I":4,"A":1,"S":1,"E":3,"C":5},
    "Systems Engineer":          {"R":4,"I":4,"A":1,"S":1,"E":2,"C":5},

    # SECURITY
    "Cybersecurity Analyst":     {"R":4,"I":5,"A":1,"S":1,"E":2,"C":4},
    "Security Engineer":         {"R":4,"I":5,"A":1,"S":1,"E":2,"C":4},

    # QA / PROCESS
    "QA Engineer":               {"R":4,"I":3,"A":1,"S":1,"E":2,"C":5},
    "Automation Test Engineer":  {"R":4,"I":4,"A":1,"S":1,"E":2,"C":5},

    # DESIGN
    "UI/UX Designer":            {"R":1,"I":2,"A":5,"S":4,"E":2,"C":1},
    "Product Designer":          {"R":1,"I":3,"A":5,"S":3,"E":3,"C":1},

    # MANAGEMENT / HYBRID
    "Product Manager":           {"R":1,"I":3,"A":2,"S":4,"E":5,"C":2},
    "Technical Program Manager": {"R":2,"I":3,"A":1,"S":4,"E":5,"C":3},
    "Tech Lead":                 {"R":3,"I":4,"A":2,"S":3,"E":4,"C":3},

    # SUPPORT / SPECIALIZED
    "Solutions Architect":       {"R":3,"I":4,"A":1,"S":3,"E":4,"C":4},
    "IT Support Engineer":       {"R":4,"I":3,"A":1,"S":4,"E":2,"C":4},
}

rows = []
SAMPLES_PER_CAREER = 200  # 25 × 200 = 5000 rows

for career, base in CAREERS.items():
    for _ in range(SAMPLES_PER_CAREER):
        rows.append({
            "R": np.clip(np.random.normal(base["R"], 0.5), 1, 5),
            "I": np.clip(np.random.normal(base["I"], 0.5), 1, 5),
            "A": np.clip(np.random.normal(base["A"], 0.5), 1, 5),
            "S": np.clip(np.random.normal(base["S"], 0.5), 1, 5),
            "E": np.clip(np.random.normal(base["E"], 0.5), 1, 5),
            "C": np.clip(np.random.normal(base["C"], 0.5), 1, 5),
            "career": career
        })

df = pd.DataFrame(rows)
df.to_csv("csit_riasec_dataset.csv", index=False)

print("✅ SELLABLE CS/IT DATASET READY:", df.shape)
