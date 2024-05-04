# Product Inventory Management System: FastAPI + Postgres (ORM: Sqlalchemy)

This project demonstrates  RESTful APIs for managing product inventory using FastAPI and SQLAlchemy, adhering to an MVC-like architecture.

# Prerequisites:
    - Docker
    - Docker Compose

# Setup

    Step 1 :- Clone the Repository:-
        git clone http://repo_url
    
    Step 2 :- Install docker-deskop:-
        url: https://docs.docker.com/desktop/install/mac-install/
    
    Step 3 :- Run application:-
        Run Services: docker compose up



# API Endpoints:

   ## Products:
            EndPoint                        Method              Description
            /products                        POST                 Create a new Product
            /products                        GET                  List all the product
            /products/{product_id}           GET                  Get details of a product by productid
            /products/{product_id}           PUT                  update details of a product by productid
            /products/{product_id}           DELETE               delete a product by productid

   ## Suppliers:
            EndPoint                        Method              Description
            /suppliers                       POST                 Create a new Supplier
            /supplier/{supplier_id}          GET                  Get details of a supplier by supplier_id



# Architecture:

    ├── __init__.py
    ├── app
    │   ├── api
    │   │   ├── product
    │   │   │   ├── __init__.py
    │   │   │   ├── helpers
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── product_helper.py
    │   │   │   ├── urls.py
    │   │   │   └── view.py
    │   │   └── supplier
    │   │       ├── __init__.py
    │   │       ├── helpers
    │   │       │   ├── __init__.py
    │   │       │   └── supplier_helper.py
    │   │       ├── urls.py
    │   │       └── view.py
    │   ├── config
    │   │   ├── __init__.py
    │   │   ├── app_config.py
    │   │   └── config_parser.py
    │   ├── create_app.py
    │   └── database
    │       ├── __init__.py
    │       ├── models
    │       │   ├── __init__.py
    │       │   ├── product.py
    │       │   └── supplier.py
    │       └── validators
    │           ├── __init__.py
    │           ├── product.py
    │           └── suppliers.py
    ├── requirements.txt
    └── run.py
    ├── docker-compose.yml
    ├── Dockerfile
    └── README.md

