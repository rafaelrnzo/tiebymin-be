# Evaluation API Documentation

## Overview
API untuk evaluasi model AI dengan perbandingan antara baseline dan fine-tuned model menggunakan struktur tabel terbaru.

## Endpoints

### 1. Get Comparison Data
**GET** `/api/v1/evaluation/compare`

Endpoint untuk mendapatkan data perbandingan antara baseline dan fine-tuned model.

**Query Parameters:**
- `pair_id` (optional): Pair ID spesifik untuk evaluasi. Jika tidak diberikan, akan mengambil secara random
- `include_progress` (optional): Apakah menyertakan informasi progress evaluasi (default: false)

**Example Requests:**

```bash
# Get random comparison data
GET /api/v1/evaluation/compare

# Get comparison with specific pair_id
GET /api/v1/evaluation/compare?pair_id=PAIR001

# Get comparison with progress (requires authentication)
GET /api/v1/evaluation/compare?include_progress=true
```

**Response:**
```json
{
  "status": "success",
  "message": "Comparison data retrieved successfully",
  "data": {
    "training_pair_set": {
      "id": "uuid",
      "pair_id": "PAIR001",
      "user_prompt": "string",
      "system_prompt": "string",
      "created_at": "datetime"
    },
    "baseline_training_pair": {
      "id": "uuid",
      "training_pair_set_id": "uuid",
      "ai_model_id": "uuid",
      "prompt": "string",
      "topic": "string",
      "category": "string",
      "duration_seconds": 60,
      "score": 75,
      "target_audience": "string",
      "content_style": "string",
      "created_at": "datetime",
      "generated_hook_variants": [...],
      "generated_scenes": [...]
    },
    "fine_tuned_training_pair": {
      // Same structure as baseline_training_pair
    }
  }
}
```

**Response with Progress:**
```json
{
  "status": "success",
  "message": "Comparison data retrieved successfully with progress",
  "data": {
    "comparison": {
      "training_pair_set": {...},
      "baseline_training_pair": {...},
      "fine_tuned_training_pair": {...}
    },
    "progress": {
      "total_pairs": 100,
      "evaluated_pairs": 25,
      "remaining_pairs": 75,
      "progress_percentage": 25.0
    }
  }
}
```

### 2. Submit User Preference
**POST** `/api/v1/evaluation/preference`

Endpoint untuk menyimpan preferensi user untuk training pair tertentu.

**Request Body:**
```json
{
  "training_pair_set_id": "uuid",
  "selected_training_pair_id": "uuid",
  "preference_reason": "string (optional)"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "User preference submitted successfully",
  "data": {
    "id": "uuid",
    "user_id": "uuid (optional)",
    "training_pair_set_id": "uuid",
    "selected_training_pair_id": "uuid",
    "preference_reason": "string",
    "created_at": "datetime"
  }
}
```

### 3. Get User Preferences
**GET** `/api/v1/evaluation/preferences`

Endpoint untuk mendapatkan semua preferensi user (requires authentication).

**Response:**
```json
{
  "status": "success",
  "message": "User preferences retrieved successfully",
  "data": [
    {
      "id": "uuid",
      "user_id": "uuid",
      "training_pair_set_id": "uuid",
      "selected_training_pair_id": "uuid",
      "preference_reason": "string",
      "created_at": "datetime"
    }
  ]
}
```

### 4. Get Evaluation Progress
**GET** `/api/v1/evaluation/progress`

Endpoint untuk mendapatkan progress evaluasi user (requires authentication).

**Response:**
```json
{
  "status": "success",
  "message": "Evaluation progress retrieved successfully",
  "data": {
    "total_pairs": 100,
    "evaluated_pairs": 25,
    "remaining_pairs": 75,
    "progress_percentage": 25.0
  }
}
```

### 5. Get Evaluation Pair for UI
**GET** `/api/v1/evaluation/pair`

Endpoint untuk mendapatkan data evaluasi untuk UI dengan informasi tambahan.

**Query Parameters:**
- `pair_id` (optional): Pair ID spesifik untuk evaluasi. Jika tidak diberikan, akan mengambil secara random

**Response:**
```json
{
  "status": "success",
  "message": "Evaluation pair data retrieved successfully",
  "data": {
    "training_pair_set": {
      "id": "uuid",
      "pair_id": "PAIR001",
      "user_prompt": "string",
      "system_prompt": "string",
      "created_at": "datetime"
    },
    "baseline_script": {
      // Same structure as baseline_training_pair
    },
    "fine_tuned_script": {
      // Same structure as fine_tuned_training_pair
    },
    "total_available_pairs": 100,
    "current_pair_index": 1
  }
}
```

## Database Schema

### Training Pair Sets (Parent Table)
- `id`: UUID (Primary Key)
- `pair_id`: String(20) (Unique)
- `user_prompt`: Text
- `system_prompt`: Text
- `created_at`: DateTime
- `created_by`: String(100)
- `updated_at`: DateTime
- `updated_by`: String(100)
- `deleted_at`: DateTime

### Generated Training Pairs (Child Table)
- `id`: UUID (Primary Key)
- `training_pair_set_id`: UUID (Foreign Key to training_pair_sets)
- `ai_model_id`: UUID (Foreign Key to ai_models)
- `prompt`: Text (NOT NULL)
- `topic`: String(255)
- `category`: String(255)
- `duration_seconds`: Integer
- `score`: Integer
- `target_audience`: String(255)
- `content_style`: String(255)
- `created_at`: DateTime
- `created_by`: String(100)
- `updated_at`: DateTime
- `updated_by`: String(100)
- `deleted_at`: DateTime

### User Preferences
- `id`: UUID (Primary Key)
- `user_id`: UUID (Foreign Key to users, SET NULL on delete)
- `training_pair_set_id`: UUID (Foreign Key to training_pair_sets, CASCADE on delete)
- `selected_training_pair_id`: UUID (Foreign Key to generated_training_pairs, CASCADE on delete)
- `preference_reason`: Text
- `created_at`: DateTime
- `created_by`: String(100)
- `updated_at`: DateTime
- `updated_by`: String(100)
- `deleted_at`: DateTime

## Error Responses

### 404 Not Found
```json
{
  "detail": "Tidak ada data perbandingan yang ditemukan"
}
```

### 400 Bad Request
```json
{
  "detail": "Failed to submit preference: [error message]"
}
```

### 401 Unauthorized
```json
{
  "detail": "Not authenticated"
}
```

## Authentication

- Endpoints `/preferences` dan `/progress` memerlukan autentikasi
- Endpoints `/compare` dan `/preference` dapat diakses tanpa autentikasi, tetapi progress hanya akan disertakan jika user terautentikasi
- Endpoint `/pair` dapat diakses tanpa autentikasi 