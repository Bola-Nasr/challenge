# W&D Challenge

## Overview

This project is application that enables users to search for properties in a database with advanced filters. Users can log in, search properties, view results on a map, and navigate through paginated results. The application is containerized using Docker for consistent deployment.

---

## Features

- **User Authentication**: Basic login functionality with pre-defined credentials (`admin/admin`).
- **Property Search**: Advanced search functionality with filters like address, class description, market value, building use, and size.
- **Sorting**: Results can be sorted by market value or square footage in ascending or descending order.
- **Map View**: Interactive map displaying property locations with clickable markers.
- **Pagination**: Efficient pagination for managing large datasets.
- **Performance Optimizations**: Asynchronous backend processing and efficient database queries.

---

## Technology Stack

### Backend: FastAPI
- **Features**:
  - High performance through asynchronous capabilities.
  - Automatic interactive API documentation (Swagger & ReDoc).
  - Scalable architecture for handling multiple concurrent requests.
- **Tools**: SQLAlchemy for ORM, SQLite for database, and Pydantic for validation.

### Frontend: Vue.js
- **Features**:
  - Reactive and component-based architecture.
  - Lightweight framework with excellent performance.
  - Rich ecosystem for seamless development.
  - Easy integration with APIs using Axios.

### Containerization: Docker
- **Advantages**:
  - Simplifies deployment with consistent environments.
  - Ensures compatibility across development, staging, and production environments.

---

## Requirements

### Backend:
- Python 3.8+
- FastAPI
- SQLAlchemy
- SQLite (or another database)
- Uvicorn (ASGI server)
- Docker

### Frontend:
- Node.js 14+
- Vue.js 3.x
- Axios

---

## Installation Instructions

### Clone the Repository
1. Clone the repository to your local machine:
   ```bash
   git clone git@github.com:Bola-Nasr/challenge.git
   cd challenge
   
# Using Docker Compose
2. Start the application:
   ```bash
   
   cd backend && python3 load_data.py
   cd .. && docker-compose up --build
   
3. Open your browser:

    Frontend: http://localhost

    Backend API: http://localhost:8000/docs (Swagger API docs)

# Using Script
2. Run the provided script:
    ```bash
   ./run.sh
   
3. Open your browser:

   Frontend: http://localhost

   Backend API: http://localhost:8000/docs (Swagger API docs)

## Additional Information
- **Database Initialization:** The database is initialized using data from a provided Excel file. This step is manual and should be done before running the application.
- **Pagination:** The backend API supports pagination using query parameters like `limit` and `offset`.
---

## Optimization Suggestions
- **Database Indexing:** Add indexes to frequently queried fields to improve search performance.
- **Caching:** Use caching (e.g., Redis) for frequently accessed data to reduce load times.
- **Load Balancing:** Add a load balancer to distribute traffic across multiple backend instances.
- **Static Files:** Ensure static assets are served with long-term caching headers.
- **Security:** Implement HTTPS, rate limiting, and input validation to enhance security.