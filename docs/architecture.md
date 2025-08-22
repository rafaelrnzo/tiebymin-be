BE-SLIDESHOW/
├── app/
│   ├── api/                      # All routing layer (HTTP request entrypoint)
│   │   ├── v1/                   # API version (v1)
│   │   │   ├── endpoints/        # Per resource/module
│   │   │   │   ├── user.py
│   │   │   │   ├── auth.py
│   │   │   │   └── ...
│   │   │   └── api_router.py     # Aggregates all routers
│   │   └── deps/                 # Dependency injection for routes
│   │       └── auth.py
│   ├── core/                     # Core app configuration (settings, security, logging, etc.)
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logging.py
│   ├── models/                   # ORM models (SQLAlchemy definitions)
│   │   ├── user.py
│   │   ├── base.py
│   │   └── ...
│   ├── schemas/                  # Request & response schemas (Pydantic)
│   │   ├── user.py
│   │   └── token.py
│   ├── services/                 # Business logic layer
│   │   ├── user_service.py
│   │   └── auth_service.py
│   ├── repositories/             # Data access abstraction (repository pattern)
│   │   ├── user_repo.py
│   │   └── ...
│   ├── db/                       # Database initialization and session management
│   │   ├── base.py               # Base class for all models
│   │   ├── session.py            # SQLAlchemy session handler
│   │   └── init_db.py
│   ├── utils/                    # General-purpose helper utilities
│   │   ├── hashing.py
│   │   └── email_sender.py
│   └── main.py                   # FastAPI application entry point
├── tests/                        # Unit & integration tests
│   ├── api/
│   ├── services/
│   └── ...
├── .env                          # Environment variables file
├── alembic/                      # Database migrations (if using Alembic)
├── requirements.txt              # List of Python dependencies (used with pip)
├── README.md                     # Project overview and usage guide
└── .gitignore                    # Git ignored files (e.g., __pycache__, .env)
