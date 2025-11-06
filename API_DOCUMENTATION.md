
# API Documentation

This document provides details on the available API endpoints.

## Authentication

Authentication is handled using JSON Web Tokens (JWT). A successful login will return an `access_token` which must be included in the `Authorization` header for all subsequent requests to protected endpoints.

**Header Format:**

`Authorization: Bearer <access_token>`

<br>

## Login Endpoint

### POST `/api/login`

This endpoint authenticates a user and returns a JWT access token upon successful login.

#### Request Body

The request body must be a JSON object containing the user's credentials.

| Parameter  | Type   | Description        | Required |
| :--------- | :----- | :----------------- | :------- |
| `username` | string | The user's username. | Yes      |
| `password` | string | The user's password. | Yes      |

**Example Request:**

```bash
curl -X POST   http://localhost:8080/api/login   -H 'Content-Type: application/json'   -d '{
        "username": "test",
        "password": "test"
      }'
```

---

#### Responses

**`200 OK` - Successful Login**

Returns a JSON object containing the access token.

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**`401 Unauthorized` - Invalid Credentials**

Returns an error message if the username or password is incorrect.

```json
{
  "msg": "Bad username or password"
}
```

---
