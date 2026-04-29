# AI Job Search Agent

## Overview
This project is an Agentic AI-based system that helps users find suitable jobs based on their role, location, and skills.

It follows an agent-based approach where different components work together to achieve a goal.

---

## Features
- Job filtering based on role and location
- Skill matching with job requirements
- Match score calculation
- Decision making (Apply / Not Recommended)
- Job ranking (best match first)
- Suggestions for improvement

---

## Agentic AI Concepts Used
- Goal-based execution
- Planning (deciding steps to perform)
- Tool usage (job filtering and analysis)
- Decision making
- Multi-agent design (Filter Agent, Analysis Agent, Decision Agent)

---

## Project Structure

ai-job-agent/
│
├── main.py # User input & output
├── agent_controller.py # Main agent (planning & coordination)
├── agent.py # Skill analysis & decision logic
├── jobs.py # Job filtering logic
├── data.json # Job dataset
└── README.md
