from jobs import filter_jobs
from agent import analyze_job

def job_search_agent(role, location, user_skills):
    print("\n🤖 Agent started...")

    # Agent 1: Filter Agent
    print("🔎 Filter Agent: Finding jobs...")
    jobs = filter_jobs(role, location, user_skills)

    if not jobs:
        return "No jobs found"

    results = []

    for job in jobs:
        print(f"\n🧠 Analysis Agent: Analyzing {job['title']}")
        analysis = analyze_job(user_skills, job)

        # Agent 3: Decision Agent
        decision = analysis["decision"]

        results.append({
            "job": job,
            "analysis": analysis,
            "final_decision": decision
        })

    # Ranking (best first)
    results = sorted(
        results,
        key=lambda x: int(x["analysis"]["match_score"].replace('%', '')),
        reverse=True
    )

    return results