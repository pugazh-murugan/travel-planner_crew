# CrewAI Travel Planner

A single CrewAI agent that suggests 3 places to visit in any city you type.

## Setup

```bash
mkdir travel-planner && cd travel-planner
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt

export OPENAI_API_KEY="your-key"  # Windows: $env:OPENAI_API_KEY="your-key"
export MODEL="openai/gpt-4o-mini" # Windows: $env:MODEL="openai/gpt-4o-mini"
```

## Run

```bash
python travel_planner.py
```

```
Which city? Jaipur
1. Amber Fort - hilltop fort with mirrored halls, go early
2. Hawa Mahal - the pink facade, best in morning light
3. City Palace - royal courtyards and a textile museum
```

## How it works

- **Agent**: Local Travel Planner with a role, goal and backstory aimed at first-time visitors.
- **Task**: asks for exactly 3 places in `{city}`; `expected_output` forces a 3-line numbered list.
- **Crew**: one agent + one task, run with `crew.kickoff(inputs={"city": city})`.

The API key is read from the environment and is never stored in the code.
