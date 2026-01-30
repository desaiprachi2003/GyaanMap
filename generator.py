import realtime_links

def format_response(career_key, intent, data):
    # 1. Sub-intent: Course Links (ONLY raw links)
    if intent == "course_links":
        links = realtime_links.REALTIME_LINKS.get(career_key, ["No links found."])
        return "\n".join(links)

    # 2. Sub-intents: Specific Fields (ONLY raw data)
    field_map = {
        "skills": "skills",
        "growth": "growth",
        "estimated_salary": "estimated_salary",
        "estimated_budget": "estimated_budget",
        "entrance_exams_required": "entrance_exams_required",
        "related_careers": "related_careers"
    }

    if intent in field_map:
        val = data.get(field_map[intent], "N/A")
        if intent == "growth" and isinstance(val, list):
            return " → ".join(val)
        return "\n".join(val) if isinstance(val, list) else str(val)

    # 3. Default: Full Career Response
    name = career_key.replace("_", " ").title()
    
    def bullet_list(key):
        items = data.get(key, [])
        return "• " + "\n• ".join(items) if isinstance(items, list) else f"• {items}"

    growth_data = data.get('growth', [])
    growth_path = " → ".join(growth_data) if isinstance(growth_data, list) else growth_data

    return (
        f"{name}\n"
        f"Domain: {data.get('domain', 'N/A')}\n\n"
        f"What they do:\n{bullet_list('description')}\n\n"
        f"Skills required:\n{bullet_list('skills')}\n\n"
        f"Education & training:\n{bullet_list('education')}\n\n"
        f"Career growth:\n{growth_path}\n\n"
        f"Estimated Budget:\n{data.get('estimated_budget', 'N/A')}\n\n"
        f"Estimated Salary:\n{data.get('estimated_salary', 'N/A')}\n\n"
        f"Entrance Exams:\n{bullet_list('entrance_exams_required')}\n\n"
        f"Related Careers:\n{bullet_list('related_careers')}\n\n"
        f"You can ask:\n• skills required\n• course links\n• suggest related careers"
    )