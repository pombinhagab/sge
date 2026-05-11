# Stock Management System (SGE) Technical Documentation

## 1. Introduction

The Stock Management System (SGE) is a web application developed using Django and Django REST Framework, designed to manage products, suppliers, categories, brands, stock inflows, and outflows. The application offers an administrative interface, RESTful API functionalities, and a dashboard with stock and sales metrics.

## 2. Technologies Used

The SGE application is built with the following technologies:

| Technology | Version |
|---|---|
| Python | 3.13.2 |
| Django | 6.0.4 |
| Django REST Framework | 3.17.1 |
| Django REST Framework Simple JWT | 5.5.1 |
| PostgreSQL | 17 |
| Docker | Latest |
| Docker Compose | Latest |
| openpyxl | 3.1.5 |
| psycopg2-binary | 2.9.12 |
| python-dotenv | 1.2.2 |

## 3. Project Structure

The project structure follows the standard Django application pattern, with modules (`apps`) dedicated to specific functionalities. Below is an overview of the main directories and files:

```
/sge
├── app/                  # Global settings, main URLs, views, and dashboard metrics
├── authentication/       # JWT authentication module
├── brands/               # Module for brand management
├── categories/           # Module for category management
├── inflows/              # Module for stock inflow management
├── outflows/             # Module for stock outflow management
├── products/             # Module for product management
├── suppliers/            # Module for supplier management
├── Dockerfile            # Docker image definition for the application
├── docker-compose.yml    # Docker Compose configuration for service orchestration
├── manage.py             # Django command-line utility
├── requirements.txt      # Project dependencies
├── requirements_dev.txt  # Development dependencies
└── .env                  # Environment variables (not versioned)
```

## 4. Core Functionalities

### 4.1. Authentication

The system uses JWT (JSON Web Tokens) based authentication via `djangorestframework_simplejwt`. The API endpoints for authentication are:

*   `api/v1/authentication/token/`: Obtain access and refresh tokens.
*   `api/v1/authentication/token/refresh/`: Renew access token.
*   `api/v1/authentication/token/verify/`: Verify token validity.

Additionally, the application includes login and logout views based on Django's default authentication system.

### 4.2. Product Management

The products module (`products`) is central to the SGE, allowing for comprehensive management of stock items. Functionalities include:

*   **Full CRUD:** Creation, reading, updating, and deletion of products via web interface and RESTful API.
*   **Filters:** Product listing with filters by title, serial number, category, and brand.
*   **Export:** Export of product data to Excel (`.xlsx`) files, including category, brand, prices, quantity, and creation date.
*   **Data Modeling:** Each product has a title, category, brand, description, serial number, cost price, selling price, quantity in stock, and creation/update timestamps.

### 4.3. Inflow Management

The inflows module (`inflows`) records the entry of products into stock. Key features include:

*   **Inflow Registration:** Creation of inflow records, associating a supplier and a product with a specific quantity.
*   **Automatic Stock Update:** After an inflow is created, the quantity of the corresponding product is automatically incremented in stock.
*   **Export:** Export of inflow data to Excel (`.xlsx`) files.

### 4.4. Outflow Management

The outflows module (`outflows`) manages the removal of products from stock, representing sales or other movements. Functionalities include:

*   **Outflow Registration:** Creation of outflow records, associating a product with a specific quantity.
*   **Automatic Stock Update:** After an outflow is created, the quantity of the corresponding product is automatically decremented in stock.
*   **Export:** Export of outflow data to Excel (`.xlsx`) files.

### 4.5. Brand, Category, and Supplier Management

The `brands`, `categories`, and `suppliers` modules provide full CRUD functionalities to manage the system's supporting entities. They include:

*   **Full CRUD:** Creation, reading, updating, and deletion of brands, categories, and suppliers via web interface and RESTful API.
*   **Error Handling:** The brands module, for example, handles `ProtectedError` when attempting to delete a brand associated with products, displaying a user-friendly message.
*   **Export:** Export of data to Excel (`.xlsx`) files.

## 5. Architecture

SGE is a monolithic application based on the Django framework, following the MVT (Model-View-Template) pattern. The API layer is implemented with Django REST Framework, providing a RESTful interface for programmatic interaction.

### 5.1. Database

The primary database used is PostgreSQL, configured to run in a separate Docker container. There is also a configuration for SQLite for local development.

### 5.2. Dockerization

The application is dockerized to facilitate development, deployment, and scalability. The `Dockerfile` defines the Python application's execution environment, and `docker-compose.yml` orchestrates the application services (web and PostgreSQL database).

## 6. Configuration and Installation

To configure and run the project locally using Docker Compose, follow the steps below:

1.  **Clone the Repository:**
    ```bash
    git clone -b develop https://github.com/pombinhagab/sge.git
    cd sge
    ```

2.  **Configure Environment Variables:**
    Create a `.env` file in the project root with the following variables:
    ```env
    SECRET_KEY=your_secret_key_here
    DEBUG=True
    ```
    *Replace `your_secret_key_here` with a strong secret key.*

3.  **Start Services with Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images, create the containers, and start the web application and PostgreSQL database.

4.  **Access the Application:**
    The application will be available at `http://localhost:8000`.

## 7. Metrics and Dashboard

The application dashboard, accessible on the homepage (`/`), displays important metrics for stock and sales management, calculated in the `app.metrics` module:

*   **Product Metrics:** Total stock cost, potential selling value, total product quantity, and potential profit.
*   **Sales Metrics:** Total outflows, total products sold, total sales value, and total sales profit.
*   **Daily Sales Data:** Historical series for the last 7 days for total sales value and quantity of products sold.
*   **Graphs:** Product count by category and by brand, for quick visualization of stock distribution.

## 8. RESTful APIs

In addition to the web interface, SGE exposes a series of RESTful endpoints for each module, allowing integration with other applications. All API endpoints are under the `api/v1/` prefix and require JWT authentication.

| Module | Endpoints (Examples) |
|---|---|
| Authentication | `/api/v1/authentication/token/`, `/api/v1/authentication/token/refresh/`, `/api/v1/authentication/token/verify/` |
| Products | `/api/v1/products/`, `/api/v1/products/{id}/` |
| Inflows | `/api/v1/inflows/` |
| Outflows | `/api/v1/outflows/` |
| Brands | `/api/v1/brands/`, `/api/v1/brands/{id}/` |
| Categories | `/api/v1/categories/`, `/api/v1/categories/{id}/` |
| Suppliers | `/api/v1/suppliers/`, `/api/v1/suppliers/{id}/` |

## 9. Final Considerations

The SGE project demonstrates a robust implementation of a stock management system using Django and Django REST Framework best practices, focusing on modularity, security (JWT), and ease of deployment (Docker). The inclusion of a dashboard with metrics and the ability to export data to Excel adds significant value for business management.

---
