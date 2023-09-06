# API

Swagger API documentation:

## Paths

### /en/v1/business/business/

- **GET**
    
    Description: Get business information.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - name: string
            - email: string
            - phone_number: string
            - address: string
            - city: string
            - state: string
            - zip_code: string

### /en/v1/content/about-us/

- **GET**
    
    Description: Get information about the organization.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - content: string

### /en/v1/content/banner/

- **GET**
    
    Description: Get banner information.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - image: string
            - url: string

### /en/v1/content/home-page/

- **GET**
    
    Description: Get information about the home page.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - content: string

### /en/v1/content/privacy/

- **GET**
    
    Description: Get privacy information.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - content: string

### /en/v1/content/terms/

- **GET**
    
    Description: Get terms information.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - content: string

### /en/v1/core/categories/

- **GET**
    
    Description: Get a list of categories.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: array
        - items:
            - type: object
            - properties:
                - id: integer
                - name: string

### /en/v1/events/

- **GET**
    
    Description: Get a list of events.
    
    Parameters:
    
    - ordering: string
    - page: integer
    - page_size: integer
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - count: integer
            - next: string
            - previous: string
            - results: array
                - items:
                    - type: object
                    - properties:
                        - id: integer
                        - title: string
                        - description: string
                        - start_date: string
                        - end_date: string
                        - location: string
                        - image: string

### /en/v1/events/{slug}/

- **GET**
    
    Description: Get event details.
    
    Parameters:
    
    - slug: string
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - description: string
            - start_date: string
            - end_date: string
            - location: string
            - image: string

### /en/v1/paperclubs/

- **GET**
    
    Description: Get a list of paper clubs.
    
    Parameters:
    
    - ordering: string
    - page: integer
    - page_size: integer
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - count: integer
            - next: string
            - previous: string
            - results: array
                - items:
                    - type: object
                    - properties:
                        - id: integer
                        - title: string
                        - description: string
                        - image: string

### /en/v1/paperclubs/{slug}/

- **GET**
    
    Description: Get paper club details.
    
    Parameters:
    
    - slug: string
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - description: string
            - image: string

### /en/v1/tracks/

- **GET**
    
    Description: Get a listSwagger API documentation:
    

## Paths

### /en/v1/business/business/

- **GET**
    
    Description: Get business information.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - name: string
            - email: string
            - phone_number: string
            - address: string
            - city: string
            - state: string
            - zip_code: string

### /en/v1/content/about-us/

- **GET**
    
    Description: Get information about the organization.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - content: string

### /en/v1/content/banner/

- **GET**
    
    Description: Get banner information.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - image: string
            - url: string

### /en/v1/content/home-page/

- **GET**
    
    Description: Get information about the home page.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - content: string

### /en/v1/content/privacy/

- **GET**
    
    Description: Get privacy information.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - content: string

### /en/v1/content/terms/

- **GET**
    
    Description: Get terms information.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - content: string

### /en/v1/core/categories/

- **GET**
    
    Description: Get a list of categories.
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: array
        - items:
            - type: object
            - properties:
                - id: integer
                - name: string

### /en/v1/events/

- **GET**
    
    Description: Get a list of events.
    
    Parameters:
    
    - ordering: string
    - page: integer
    - page_size: integer
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - count: integer
            - next: string
            - previous: string
            - results: array
                - items:
                    - type: object
                    - properties:
                        - id: integer
                        - title: string
                        - description: string
                        - start_date: string
                        - end_date: string
                        - location: string
                        - image: string

### /en/v1/events/{slug}/

- **GET**
    
    Description: Get event details.
    
    Parameters:
    
    - slug: string
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - description: string
            - start_date: string
            - end_date: string
            - location: string
            - image: string

### /en/v1/paperclubs/

- **GET**
    
    Description: Get a list of paper clubs.
    
    Parameters:
    
    - ordering: string
    - page: integer
    - page_size: integer
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - count: integer
            - next: string
            - previous: string
            - results: array
                - items:
                    - type: object
                    - properties:
                        - id: integer
                        - title: string
                        - description: string
                        - image: string

### /en/v1/paperclubs/{slug}/

- **GET**
    
    Description: Get paper club details.
    
    Parameters:
    
    - slug: string
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - id: integer
            - title: string
            - description: string
            - image: string

### /en/v1/tracks/

- **GET**
    
    Description: Get a list of tracks.
    
    Parameters:
    
    - ordering: string
    - page: integer
    - page_size: integer
    
    Response:
    
    - 200 OK
    - Content-Type: application/json
    - schema:
        - type: object
        - properties:
            - count: integer
            - next: string
            - previous: string
            - results: array
                - items:
                    - type: object
                    - properties:
                        - id: integer
                        - name: string
                        - description: string

## Definitions

### Category

- type: object
- properties:
    - id: integer
    - name: string

### Event

- type: object
- properties:
    - id: integer
    - title: string
    - description: string
    - start_date: string
    - end_date: string
    - location: string
    - image: string

### PaperClub

- type: object
- properties:
    - id: integer
    - title: string
    - description: string
    - image: string

### Track

- type: object
- properties:
    - id: integer
    - name: string
    - description: string

### AboutUs

- type: object
- properties:
    - id: integer
    - title: string
    - content: string

### Business

- type: object
- properties:
    - id: integer
    - name: string
    - email: string
    - phone_number: string
    - address: string
    - city: string
    - state: string
    - zip_code: string

### PasswordChange

- type: object
- properties:
    - new_password1: string
    - new_password2: string

### PasswordReset

- type: object
- properties:
    - email: string

### PasswordResetConfirm

- type: object
- properties:
    - token: string
    - uid: string
    - new_password1: string
    - new_password2: string

### UserDetails

- type: object
- properties:
    - id: integer
    - username: string
    - email: string
    - first_name: string
    - last_name: string

### Login

- type: object
- properties:
    - username: string
    - password: string