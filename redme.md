
# Inventory Management API Documentation

## Overview
This document provides an overview of the Inventory Management API using Postman. It includes endpoints for user authentication, item creation, retrieval, update, and deletion.


## Endpoints

### 1. User Token Generation
- **Endpoint**: `http://127.0.0.1:8000/api/user/token/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "ajith@gmail.com",
    "password": "ajith"
  }
  ```

### 2. Create Item
- **Endpoint**: `http://127.0.0.1:8000/api/items/create/`
- **Method**: `POST`
- **Authorization**: Bearer token required
- **Headers**:
  - `Authorization: Bearer <JWT_TOKEN>`
  - `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "name": "Sample Item 1",
    "description": "This is a description of the sample item 1."
  }
  ```

### 3. Get Item by ID
- **Endpoint**: `http://127.0.0.1:8000/api/items/<id>/`
- **Method**: `GET`
- **Authorization**: Bearer token required
- **Headers**:
  - `Authorization: Bearer <JWT_TOKEN>`
  - `Content-Type: application/json`

### 4. Delete Item by ID
- **Endpoint**: `http://127.0.0.1:8000/api/items/<id>/`
- **Method**: `DELETE`
- **Authorization**: Bearer token required
- **Headers**:
  - `Authorization: Bearer <JWT_TOKEN>`
  - `Content-Type: application/json`

### 5. Update Item by ID
- **Endpoint**: `http://127.0.0.1:8000/api/items/<id>/`
- **Method**: `PUT` (assumed from the context)
- **Authorization**: Bearer token required
- **Headers**:
  - `Authorization: Bearer <JWT_TOKEN>`
  - `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "name": "update Sample Item 4",
    "description": "update This is a description of the sample item 4."
  }
  ```

### 6. Create User
- **Endpoint**: `http://127.0.0.1:8000/api/user/create/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "jane_doe",
    "email": "jane.doe@example.com",
    "first_name": "Jane",
    "last_name": "Doe",
    "password": "password123"
  }
  ```

## Notes
- Replace `<JWT_TOKEN>` with the actual token generated during user authentication.
- Use the correct item ID when making requests to retrieve, update, or delete items.

## Conclusion
This document serves as a guide to using the Inventory Management API through Postman, allowing you to manage user accounts and inventory items effectively.
```

You can save this content in a `.md` file, and it will format correctly for Markdown viewers.