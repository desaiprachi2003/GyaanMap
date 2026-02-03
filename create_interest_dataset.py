import pandas as pd

# ----------------------------
# Load existing RIASEC dataset
# ----------------------------
df = pd.read_csv("csit_riasec_dataset.csv")

# ----------------------------
# Career → Interest mapping
# ----------------------------
career_to_interest = {
    # Technical
    "Backend Developer": "Technical",
    "Frontend Developer": "Technical",
    "Full Stack Developer": "Technical",
    "DevOps Engineer": "Technical",
    "Site Reliability Engineer": "Technical",
    "Systems Engineer": "Technical",
    "Tech Lead": "Technical",
    "Mobile App Developer": "Technical",


    # Data
    "Data Analyst": "Data",
    "Data Scientist": "Data",
    "Big Data Engineer": "Data",
    "Machine Learning Engineer": "Data",
    "AI Engineer": "Data",

    # Design
    "UI/UX Designer": "Design",
    "Product Designer": "Design",
    "Game Developer": "Design",

    # Management
    "Product Manager": "Management",
    "Technical Program Manager": "Management",
    "Solutions Architect": "Management",

    # Quality & Support
    "QA Engineer": "QualitySupport",
    "Automation Test Engineer": "QualitySupport",
    "IT Support Engineer": "QualitySupport",

    # Security & Cloud
    "Cybersecurity Analyst": "SecurityCloud",
    "Security Engineer": "SecurityCloud",
    "Cloud Engineer": "SecurityCloud",
}

# ----------------------------
# Create interest_label column
# ----------------------------
df["interest_label"] = df["career"].map(career_to_interest)

# Safety check
missing = df[df["interest_label"].isna()]["career"].unique()
if len(missing) > 0:
    raise ValueError(f"Unmapped careers found: {missing}")

# ----------------------------
# Save new dataset
# ----------------------------
output_file = "csit_riasec_interest_dataset.csv"
df.to_csv(output_file, index=False)

print("✅ Interest-based dataset created:", output_file)
print("📊 Label distribution:")
print(df["interest_label"].value_counts())
print(df[["R","I","A","S","E","C"]].describe())