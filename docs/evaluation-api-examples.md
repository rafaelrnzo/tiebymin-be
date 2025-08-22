# Evaluation API Examples

## Overview
Contoh penggunaan API evaluation dengan struktur tabel terbaru.

## Setup

### 1. Authentication
```bash
# Login untuk mendapatkan token
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'

# Response akan berisi access_token
{
  "status": "success",
  "message": "Login successful",
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "token_type": "bearer"
  }
}
```

## API Examples

### 1. Get Random Comparison Data
```bash
curl -X GET "http://localhost:8000/api/v1/evaluation/compare" \
  -H "Content-Type: application/json"
```

**Response:**
```json
{
  "status": "success",
  "message": "Comparison data retrieved successfully",
  "data": {
    "training_pair_set": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "pair_id": "PAIR001",
      "user_prompt": "Buat video tutorial tentang cara memasak nasi goreng",
      "system_prompt": "Anda adalah seorang chef profesional yang akan membuat video tutorial memasak",
      "created_at": "2024-01-15T10:30:00Z"
    },
    "baseline_training_pair": {
      "id": "550e8400-e29b-41d4-a716-446655440001",
      "training_pair_set_id": "550e8400-e29b-41d4-a716-446655440000",
      "ai_model_id": "550e8400-e29b-41d4-a716-446655440002",
      "prompt": "Buat video tutorial tentang cara memasak nasi goreng",
      "topic": "Cooking Tutorial",
      "category": "Food",
      "duration_seconds": 120,
      "score": 75,
      "target_audience": "Beginner cooks",
      "content_style": "Educational",
      "created_at": "2024-01-15T10:30:00Z",
      "generated_hook_variants": [
        {
          "id": "550e8400-e29b-41d4-a716-446655440003",
          "training_pair_id": "550e8400-e29b-41d4-a716-446655440001",
          "hook_variant": 1,
          "scene_number": 1,
          "scene_type": "hook",
          "timestamp": "00:00-00:05",
          "text_overlay": "Cara Masak Nasi Goreng",
          "voiceover": "Halo semua, hari ini saya akan mengajarkan cara memasak nasi goreng yang enak",
          "visual": "Chef standing in kitchen",
          "tip": "Pastikan nasi sudah dingin sebelum digoreng",
          "order_index": 1,
          "created_at": "2024-01-15T10:30:00Z"
        }
      ],
      "generated_scenes": [
        {
          "id": "550e8400-e29b-41d4-a716-446655440004",
          "training_pair_id": "550e8400-e29b-41d4-a716-446655440001",
          "scene_number": 2,
          "scene_type": "instruction",
          "timestamp": "00:05-00:15",
          "text_overlay": "Siapkan Bahan-bahan",
          "voiceover": "Pertama, siapkan semua bahan yang diperlukan",
          "visual": "Ingredients on table",
          "tip": "Gunakan bahan segar untuk hasil terbaik",
          "order_index": 2,
          "created_at": "2024-01-15T10:30:00Z"
        }
      ]
    },
    "fine_tuned_training_pair": {
      "id": "550e8400-e29b-41d4-a716-446655440005",
      "training_pair_set_id": "550e8400-e29b-41d4-a716-446655440000",
      "ai_model_id": "550e8400-e29b-41d4-a716-446655440006",
      "prompt": "Buat video tutorial tentang cara memasak nasi goreng",
      "topic": "Cooking Tutorial",
      "category": "Food",
      "duration_seconds": 120,
      "score": 85,
      "target_audience": "Beginner cooks",
      "content_style": "Educational",
      "created_at": "2024-01-15T10:30:00Z",
      "generated_hook_variants": [
        {
          "id": "550e8400-e29b-41d4-a716-446655440007",
          "training_pair_id": "550e8400-e29b-41d4-a716-446655440005",
          "hook_variant": 1,
          "scene_number": 1,
          "scene_type": "hook",
          "timestamp": "00:00-00:05",
          "text_overlay": "Nasi Goreng Spesial",
          "voiceover": "Hai teman-teman! Kali ini saya akan share resep nasi goreng yang bikin nagih",
          "visual": "Chef with wok",
          "tip": "Gunakan api besar untuk hasil yang lebih baik",
          "order_index": 1,
          "created_at": "2024-01-15T10:30:00Z"
        }
      ],
      "generated_scenes": [
        {
          "id": "550e8400-e29b-41d4-a716-446655440008",
          "training_pair_id": "550e8400-e29b-41d4-a716-446655440005",
          "scene_number": 2,
          "scene_type": "instruction",
          "timestamp": "00:05-00:15",
          "text_overlay": "Bahan-bahan yang Diperlukan",
          "voiceover": "Untuk membuat nasi goreng yang enak, kita perlu bahan-bahan berikut",
          "visual": "Close-up of ingredients",
          "tip": "Pilih beras yang sudah dingin dan tidak terlalu lembek",
          "order_index": 2,
          "created_at": "2024-01-15T10:30:00Z"
        }
      ]
    }
  }
}
```

