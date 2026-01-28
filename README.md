# Content Management System (CMS) API

## Description
This project implements a simple Content Management System using a RESTful API
developed in Python with Flask. Postman is used to test and validate all CRUD
operations.

## Features
- Create content
- View all content
- View content by ID
- Update content
- Delete content

## Technologies Used
- Python
- Flask
- Postman
- Git

## Project Structure
cms-api/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── postman/
    └── cms_postman_collection.json

## How to Run
1. Install dependencies  
   `pip install -r requirements.txt`
2. Run the application  
   `python app.py`
3. Open Postman and test the APIs

## API Endpoints
POST    /contents  
GET     /contents  
GET     /contents/{id}  
PUT     /contents/{id}  
DELETE  /contents/{id}
