# Django Basic DDD App

This repository is a simple e-commerce API created with Django and [django-ddd](https://github.com/jdiazromeral/django-ddd)

## API Definition

This project uses the OpenAPI 3.0.3 specification for defining and documenting APIs. The current API has three endpoints:

- **GET /api/products/list**: Lists all available products. 
- **POST /api/products/create**: Creates a new product. 
- **POST /api/reviews/create**: Creates a new review for a product.

For authentication, the API uses JSON Web Tokens (JWT). Therefore, to access these endpoints, include the token in the request header.

For testing purposes, the following payload structure is used for JWT:

```yaml
{
  "user_id": "1",
}
```
and the secret key is `secret`.

You can use a tool such as https://jwt.io/ to generate the token.

<details>
<summary><strong> OpenApi Definition </strong></summary>

```yaml
openapi: 3.0.3
info:
  title: DBDA - OpenAPI 3.0
  description: Basic API
  version: 0.1.0

servers:
  - url: localhost:8080
tags:
  - name: Products
    description: Our e-commerce products
  - name: Reviews
    description: Our e-commerce product's reviews

paths:
  /api/products/create:
    post:
      tags:
        - Products
      summary: Add a new product to the store
      operationId: addProduct
      security:
        - bearerAuth: [] 
      requestBody:
        description: Create a new product in the store
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Product'
        required: true
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PostResponse'          
        '405':
          description: Invalid input
        '401':
          description: Unauthorized

  /api/products/list:
    get:
      tags:
        - Products
      summary: List all available products
      operationId: listProducts
      security:
        - bearerAuth: [] 
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ProductList'          
        '404':
          description: Not Found
          
  /api/reviews/create:
    post:
      tags:
        - Reviews
      summary: Add a new review for a product
      operationId: addReview
      security:
        - bearerAuth: [] 
      requestBody:
        description: Create a new review for a product
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Review'
        required: true
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PostResponse'          
        '405':
          description: Invalid input
        '403':
          description: Forbidden

components:
  schemas:
  
    Review:
      required:
        - product_id
        - review
        - grade
      type: object
      properties:
        product_id:
          type: integer
          description: ID of the product being reviewed
          example: 1
        review:
          type: string
          description: Review text for the product
          example: Increible prueba tecnica
        grade:
          type: number
          description: Review grade for the product
          example: 5
  
    Product:
      required:
        - name
        - description
      type: object
      properties:
        name:
          type: string
          description: Name of the product
          example: prueba tecnica
        description:
          type: string
          description: Description of the product
          example: prueba tecnica de pablo
          
    ProductList:
      type: object
      properties:
        product_id:
          type: integer
          description: ID of the product
          example: 1
        average_grade:
          type: number
          description: Average grade of all reviews for a product
          example: 4.5
        num_reviews:
          type: integer
          description: Number of reviews for a product
          example: 2
        user_review:
          type: string
          description: A user's review for a product
          example: Increible prueba tecnica
          
    PostResponse:
      type: object
      properties:
        status:
          type: integer
          format: int64
          default: 200
          description: Status code of the response
          
  securitySchemes:
    bearerAuth:         
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: JWT used for authentication

```
</details>

## Installation

This project uses Python 3.11 and the dependencies are managed with Poetry.

You can clone the repository and install dependencies with:

```bash
git clone https://github.com/pablo-snz/django-basic-ddd-app.git
cd django-basic-ddd-app
poetry install
```


## Project Structure

This project uses Domain-Driven Design, resulting in the following structure:

```bash 
api
├── application
│   ├── interfaces
│   │   └── uow.py
│   └── services
│       ├── product_command.py
│       ├── product_query.py
│       └── review_command.py
├── domain
│   ├── entities
│   │   ├── product.py
│   │   └── review.py
│   ├── interfaces
│   │   └── repository.py
│   └── value_objects
│       ├── average_rating.py
│       ├── description.py
│       ├── name.py
│       ├── rating.py
│       ├── review_count.py
│       └── user_id.py
└──  infrastructure
          ├── apps.py
          ├── admin.py
          ├── controller
          │         ├── base_controller.py
          │         ├── create_product_controller.py
          │         ├── create_review_controller.py
          │         └── list_products_controller.py
          ├── django_repository.py
          ├── django_uow.py
          └── models.py

```
## Architecture Overview

The architecture of this project is centered around Domain-Driven Design (DDD), a design methodology aimed at handling complex domains. This strategic design approach separates the system into different layers, each having its specific responsibilities, leading to a system that is easier to manage, maintain, and scale.

### Domain Layer

At the core of this project lies the domain layer, which encapsulates the business logic, ensuring that all business rules are strictly adhered to. This layer is structured around entities such as `products` (our aggregate root) and `reviews`, and value objects such as average ratings, descriptions, names, etc.

The entities represent key business objects that have both a unique identity and a lifecycle. On the other hand, value objects are immutable and they are used to describe certain aspects of the domain. They do not have a conceptual identity.

### Application Layer

The application layer is responsible for orchestrating the execution of business operations, delegating the business rules to the domain layer. In this project, the application layer is divided into three services

- `ProductCommandService` - responsible for handling commands related to products, such as creating a new product.
- `ProductQueryService` - responsible for handling queries related to products, such as listing all available products.
- `ReviewCommandService` - responsible for handling commands related to reviews, such as creating a new review.

Note that this separation of concerns adheres to the Command Query Responsibility Segregation (CQRS) pattern.

Also, the Unit of Work pattern has been implemented to manage transactions, ensuring that there is only one transaction per business operation, and that all work within a transaction is completed or rolled back as a single unit.

### Infrastructure Layer

The infrastructure layer provides implementations of technical concerns such as data access and network communication. Here, we have defined models for persistence mechanisms, mirroring the domain entities as required by Django's ORM. This adheres to the Repository pattern, which provides a collection-like interface for accessing domain entities.

By separating these concerns, the codebase achieves a high level of modularity, making it easier to understand, maintain and extend. It also supports the Dependency Inversion Principle (DIP). This is achieved through the use of interface definitions in each layer.


## Running the Application

To start the server, run the following command:

```bash
python manage.py runserver
```

## Using the API

Here are some curl examples to interact with the API:

**Create a product:**

```bash
curl -X POST "http://localhost:8000/products/create" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <Your JWT Token>" \
-d '{
  "name": "Test product",
  "description": "Test product description"
}'
```

**List products:**

```bash
curl -X GET "http://localhost:8000/products/list" \
-H "accept: application/json" \
-H "Authorization: Bearer <Your JWT Token>"
```

**Create a review:**

```bash

curl -X POST "http://localhost:8000/reviews/create" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <Your JWT Token>" \
-d '{
  "product_id": "afb2fcae-5081-4edf-8fc5-aba79a6cb7c7",
  "review": "Great product",
  "grade": 5
}'

```

## Installing with Docker

Using Docker, you can create a containerized environment for the application which has all the necessary dependencies installed.

First, make sure Docker and Docker Compose are installed on your machine. If you do not have these installed, you can download them from Docker's official website.

Once you have Docker and Docker Compose installed, navigate to the root directory of the project where the `Dockerfile` and `docker-compose.yml` files are located.

Make `entrypoint.sh` executable by running the following command:

```bash
chmod +x entrypoint.sh
```


Build the Docker image by running the following command:

```bash
docker-compose build
```

After building the image, you can run the application using the following command:

```bash
docker-compose up
```

The application will now be accessible at http://localhost:8000.


### Testing

While the application is running in a Docker container, you can perform tests by executing the following command in another terminal:

```bash
docker-compose exec web pytest --cov=api
```

This command tells Docker to execute the command python manage.py test inside the running container named web.
