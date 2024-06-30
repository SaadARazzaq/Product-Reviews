# Product-Reviews 📝

This project demonstrates a FastAPI application using Beanie ODM (Object Document Mapper) for MongoDB. The project is containerized using Docker and Docker Compose for easy setup and deployment.

## Project Structure 🧱

<img width="574" alt="Screenshot 2024-06-30 at 4 02 42 AM" src="https://github.com/SaadARazzaq/Product-Reviews-API/assets/123338307/c2d6ed5e-f235-4186-886e-4b545b3ca95e">
<img width="275" alt="Screenshot 2024-06-30 at 3 57 41 AM" src="https://github.com/SaadARazzaq/Product-Reviews-API/assets/123338307/84f21262-6c58-48ad-a3b3-6c0f74112544">
- **app/server/models/product_review.py**: Defines the `ProductReview` and `UpdateProductReview` models using `Beanie` and `Pydantic`.
- **app/server/routes/product_review.py**: Contains the `API routes` for handling product reviews.
- **app/server/app.py**: The main `FastAPI` application setup, including `route inclusion` and `database initialization`.
- **app/server/database.py**: Contains the `database initialization logic`.
- **main.py**: The entry point for running the `Uvicorn server`.
- **Dockerfile**: The `Dockerfile` for building the FastAPI application image.
- **docker-compose.yml**: `Docker Compose file` for setting up the `FastAPI` and `MongoDB services`.
- **requirements.txt**: Python dependencies required for the project.

## Getting Started 🏃

### Prerequisites 📋

- `Docker Desktop` installed and up and running on your machine.

### Installation 🛠️

1. Clone the repository:

    ```sh
    git clone https://github.com/SaadARazzaq/Product-Reviews-API
    cd fastapi-beanie
    ```

2. Build and start the Docker containers:

    ```sh
    docker-compose up --build
    ```

3. The FastAPI application will be available at `http://localhost:8000`.

### API Endpoints ⚡

<img width="1171" alt="Screenshot 2024-06-30 at 4 08 40 AM" src="https://github.com/SaadARazzaq/Product-Reviews-API/assets/123338307/a29067cd-7627-4846-ab34-fcda264f73fb">

### Example Product Review Model Schema 🧩

```json
{
    "name": "Saad Abdur Razzaq",
    "title": "MacBook Air M2",
    "rating": 5.0,
    "review": "Best Laptop in the world",
    "date": "2023-06-30T12:34:56.789Z"
}
```

### Example Update Product Review Model Schema 🧩

```json
{
    "name": "Taha Abdur Razzaq",
    "title": "HP Victus 16",
    "rating": 5.0,
    "review": "Worst Laptop in the world",
    "date": "2023-06-30T12:34:56.789Z"
}
```

### Notes 📒

- Ensure MongoDB is running and accessible for the FastAPI application to function correctly.
- The mongo_url in app/server/database.py is set to connect to a MongoDB instance at host.docker.internal.

---

```bash
This project was made with 💖 by Saad Abdur Razzaq
```
