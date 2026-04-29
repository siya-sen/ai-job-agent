import json

def load_jobs():
    with open("data.json") as f:
        return json.load(f)

def filter_jobs(role, location, user_skills):
    jobs = load_jobs()
    result = []

    for job in jobs:
        if role.lower() in job["title"].lower() and location.lower() in job["location"].lower():
            
            # check skill match
            match = any(skill.lower() in [s.lower() for s in job["skills"]] for skill in user_skills)

            if match:
                result.append(job)

    return result

    for job in jobs:
        if role.lower() in job["title"].lower() and location.lower() in job["location"].lower():
            result.append(job)

    return result