### 2. Get Comparison with Specific Pair ID
```bash
curl -X GET "http://localhost:8000/api/v1/evaluation/compare?pair_id=PAIR001" \
  -H "Content-Type: application/json"
```

### 3. Get Comparison with Progress (Authenticated)
```bash
curl -X GET "http://localhost:8000/api/v1/evaluation/compare?include_progress=true" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
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
      "total_pairs": 50,
      "evaluated_pairs": 15,
      "remaining_pairs": 35,
      "progress_percentage": 30.0
    }
  }
}
```

### 4. Submit User Preference
```bash
curl -X POST "http://localhost:8000/api/v1/evaluation/preference" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "training_pair_set_id": "550e8400-e29b-41d4-a716-446655440000",
    "selected_training_pair_id": "550e8400-e29b-41d4-a716-446655440005",
    "preference_reason": "Fine-tuned model menghasilkan konten yang lebih engaging dan natural"
  }'
```

**Response:**
```json
{
  "status": "success",
  "message": "User preference submitted successfully",
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440009",
    "user_id": "550e8400-e29b-41d4-a716-446655440010",
    "training_pair_set_id": "550e8400-e29b-41d4-a716-446655440000",
    "selected_training_pair_id": "550e8400-e29b-41d4-a716-446655440005",
    "preference_reason": "Fine-tuned model menghasilkan konten yang lebih engaging dan natural",
    "created_at": "2024-01-15T11:00:00Z"
  }
}
```

### 5. Get User Preferences
```bash
curl -X GET "http://localhost:8000/api/v1/evaluation/preferences" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
{
  "status": "success",
  "message": "User preferences retrieved successfully",
  "data": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440009",
      "user_id": "550e8400-e29b-41d4-a716-446655440010",
      "training_pair_set_id": "550e8400-e29b-41d4-a716-446655440000",
      "selected_training_pair_id": "550e8400-e29b-41d4-a716-446655440005",
      "preference_reason": "Fine-tuned model menghasilkan konten yang lebih engaging dan natural",
      "created_at": "2024-01-15T11:00:00Z"
    },
    {
      "id": "550e8400-e29b-41d4-a716-446655440011",
      "user_id": "550e8400-e29b-41d4-a716-446655440010",
      "training_pair_set_id": "550e8400-e29b-41d4-a716-446655440012",
      "selected_training_pair_id": "550e8400-e29b-41d4-a716-446655440013",
      "preference_reason": "Baseline model lebih straightforward dan mudah dipahami",
      "created_at": "2024-01-15T12:00:00Z"
    }
  ]
}
```

### 6. Get Evaluation Progress
```bash
curl -X GET "http://localhost:8000/api/v1/evaluation/progress" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
{
  "status": "success",
  "message": "Evaluation progress retrieved successfully",
  "data": {
    "total_pairs": 50,
    "evaluated_pairs": 15,
    "remaining_pairs": 35,
    "progress_percentage": 30.0
  }
}
```

