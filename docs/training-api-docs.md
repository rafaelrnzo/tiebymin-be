# Training API Documentation

## Authentication

> Semua endpoint di bawah ini membutuhkan autentikasi JWT (Bearer Token) pada header `Authorization`.

---

## Get Training Queue (Paginated)

**Endpoint:**  
`GET /api/v1/training/queue`

**Deskripsi:**  
Mengambil daftar training pairs dengan dukungan paginasi.

**Query Parameters:**
- `page` (int, default: 1): Nomor halaman (mulai dari 1)
- `size` (int, default: 10, min: 1, max: 100): Jumlah item per halaman

**Response:**
```json
{
  "code": 200,
  "status": "OK",
  "data": [
    {
      "id": "UUID",
      "pair_id": "string",
      "topic": "string",
      "category": "string",
      "duration_seconds": 120,
      "score": 90,
      "user_prompt": "string",
      "system_prompt": "string",
      "target_audience": "string",
      "content_style": "string",
      "created_at": "2024-06-01T12:00:00Z",
      "created_by": "string",
      "updated_at": "2024-06-01T12:00:00Z",
      "updated_by": "string",
      "hashtags": [
        {
          "id": "UUID",
          "name": "string",
          "created_at": "2024-06-01T12:00:00Z",
          "created_by": "string",
          "updated_at": "2024-06-01T12:00:00Z",
          "updated_by": "string"
        }
      ],
      "hook_variants": [
        {
          "id": "UUID",
          "hook_variant": 1,
          "scene_number": 1,
          "scene_type": "Hook",
          "timestamp": "0-3s",
          "text_overlay": "string",
          "voiceover": "string",
          "visual": "string",
          "tip": "string",
          "order_index": 1,
          "created_at": "2024-06-01T12:00:00Z",
          "created_by": "string",
          "updated_at": "2024-06-01T12:00:00Z",
          "updated_by": "string"
        }
      ],
      "scenes": [
        {
          "id": "UUID",
          "scene_number": 2,
          "scene_type": "Main Content",
          "timestamp": "3-30s",
          "text_overlay": "string",
          "voiceover": "string",
          "visual": "string",
          "tip": "string",
          "order_index": 1,
          "created_at": "2024-06-01T12:00:00Z",
          "created_by": "string",
          "updated_at": "2024-06-01T12:00:00Z",
          "updated_by": "string"
        }
      ]
    }
  ],
  "paging": {
    "page": 1,
    "size": 10,
    "totalItems": 100,
    "totalPages": 10
  }
}
```

---

## Struktur Data

### TrainingPairOut
- `id`: UUID
- `pair_id`: string
- `topic`: string | null
- `category`: string | null
- `duration_seconds`: int | null
- `score`: int | null
- `user_prompt`: string | null
- `system_prompt`: string | null
- `target_audience`: string | null
- `content_style`: string | null
- `created_at`, `created_by`, `updated_at`, `updated_by`: audit fields
- `hashtags`: array of HashtagOut
- `hook_variants`: array of HookVariantOut
- `scenes`: array of SceneOut

### HookVariantOut
- `id`: UUID
- `hook_variant`: int | null - Nomor varian hook
- `scene_number`: int | null - Nomor scene
- `scene_type`: string | null - Jenis scene (Hook, Main Content, dll)
- `timestamp`: string | null - Timestamp scene (misal: "0-3s")
- `text_overlay`: string | null - Teks overlay untuk scene
- `voiceover`: string | null - Voiceover hook
- `visual`: string | null - Visual/gambar untuk scene
- `tip`: string | null - Tips untuk hook
- `order_index`: int | null - Urutan dalam training pair
- `created_at`, `created_by`, `updated_at`, `updated_by`: audit fields

### SceneOut
- `id`: UUID
- `scene_number`: int | null - Nomor scene
- `scene_type`: string | null - Jenis scene (Hook, Main Content, dll)
- `timestamp`: string | null - Timestamp scene (misal: "3-30s")
- `text_overlay`: string | null - Teks overlay untuk scene
- `voiceover`: string | null - Voiceover scene
- `visual`: string | null - Visual/gambar untuk scene
- `tip`: string | null - Tips untuk scene
- `order_index`: int | null - Urutan dalam training pair
- `created_at`, `created_by`, `updated_at`, `updated_by`: audit fields

### Paging
- `page`: int
- `size`: int
- `totalItems`: int
- `totalPages`: int

--- 

### Update User Prompt pada Training Data

- **Endpoint:** `PATCH /api/v1/training/{training_pair_id}/user-prompt`
- **Description:** Mengubah field `user_prompt` pada data training tertentu.
- **Auth:** Wajib (Bearer Token)

#### Request

```http
PATCH /api/v1/training/{training_pair_id}/user-prompt HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{
  "user_prompt": "Prompt baru dari user"
}
```

| Field        | Type   | Required | Description                |
|--------------|--------|----------|----------------------------|
| user_prompt  | string | Yes      | Prompt baru dari user      |

#### Response

```json
{
  "id": "uuid",
  "pair_id": "string",
  "topic": "string",
  "category": "string",
  "duration_seconds": 60,
  "score": 90,
  "user_prompt": "Prompt baru dari user",
  "system_prompt": "string",
  "target_audience": "string",
  "content_style": "string",
  "created_at": "2024-06-07T12:34:56",
  "created_by": "username",
  "updated_at": "2024-06-07T13:00:00",
  "updated_by": "username",
  "hashtags": [ ... ],
  "hook_variants": [ ... ],
  "scenes": [ ... ]
}
```

