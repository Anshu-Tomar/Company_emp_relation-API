# Company Employee Relation API

A Django REST Framework API that models a one-to-many relationship between **Companies** and **Employees** — each company can have multiple employees, and each employee belongs to exactly one company.

## Features
- Full CRUD for companies and employees via DRF `ViewSet`s and a `DefaultRouter`
- Company categorization by type (IT / Non IT / Mobile Phones)
- Employee-to-company relationship via foreign key
- Employee position tracking (Manager / Software Developer / Project Leader)
- CORS enabled for cross-origin frontend consumption

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Framework | Django, Django REST Framework |
| Database | MySQL (`mysqlclient`) |
| CORS | django-cors-headers |

## Data Model

**Company**
| Field | Type |
|---|---|
| company_id | Auto (PK) |
| name | CharField |
| location | CharField |
| about | TextField |
| type | Choice: IT / Non IT / Mobiles Phones |
| added_date | DateTime (auto) |
| activate | Boolean |

**Employee**
| Field | Type |
|---|---|
| emp_name | CharField |
| emp_email | CharField |
| emp_address | CharField |
| emp_phone | CharField |
| emp_about | TextField |
| emp_position | Choice: Manager / Software Developer / Project Leader |
| company | ForeignKey → Company |

## API Reference

Base URL: `http://localhost:8000/`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/companies/` | List all companies |
| POST | `/companies/` | Create a company |
| GET | `/companies/{id}/` | Retrieve a company |
| PUT/PATCH | `/companies/{id}/` | Update a company |
| DELETE | `/companies/{id}/` | Delete a company |
| GET | `/employees/` | List all employees |
| POST | `/employees/` | Create an employee |
| GET | `/employees/{id}/` | Retrieve an employee |
| PUT/PATCH | `/employees/{id}/` | Update an employee |
| DELETE | `/employees/{id}/` | Delete an employee |

## Installation Guide

### Prerequisites
- Python 3.9+
- MySQL server running locally

### 1. Clone the repository
```bash
git clone https://github.com/Anshu-Tomar/Company_emp_relation-API.git
cd Company_emp_relation-API/company_emp_relation
```

### 2. Install dependencies
```bash
pip install django djangorestframework django-cors-headers mysqlclient
```

### 3. Configure the database
Update the `DATABASES` setting in `company_emp_relation/settings.py` with your local MySQL credentials, then run migrations:
```bash
python manage.py migrate
```

### 4. Run the server
```bash
python manage.py runserver
```
The API is now available at `http://localhost:8000/`.

## Usage Examples

Create a company:
```bash
curl -X POST http://localhost:8000/companies/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Acme Corp", "location": "Delhi NCR", "about": "IT services", "type": "IT", "activate": true}'
```

Add an employee under that company:
```bash
curl -X POST http://localhost:8000/employees/ \
  -H "Content-Type: application/json" \
  -d '{"emp_name": "John Doe", "emp_email": "john@acme.com", "emp_address": "Noida", "emp_phone": "9999999999", "emp_about": "Backend dev", "emp_position": "Software Developer", "company": 1}'
```

List all employees:
```bash
curl http://localhost:8000/employees/
```