### 7. Get Evaluation Pair for UI
```bash
curl -X GET "http://localhost:8000/api/v1/evaluation/pair" \
  -H "Content-Type: application/json"
```

**Response:**
```json
{
  "status": "success",
  "message": "Evaluation pair data retrieved successfully",
  "data": {
    "training_pair_set": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "pair_id": "PAIR001",
      "user_prompt": "Buat video tutorial tentang cara memasak nasi goreng",
      "system_prompt": "Anda adalah seorang chef profesional yang akan membuat video tutorial memasak",
      "created_at": "2024-01-15T10:30:00Z"
    },
    "baseline_script": {
      // Same structure as baseline_training_pair
    },
    "fine_tuned_script": {
      // Same structure as fine_tuned_training_pair
    },
    "total_available_pairs": 50,
    "current_pair_index": 1
  }
}
```

## Error Handling Examples

### 404 Not Found
```bash
curl -X GET "http://localhost:8000/api/v1/evaluation/compare?pair_id=NONEXISTENT" \
  -H "Content-Type: application/json"
```

**Response:**
```json
{
  "detail": "Tidak ada data perbandingan yang ditemukan"
}
```

### 400 Bad Request
```bash
curl -X POST "http://localhost:8000/api/v1/evaluation/preference" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "training_pair_set_id": "invalid-uuid",
    "selected_training_pair_id": "550e8400-e29b-41d4-a716-446655440005"
  }'
```

**Response:**
```json
{
  "detail": "Failed to submit preference: Invalid UUID format"
}
```

### 401 Unauthorized
```bash
curl -X GET "http://localhost:8000/api/v1/evaluation/preferences" \
  -H "Content-Type: application/json"
```

**Response:**
```json
{
  "detail": "Not authenticated"
}
```

## Testing with Python

```python
import requests
import json

# Base URL
BASE_URL = "http://localhost:8000/api/v1"

# Login
def login(username, password):
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "username": username,
        "password": password
    })
    return response.json()["data"]["access_token"]

# Get comparison data
def get_comparison(pair_id=None, include_progress=False, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    params = {}
    if pair_id:
        params["pair_id"] = pair_id
    if include_progress:
        params["include_progress"] = "true"
    
    response = requests.get(f"{BASE_URL}/evaluation/compare", headers=headers, params=params)
    return response.json()

# Submit preference
def submit_preference(training_pair_set_id, selected_training_pair_id, preference_reason=None, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    data = {
        "training_pair_set_id": training_pair_set_id,
        "selected_training_pair_id": selected_training_pair_id
    }
    if preference_reason:
        data["preference_reason"] = preference_reason
    
    response = requests.post(f"{BASE_URL}/evaluation/preference", headers=headers, json=data)
    return response.json()

# Usage example
if __name__ == "__main__":
    # Login
    token = login("your_username", "your_password")
    
    # Get random comparison
    comparison = get_comparison(include_progress=True, token=token)
    print("Comparison:", json.dumps(comparison, indent=2))
    
    # Submit preference
    if comparison["status"] == "success":
        data = comparison["data"]["comparison"]
        training_pair_set_id = data["training_pair_set"]["id"]
        fine_tuned_id = data["fine_tuned_training_pair"]["id"]
        
        preference = submit_preference(
            training_pair_set_id=training_pair_set_id,
            selected_training_pair_id=fine_tuned_id,
            preference_reason="Fine-tuned model lebih baik",
            token=token
        )
        print("Preference:", json.dumps(preference, indent=2))
```

## Notes

1. **Authentication**: Beberapa endpoint memerlukan autentikasi, pastikan untuk menyertakan token Bearer
2. **UUID Format**: Semua ID menggunakan format UUID
3. **Error Handling**: Selalu periksa response status dan handle error dengan baik
4. **Progress Tracking**: Progress hanya tersedia untuk user yang terautentikasi
5. **Data Consistency**: Pastikan data training pair set dan generated training pairs sudah sesuai dengan struktur baru 