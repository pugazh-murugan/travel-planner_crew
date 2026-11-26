"""CrewAI Travel Planner - Week 4 Day 3.

The user types a city and a Travel Planner agent suggests exactly 3 places to visit.
Run:  python travel_planner.py
"""
import asyncio
import os
import sys

from crewai import Agent, Crew, Task

# The API key is read from the environment (never hard-code or commit it).
# MODEL tells CrewAI which model to call, e.g. openai/gpt-4o-mini.
if not os.getenv("OPENAI_API_KEY"):
    sys.exit("OPENAI_API_KEY is not set. Run: export OPENAI_API_KEY='your-key'")
os.environ.setdefault("MODEL", "openai/gpt-4o-mini")

city = input("Which city? ").strip()
if not city:
    sys.exit("Please enter a city name.")

# The backstory steers the writing: who the planner writes for and in what style.
planner = Agent(
    role="Local Travel Planner",
    goal=(
        "Suggest the three best places for a first-time visitor to see in a given "
        "city, each with a short reason why it is worth the time."
    ),
    backstory=(
        "You are a well-travelled local guide who has spent 15 years helping "
        "first-time visitors with only one or two days to spare. You pick famous "
        "highlights over obscure spots, mention the best time of day to go, and "
        "keep every suggestion short, practical and friendly."
    ),
    verbose=True,
)

# expected_output defines the shape so we get three clean lines, not an essay.
task = Task(
    description=(
        "Suggest exactly 3 places to visit in {city}. Choose places a first-time "
        "visitor should not miss, and make sure they are real places in {city}."
    ),
    expected_output=(
        "A numbered list of exactly 3 lines and nothing else (no intro, no "
        "conclusion). Each line follows the format: "
        "'<number>. <Place name> - <one short sentence on why to go>'. "
        "Example: '1. Amber Fort - hilltop fort with mirrored halls, go early'."
    ),
    agent=planner,
)

crew = Crew(agents=[planner], tasks=[task])

result = asyncio.run(crew.kickoff_async(inputs={"city": city}))
print("\n" + str(result))
