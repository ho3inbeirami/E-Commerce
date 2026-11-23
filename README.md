# 🛒 E-Commerce

An e-commerce project with a Products REST API, fully dockerized and served on port **8000**.

---

## 📑 Table of Contents

- [Features](#-features)
- [Getting Started with Docker](#-getting-started-with-docker)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [Author](#-author)

---

## ✨ Features

- Products REST API (create, read, update, delete)
- Fully dockerized: run the whole project with a single command
- Served on port `8000`

## 🐳 Getting Started with Docker

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/) (included with Docker Desktop)
- Git

### Run the project

1. **Clone the repository**

   ```bash
   git clone https://github.com/ho3inbeirami/E-Commerce.git
   cd E-Commerce
   ```

2. **Build and start the containers**

   ```bash
   docker compose up --build
   ```

   To run in the background:

   ```bash
   docker compose up --build -d
   ```

3. **Open the app**

   The project is now available at: **http://localhost:8000**

### Useful Docker commands

```bash
# View logs
docker compose logs -f

# Stop the containers
docker compose down

# Stop and remove volumes (resets the database)
docker compose down -v
```

---

## 📡 API Documentation

Base URL: `http://localhost:8000`

All requests and responses use JSON.

### Products

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | `/products`      | List all products      |
| GET    | `/products/:id`  | Get a single product   |
| POST   | `/products`      | Create a new product   |
| PUT    | `/products/:id`  | Update a product       |
| DELETE | `/products/:id`  | Delete a product       |

> Adjust the paths above if your routes use a prefix such as `/api/products`.

#### Product object

```json
{
  "id": 1,
  "name": "Wireless Headphones",
  "description": "Bluetooth over-ear headphones",
  "price": 59.99,
  "stock": 25
}
```

#### Examples

**Get all products**

```bash
curl http://localhost:8000/products
```

**Get one product**

```bash
curl http://localhost:8000/products/1
```

**Create a product**

```bash
curl -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Wireless Headphones", "description": "Bluetooth over-ear headphones", "price": 59.99, "stock": 25}'
```

**Update a product**

```bash
curl -X PUT http://localhost:8000/products/1 \
  -H "Content-Type: application/json" \
  -d '{"price": 49.99, "stock": 30}'
```

**Delete a product**

```bash
curl -X DELETE http://localhost:8000/products/1
```

#### Status codes

| Status | Meaning                        |
|--------|--------------------------------|
| 200    | Success                        |
| 201    | Product created                |
| 400    | Bad request / validation error |
| 404    | Product not found              |
| 500    | Server error                   |

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m "Add amazing feature"`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request


## 👤 Author

**Hossein Beirami**
GitHub: [@ho3inbeirami](https://github.com/ho3inbeirami)
