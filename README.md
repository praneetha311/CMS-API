# Customer Management System (CMS) – REST API + Web UI

## Description
A simple **Customer Management System (CMS)** built using **Python Flask**.  
The application provides REST APIs to perform **CRUD operations** on customer data and includes a **web-based UI** built using HTML, CSS, and JavaScript.

## Technologies
- Python 3  
- Flask  
- HTML, CSS, JavaScript  
- Postman  
- Git  
- JSON  

## Project Structure
```

cms-api/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── postman/
└── cms_postman_collection.json

````

## Run
```bash
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

## Web UI

A clean, responsive UI allows:

* Adding customers
* Viewing all customers
* Editing customer details
* Deleting records

Built using:

* `templates/index.html`
* `static/style.css`
* `static/script.js`

Access it at:

```
http://127.0.0.1:5000
```

## Postman

Import the collection from:

```
postman/cms_postman_collection.json
```

## Notes

* Uses in-memory storage
* Data resets on restart
* Can be extended with database + authentication


