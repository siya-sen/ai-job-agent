from agent_controller import job_search_agent

role = input("Enter job role: ")
location = input("Enter location: ")
skills = input("Enter your skills (comma separated): ")

user_skills = [s.strip() for s in skills.split(",")]

results = job_search_agent(role, location, user_skills)

if not isinstance(results, str) and results:
    best = results[0]
    print("\n🏆 BEST MATCH:")
    print(f"{best['job']['title']} in {best['job']['location']}")
    print(f"Score: {best['analysis']['match_score']}")

print("\n📊 Final Results:\n")

if isinstance(results, str):
    print(results)
else:
    for item in results:
        job = item["job"]
        analysis = item["analysis"]

        print("="*40)
        print(f"Role: {job['title']}")
        print(f"Location: {job['location']}")

        print(f"Match Score: {analysis['match_score']}")
        print(f"Decision: {analysis['decision']}")
        print(f"Suggestion: {analysis['suggestion']}")
        print("="*40)