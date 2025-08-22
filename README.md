# BE-FT (Backend FastAPI Training)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)](https://postgresql.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Backend API untuk aplikasi training data management menggunakan FastAPI framework.


> **Note**: Project ini menggunakan FastAPI dengan struktur modular untuk training data management, review system, dan AI tools integration.

## 📋 Table of Contents

- [🎯 Fitur Utama](#-fitur-utama)
- [📁 Struktur Project](#-struktur-project)
- [🚀 Quick Start](#-quick-start)
- [🤖 AI Tools Modular](#-ai-tools-modular)
- [🛠️ Utils Modular](#️-utils-modular)
- [📋 Available Endpoints](#-available-endpoints)
- [🧪 Testing](#-testing)
- [🔧 Development](#-development)
- [📚 Tech Stack](#-tech-stack)
- [🌍 Environment Variables](#-environment-variables)
- [📖 Documentation](#-documentation)
- [📁 Generated Files](#-generated-files)
- [🗄️ Database Schema](#️-database-schema)
- [🤝 Contributing](#-contributing)
- [📞 Support](#-support)
- [📄 License](#-license)

## 🎯 Fitur Utama

- **Training Data Management**: Manajemen data training dengan hooks, scenes, dan hashtags
- **Review System**: Sistem review untuk approve/reject/skip training data
- **Export Functionality**: Export data training ke format JSONL
- **Authentication**: JWT-based authentication system
- **Pagination**: Pagination untuk data training queue
- **AI Tools Integration**: Modular AI tools untuk text overlay dan processing

## 📁 Struktur Project

```
app/
├── api/            # Routing & HTTP handlers
│   ├── v1/         # API version v1
│   │   ├── endpoints/      # Endpoint handlers
│   │   │   ├── auth.py     # Authentication endpoints
│   │   │   ├── health.py   # Health check endpoints
│   │   │   ├── review.py   # Review management endpoints
│   │   │   └── training.py # Training data endpoints
│   │   └── routers.py      # Main router (modular)
│   └── deps/       # Dependency injection
│       └── auth.py # Authentication dependencies
├── core/           # Config, security, logging
├── db/             # Database engine & session
├── models/         # SQLAlchemy ORM models
│   ├── training.py # Training data models
│   └── user.py     # User models
├── schemas/        # Pydantic request/response schemas
│   ├── training.py # Training data schemas
│   ├── user.py     # User schemas
│   ├── review.py   # Review schemas
│   ├── token.py    # Token schemas
│   ├── health.py   # Health check schemas
│   └── web_response.py # Web response schemas
├── services/       # Business logic layer
│   ├── auth_service.py    # Authentication service
│   ├── training_service.py # Training data service
│   ├── review_service.py  # Review service
│   └── export_service.py  # Data export service
├── repositories/   # Data access layer
│   ├── base.py     # Base repository
│   ├── user.py     # User repository
│   ├── training.py # Training data repository
│   └── review.py   # Review repository
├── utils/          # Helper utilities (modular, per domain)
│   ├── hashing.py
│   ├── pagination.py
│   ├── serializers.py
│   └── response_helpers.py
├── ai_tools/       # Modular AI tools integration
│   ├── overlay_text.py
│   ├── function_map.py
│   └── registry.json
└── main.py         # FastAPI application entry point
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL database
- Virtual environment (recommended)
- Git (untuk cloning repository)

### Installation

1. Clone repository
```bash
git clone <repository-url>
cd BE-FT
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Setup environment variables
```bash
# Buat file .env dengan konfigurasi yang diperlukan
# Contoh: DATABASE_URL, JWT_SECRET_KEY, dll
```

5. Setup database
```bash
# Jalankan migration untuk membuat tabel
alembic upgrade head
```

6. Run the application
```bash
python main.py
```

Alternative dengan uvicorn:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

7. Access the application
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/api/v1/health

## 🤖 AI Tools Modular

- Semua integrasi AI tools kini modular di folder `app/ai_tools/`.
- Tambahkan tool baru dengan membuat file baru dan update `function_map.py`.
- Contoh: `overlay_text_on_image` kini ada di `ai_tools/overlay_text.py`.
- Registry AI tools tersimpan di `ai_tools/registry.json`.

## 🛠️ Utils Modular

- Utility functions kini dipisah per domain:
  - `hashing.py`: Hash password
  - `pagination.py`: Pagination helper
  - `serializers.py`: Custom encoder & SQLAlchemy serialization
  - `response_helpers.py`: Helper untuk WebResponse

## 📋 Available Endpoints

### Health Check
- **GET** `/` - Root endpoint dengan informasi dasar
- **GET** `/api/v1/health/` - Health check endpoint

### Authentication
- **POST** `/api/v1/auth/login` - User login
- **POST** `/api/v1/auth/register` - User registration

### Training Data Management
- **GET** `/api/v1/training/queue` - Get training queue with pagination
- **PATCH** `/api/v1/training/{id}/user-prompt` - Update user prompt
- **PATCH** `/api/v1/training/hooks/{id}` - Update hook variant
- **PATCH** `/api/v1/training/scenes/{id}` - Update scene
- **GET** `/api/v1/training/export/jsonl` - Export training data to JSONL

### Review Management
- **GET** `/api/v1/review/summary` - Get review summary
- **POST** `/api/v1/review/approve` - Approve review
- **POST** `/api/v1/review/reject` - Reject review
- **POST** `/api/v1/review/skip` - Skip review

### API Documentation
- **GET** `/docs` - Swagger UI documentation
- **GET** `/redoc` - ReDoc documentation

## 🧪 Testing

Jalankan tests dengan pytest:
```bash
pytest
```

Jalankan tests dengan coverage:
```bash
pytest --cov=app
```

Jalankan tests untuk specific module:
```bash
pytest tests/api/ -v
pytest tests/services/ -v
```

## 🔧 Development

### Database Migration

1. Initialize Alembic (hanya sekali)
```bash
alembic init alembic
```

2. Create migration
```bash
alembic revision --autogenerate -m "Initial migration"
```

3. Apply migration
```bash
alembic upgrade head
```

4. Check migration status
```bash
alembic current
alembic history
```

### Adding New Features

1. Buat endpoint di `app/api/v1/endpoints/`
2. Tambah business logic di `app/services/`
3. Buat repository class di `app/repositories/`
4. Definisikan model di `app/models/` (jika perlu)
5. Buat schema di `app/schemas/`
6. Tambah tests di `tests/`
7. Tambah AI tool di `app/ai_tools/` jika perlu
8. Update dokumentasi di `docs/`
9. Update router di `app/api/v1/routers.py`

## 📚 Tech Stack

- **FastAPI** - Web framework
- **SQLAlchemy** - ORM
- **PostgreSQL** - Database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **Pytest** - Testing framework
- **Loguru** - Logging
- **Jose** - JWT handling
- **Alembic** - Database migrations
- **OpenAI** - AI integration
- **Pillow** - Image processing
- **Fal Client** - AI tools integration

## 🌍 Environment Variables

Buat file `.env` dengan konfigurasi environment variables yang diperlukan seperti:
- Database connection string
- JWT secret key
- API keys untuk AI tools
- Logging configuration
- CORS origins
- Environment (development/production)

## 📖 Documentation

- **API Documentation**: Lihat folder `docs/` untuk dokumentasi lengkap API
  - `training-api-docs.md` - Training data management API
  - `review-api-docs.md` - Review management API
  - `auth-api-spec.md` - Authentication API
  - `architecture.md` - Project architecture overview

## 📁 Generated Files

- **training.jsonl**: File export yang dihasilkan oleh endpoint `/api/v1/training/export/jsonl`
- **alembic/**: Folder untuk database migrations
- **tests/**: Folder untuk unit dan integration tests
- **tools/**: Standalone tools dan utilities
- **.github/**: GitHub workflows dan instructions

## 🗄️ Database Schema

### Core Tables
- **users**: User management dengan authentication
- **training_pairs**: Data training utama dengan hooks dan scenes
- **hashtags**: Tag system untuk kategorisasi
- **hook_variants**: Variasi hook dengan scene_number, scene_type, timestamp
- **scenes**: Scene content dengan text_overlay, voiceover, visual
- **review_actions**: Review tracking system
- **training_pair_hashtags**: Many-to-many relationship table

## 📄 License

MIT License

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Update documentation
6. Submit a pull request

## 📞 Support

Untuk pertanyaan atau dukungan, silakan buat issue di repository ini.