#### Error

- **400 Bad Request**: Jika `user_prompt` tidak diisi.
- **404 Not Found**: Jika `training_pair_id` tidak ditemukan. 

---

### Update Hook Variant

- **Endpoint:** `PATCH /api/v1/training/hooks/{hook_variant_id}`
- **Description:** Mengubah data hook variant (hook_variant, scene_number, scene_type, timestamp, text_overlay, voiceover, visual, tip) pada training data.
- **Auth:** Wajib (Bearer Token)

#### Request

```http
PATCH /api/v1/training/hooks/{hook_variant_id} HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{
  "hook_variant": 1,
  "scene_number": 1,
  "scene_type": "Hook",
  "timestamp": "0-3s",
  "text_overlay": "string (optional)",
  "voiceover": "string (optional)",
  "visual": "string (optional)",
  "tip": "string (optional)"
}
```

| Field        | Type   | Required | Description                    |
|--------------|--------|----------|--------------------------------|
| hook_variant | int    | No       | Nomor varian hook              |
| scene_number | int    | No       | Nomor scene                    |
| scene_type   | string | No       | Jenis scene (Hook, Main Content, dll) |
| timestamp    | string | No       | Timestamp scene (misal: "0-3s") |
| text_overlay | string | No       | Teks overlay untuk scene       |
| voiceover    | string | No       | Voiceover hook                 |
| visual       | string | No       | Visual/gambar untuk scene      |
| tip          | string | No       | Tips untuk hook                |

#### Response

```json
{
  "id": "uuid",
  "hook_variant": 1,
  "scene_number": 1,
  "scene_type": "Hook",
  "timestamp": "0-3s",
  "text_overlay": "string",
  "voiceover": "string",
  "visual": "string",
  "tip": "string",
  "order_index": 1,
  "created_at": "2024-06-07T12:34:56",
  "created_by": "username",
  "updated_at": "2024-06-07T13:00:00",
  "updated_by": "username"
}
```

#### Error

- **404 Not Found**: Jika `hook_variant_id` tidak ditemukan. 

---

### Update Scene

- **Endpoint:** `PATCH /api/v1/training/scenes/{scene_id}`
- **Description:** Mengubah data scene (scene_number, scene_type, timestamp, text_overlay, voiceover, visual, tip) pada training data.
- **Auth:** Wajib (Bearer Token)

#### Request

```http
PATCH /api/v1/training/scenes/{scene_id} HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{
  "scene_number": 2,
  "scene_type": "Main Content",
  "timestamp": "3-30s",
  "text_overlay": "string (optional)",
  "voiceover": "string (optional)",
  "visual": "string (optional)",
  "tip": "string (optional)"
}
```

| Field        | Type   | Required | Description                    |
|--------------|--------|----------|--------------------------------|
| scene_number | int    | No       | Nomor scene                    |
| scene_type   | string | No       | Jenis scene (Hook, Main Content, dll) |
| timestamp    | string | No       | Timestamp scene (misal: "3-30s") |
| text_overlay | string | No       | Teks overlay untuk scene       |
| voiceover    | string | No       | Voiceover scene                |
| visual       | string | No       | Visual/gambar untuk scene      |
| tip          | string | No       | Tips untuk scene               |

#### Response

```json
{
  "id": "uuid",
  "scene_number": 2,
  "scene_type": "Main Content",
  "timestamp": "3-30s",
  "text_overlay": "string",
  "voiceover": "string",
  "visual": "string",
  "tip": "string",
  "order_index": 1,
  "created_at": "2024-06-07T12:34:56",
  "created_by": "username",
  "updated_at": "2024-06-07T13:00:00",
  "updated_by": "username"
}
```

#### Error

- **404 Not Found**: Jika `scene_id` tidak ditemukan. 

---

### Export Training Data (Download JSONL)

- **Endpoint:** `GET /api/v1/training/export/jsonl`
- **Description:** Mengekspor seluruh data training (status APPROVED) ke file JSONL dan langsung mengunduh file tersebut.
- **Auth:** Wajib (Bearer Token)

#### Request

```http
GET /api/v1/training/export/jsonl HTTP/1.1
Authorization: Bearer <token>
```

#### Response
- **200 OK**
- **Content-Type:** application/jsonl
- **Attachment:** File `training.jsonl` berisi satu objek per baris, contoh:

```jsonl
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "{\"type\":\"video_script\",\"data\":{\"hooks\":[{\"hook_variant\":1,\"scene_number\":1,\"scene_type\":\"Hook\",\"timestamp\":\"0-3s\",\"text_overlay\":\"...\",\"voiceover\":\"...\",\"visual\":\"...\",\"tip\":\"...\"}],\"script_body\":[{\"scene_number\":2,\"scene_type\":\"Main Content\",\"timestamp\":\"3-30s\",\"text_overlay\":\"...\",\"voiceover\":\"...\",\"visual\":\"...\",\"tip\":\"...\"}]}}"}]}
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "{\"type\":\"video_script\",\"data\":{\"hooks\":[...],\"script_body\":[...]}}"}]}
```

#### Error
- **401 Unauthorized**: Jika tidak login.
- **500 Internal Server Error**: Jika terjadi error saat export. 