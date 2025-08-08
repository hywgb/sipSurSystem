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

Endpoints
- Health: GET /health
- Version: GET /version
- Agents: PUT /agents/{id}, GET /agents, GET /agents/{id}, DELETE /agents/{id}
- Conversations: POST /conversations, GET /conversations?status=, GET /conversations/{id}
- Messages: POST /conversations/{id}/messages, GET /conversations/{id}/messages
- Assign/Close: POST /conversations/{id}/assign, POST /conversations/{id}/close
- AI Placeholders: POST /ai/qa, POST /ai/summary, POST /ai/quality