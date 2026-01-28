# Customer Management System (CMS) – REST API

## Description
A simple **Customer Management System (CMS)** built using **Python Flask**.  
The application exposes REST APIs to perform **CRUD operations** on customer data and uses **Postman** for API testing.

## Technologies
- Python 3  
- Flask  
- Postman  
- Git  
- JSON  

## Project Structure
```

customer-cms-api/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── postman/
└── customer_cms_postman_collection.json

````

## Setup & Run
```bash
pip install -r requirements.txt
python app.py
````

Server URL:

```
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint        | Description        |
| ------ | --------------- | ------------------ |
| POST   | /customers      | Add customer       |
| GET    | /customers      | Get all customers  |
| GET    | /customers/{id} | Get customer by ID |
| PUT    | /customers/{id} | Update customer    |
| DELETE | /customers/{id} | Delete customer    |

## Sample Request (POST)

```json
{
  "id": 101,
  "name": "Rahul Sharma",
  "email": "rahul@gmail.com",
  "phone": "9876543210",
  "city": "Hyderabad"
}
```

## Postman

Import the collection from:

```
postman/customer_cms_postman_collection.json
```

## Notes

* Uses in-memory storage
* Data resets on server restart
* Can be extended with database and authentication

