**STOCK API**

This is a Django Rest Framework API project for Stock API. It provides a backend API for managing various aspects of the application.
Technologies Used
Django: 4.2.2
Django Rest Framework:3.14.0
Python: 3.10.11

Features
🔒 **User Authentication**
 The API includes user registration and authentication functionality, allowing users to create an account, log in, and obtain an authentication token.

📂 **Category Management**
The API provides CRUD (Create, Read, Update, Delete) operations for managing categories. It allows creating, retrieving, updating, and deleting categories, along with the ability to search for categories by name.

🏷️ **Brand Management**
Similar to categories, the API allows managing brands with CRUD operations. Brands can be created, retrieved, updated, and deleted.

🏢 **Firm Management**
The API includes functionality for managing firms, such as creating, retrieving, updating, and deleting firms. Additionally, it supports searching for firms by name, address, and phone number.

📦 **Product Management**
The API provides CRUD operations for managing products. Users can create, retrieve, update, and delete products.

💰 **Purchase and Sales Management**
The API allows managing purchases and sales with separate endpoints. Users can create, retrieve, update, and delete purchase and sales records. The sales endpoint includes validation to ensure that the quantity being sold does not exceed the available stock for a product.

🌐 **URL Routing and Configuration**
The main URL configuration file sets up the routing for various URLs and includes static file handling for media files.

🔐 **Django Model Permissions**
The code includes a custom permission class `myDjangoModelPermissions` that defines the permissions for different HTTP methods on model-based views.

📝 **Serializers**
The code includes serializers for different models, such as `ProductSerializer`, `CategorySerializer`, `BrandSerializer`, `FirmSerializer`, `PurchasesSerializer`, and `SalesSerializer`. These serializers define how data is serialized/deserialized when interacting with the API.

🔍 **Filtering and Searching**
The API includes filtering and searching capabilities for categories and firms. It allows filtering categories by name and provides search functionality for categories and firms.

**API Documentation**
It provides detailed information about the available endpoints, request/response formats, authentication, and authorization.

**Summary:**
The API is built using Django and Django Rest Framework. It provides functionality for managing categories, brands, firms, products, purchases, and sales. Users can register, authenticate, and perform CRUD operations on various resources. The API includes filtering, searching, and validation features to ensure data integrity. It also implements authentication and authorization for secure access to the endpoints.

**Usage:**
To use the API, follow these steps:

Clone the repository: git clone [https://github.com/gulfidanozturk/django-rest-api-stock-management.git]
Install the dependencies: pip install -r requirements.txt
Configure the database settings in the settings.py file.
Run database migrations: python manage.py migrate
Start the development server: python manage.py runserver
Once the server is running, you can make requests to the API endpoints using tools like cURL, Postman, or any HTTP client. Here are some example requests and responses:

Register a new user:
Register obtain an authentication token:
Request:

POST /account/register/
Body: { "email": "user@example.com", "password": "password123", "password2": "password123" }

Response:
Status: 201 Created
Body: { "id": 1, "email": "user@example.com", "first_name": "", "last_name": "" }

**Additional Usage Instructions:**

The API provides CRUD operations for categories, brands, firms, products, purchases, and sales. Refer to the API documentation for detailed information about available endpoints and their usage.

**Authentication and Authorization:**

Authentication is handled using token-based authentication. Users can register to create an account and log in to obtain an authentication token. The token should be included in the request headers for authorized access to protected endpoints.

**Contact**
For any inquiries or support, please contact Gul fidan Ozturk  at gulfidanozturk34@gmail.com

Please note that this is a generated README.md and may require further modifications to fit your project's specific details.


![APIroot](/preview/apiroot.jpg?raw=true "API root")


