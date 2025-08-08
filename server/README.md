# ITACATI Contact Center - Backend

## Run

Create venv and install deps:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start server:

```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Health: GET /health
Version: GET /version
Agents: PUT /agents/{id}, GET /agents
Conversations: POST /conversations, GET /conversations
Messages: POST /conversations/{id}/messages, GET /conversations/{id}/messages