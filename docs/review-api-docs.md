# Review API Documentation

## Authentication

Seluruh endpoint di bawah ini membutuhkan autentikasi JWT (Bearer Token) pada header:

```
Authorization: Bearer <token>
```

---

## 1. Get Review Summary

- **Endpoint:** `GET /summary`
- **Description:** Mengambil ringkasan status review milik user yang sedang login.

### Request

```http
GET /summary HTTP/1.1
Host: <base_url>
Authorization: Bearer <token>
```

### Response

```json
{
  "total": 10,
  "approved": 5,
  "rejected": 3,
  "skipped": 2
}
```

| Field     | Type    | Description                |
|-----------|---------|---------------------------|
| total     | int     | Total review              |
| approved  | int     | Jumlah review disetujui   |
| rejected  | int     | Jumlah review ditolak     |
| skipped   | int     | Jumlah review dilewati    |

---

## 2. Approve Review

- **Endpoint:** `POST /approve`
- **Description:** Menyetujui sebuah review.

### Request

```http
POST /approve HTTP/1.1
Host: <base_url>
Authorization: Bearer <token>
Content-Type: application/json

{
  "review_id": 123,
  "note": "Good job"
}
```

| Field      | Type    | Required | Description                |
|------------|---------|----------|----------------------------|
| review_id  | int     | Yes      | ID review yang di-approve  |
| note       | string  | No       | Catatan tambahan           |

### Response

```json
{
  "id": 1,
  "review_id": 123,
  "action": "APPROVED",
  "note": "Good job",
  "user_id": 5,
  "created_at": "2024-06-07T12:34:56"
}
```

| Field      | Type      | Description                |
|------------|-----------|---------------------------|
| id         | int       | ID aksi                   |
| review_id  | int       | ID review                 |
| action     | string    | "APPROVED"                |
| note       | string    | Catatan                   |
| user_id    | int       | ID user                   |
| created_at | datetime  | Waktu aksi                |

---

## 3. Reject Review

- **Endpoint:** `POST /reject`
- **Description:** Menolak sebuah review.

### Request

```http
POST /reject HTTP/1.1
Host: <base_url>
Authorization: Bearer <token>
Content-Type: application/json

{
  "review_id": 123,
  "note": "Kurang lengkap"
}
```

### Response

```json
{
  "id": 2,
  "review_id": 123,
  "action": "REJECTED",
  "note": "Kurang lengkap",
  "user_id": 5,
  "created_at": "2024-06-07T12:35:00"
}
```

---

## 4. Skip Review

- **Endpoint:** `POST /skip`
- **Description:** Melewati sebuah review (tidak approve/tolak).

### Request

```http
POST /skip HTTP/1.1
Host: <base_url>
Authorization: Bearer <token>
Content-Type: application/json

{
  "review_id": 123,
  "note": "Bukan bidang saya"
}
```

### Response

```json
{
  "id": 3,
  "review_id": 123,
  "action": "SKIPPED",
  "note": "Bukan bidang saya",
  "user_id": 5,
  "created_at": "2024-06-07T12:35:10"
}
```

---

## Catatan

- Semua endpoint POST (`/approve`, `/reject`, `/skip`) menggunakan request body yang sama.
- Field `note` pada request body bersifat opsional.
- Semua response untuk approve, reject, dan skip memiliki struktur yang sama, hanya berbeda pada nilai `action`. 