# Django Basic DDD App

This repository is a simple e-commerce API created with Django and Domain-Driven Design.

## API Definition

This project uses the OpenAPI 3.0.3 specification for defining and documenting APIs. The current API has three endpoints:

- **GET /api/products/list**: Lists all available products. 
- **POST /api/products/create**: Creates a new product. 
- **POST /api/review/create**: Creates a new review for a product.

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
  title: YourStep - OpenAPI 3.0
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
          
  /api/review/create:
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
.
├── application
│   └── __init__.py
├── domain
│   └── __init__.py
├── infrastructure
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   └── models.py
└── __init__.py

```

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
