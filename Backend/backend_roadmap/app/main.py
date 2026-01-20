from app.services.roadmap_service import generate_ai_roadmap, get_resources_for_step
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.roadmap_service import generate_ai_roadmap

app = FastAPI(title="GyaanMap Career Roadmap API")

class RoadmapRequest(BaseModel):
    career: str

@app.post("/roadmap")
def generate_roadmap(request: RoadmapRequest):
    ai_text = generate_ai_roadmap(request.career)

    # 🔹 FALLBACK if AI fails
    if ai_text is None:
        return {
            "career": request.career,
            "roadmap": [
                {
                    "step_number": 1,
                    "title": f"Understand fundamentals of {request.career}",
                    "resources": get_resources_for_step("Learn " + request.career)

                },
                {
                    "step_number": 2,
                    "title": "Learn core concepts and theory",
                    "resources": get_resources_for_step("Learn " + request.career)

                },
                {
                    "step_number": 3,
                    "title": "Practice with hands-on projects",
                    "resources": get_resources_for_step("Learn " + request.career)

                },
                {
                    "step_number": 4,
                    "title": "Learn tools and frameworks",
                    "resources": get_resources_for_step("Learn " + request.career)

                },
                {
                    "step_number": 5,
                    "title": "Build portfolio and prepare for jobs",
                    "resources": get_resources_for_step("Learn " + request.career)

                }
            ],
            "note": "Fallback roadmap used due to AI API unavailability"
        }

    # 🔹 AI SUCCESS PATH
    steps = []
    lines = ai_text.split("\n")
    step_number = 1

    for line in lines:
        if line.strip():
            steps.append({
                "step_number": step_number,
                "title": line.strip(),
                "resources": get_resources_for_step(line.strip())

                
            })
            step_number += 1

    return {
        "career": request.career,
        "roadmap": steps
    }
