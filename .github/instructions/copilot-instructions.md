---
applyTo: "**"
---

# 🧠 GitHub Copilot Instructions — FastAPI Project

## 📁 Project Structure & Layer Separation

Use this folder structure:

app/
├── api/            # Routing & HTTP handlers
├── services/       # Business logic
├── repositories/   # Data access abstraction
├── models/         # ORM entities
├── schemas/        # Pydantic request/response schemas
├── core/           # Config, security, logging
├── db/             # Engine & session init
├── utils/          # Shared helper functions
└── main.py         # FastAPI entrypoint

When adding a new feature:

- Create endpoint(s) under `api/v1/endpoints/`
- Add service function in `services/`
- Create repository class in `repositories/`
- Add SQLAlchemy model in `models/` if needed
- Define Pydantic schema in `schemas/`

---

## 🧰 Coding Conventions

- Use `async def` for I/O-bound operations.
- All functions must include type hints.
- File names: `snake_case.py`
- Class names: `PascalCase`
- No business logic inside route handlers — delegate to services.
- Inject dependencies (e.g., `get_db`, `get_current_user`) via `api/deps/`.

---

## 🔐 Security & Error Handling

- Use JWT-based authentication (configured in `core/security.py`)
- Handle exceptions using `core/logging.py` or FastAPI exception handlers.
- Validate all input with Pydantic.
- Handle database errors gracefully using try/except in repositories or services.

---

## 🧪 Testing Guidelines

- Place tests under `tests/` folder, mirroring `app/` structure.
- Use `pytest` for test framework and `httpx.AsyncClient` for API tests.
- Write unit tests for service and repository logic.
- Use `TestClient` or dependency overrides for isolated testing.

---

## 📦 Standard Web Response Wrapper (English)

All endpoints **must** wrap their JSON responses in the following structure:

```jsonc
{
  "code": <integer>,               // HTTP status code (e.g. 200, 201, 400, etc.)
  "status": "<string>",            // HTTP status text (e.g. "OK", "Created", "Bad Request")
  "column": [                      // optional: dynamic column definitions for UI tables
    {
      "field": "string",
      "headerName": "string",
      "width": integer,
      // …other CustomColumn properties
    }
  ],
  "data": <T>,                     // the main payload (object or array)
  "paging": {                      // optional: pagination info, omit if not paginated
    "page": <integer>,
    "size": <integer>,
    "totalItems": <integer>,
    "totalPages": <integer>
  },
  "errors": {                      // optional: validation or business errors
    "<fieldName>": ["<error1>", "<error2>", …],
    …
  },
  "metadata": {                    // optional: any additional info (e.g. requestId, executionTime)
    "<key>": <value>,
    …
  }
}

--

## 🤖 Copilot-Specific Instructions

To GitHub Copilot:

- When writing route handlers, delegate core logic to service functions.
- Prefer calling repository methods like `UserRepo(db).get_by_id(...)` over raw queries.
- When suggesting schemas, ensure field alignment with the corresponding models.
- Place reusable logic (e.g., token generation) in `utils/` or `services/`.

