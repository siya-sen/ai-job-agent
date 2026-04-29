def analyze_job(user_skills, job):
    job_skills = job["skills"]

    matched = [s for s in user_skills if s.lower() in [j.lower() for j in job_skills]]
    missing = [s for s in job_skills if s.lower() not in [u.lower() for u in user_skills]]

    score = (len(matched) / len(job_skills)) * 100

    decision = "Apply" if score >= 60 else "Not Recommended"

    if missing:
      suggestion = f"Improve {missing} to increase chances"
    else:
      suggestion = "You are a strong match for this role"

    return {
      "match_score": f"{score:.0f}%",
      "matched_skills": matched,
      "missing_skills": missing,
      "decision": decision,
      "suggestion": suggestion
    }