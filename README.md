# Siyologics Commerce Platform Demo

## Overview

Siyologics Commerce Platform is a full-stack direct-to-customer commerce operations prototype developed to manage product showcasing, online ordering, payment processing, shipment tracking, inventory workflows, and admin-side operational management through a unified web platform.

The project combines customer-facing commerce functionality with backend operational workflows including payment handling, inventory synchronization, shipment lifecycle management, and automated email communication.

---

## Live Prototype

[https://siyologics.pythonanywhere.com/](https://siyologics.pythonanywhere.com/)

---

## Core Features

### Customer Features

* Product showcase and specifications
* Direct order placement workflow
* Razorpay payment integration
* Dynamic quantity-based pricing
* Shipment tracking without account login
* Automated order confirmation emails
* Responsive multi-device interface

### Admin Features

* Secure admin authentication
* KPI dashboard monitoring
* Order lifecycle management
* Inventory and stock management
* Shipment tracking updates
* Tracking ID management
* Shipping workflow operations

---

## Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap
* Jinja2 Templates

### Backend

* Flask (Python)
* mysql-connector-python

### Database

* MySQL

### Integrations

* Razorpay
* Flask-Mail
* Gmail SMTP

### Deployment

* PythonAnywhere
* Git & GitHub

---

## System Architecture

Frontend Interface
↓
Flask Backend
↓
MySQL Database
↓
External Services (Razorpay & SMTP)

---

## Project Structure

```plaintext
siyologics-commerce-platform-demo/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── templates/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── database/
│   └── schema.sql
│
├── docs/
│   ├── case-study.pdf
│   ├── er-diagram.png
│   ├── dfd-level0.png
│   ├── dfd-level1-user.png
│   └── dfd-level1-admin.png
│
└── screenshots/
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/THAMAN-SIYO/siyologics-commerce-platform-demo.git
cd siyologics-commerce-platform-demo
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
DB_HOST=your_host
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_database

MAIL_USERNAME=your_email
MAIL_PASSWORD=your_password

RAZORPAY_KEY_ID=your_key
RAZORPAY_KEY_SECRET=your_secret

FLASK_SECRET_KEY=your_secret_key

BASE_URL=http://localhost:5000
ADMIN_EMAIL=admin@example.com
```

---

### 5. Configure Database

Import the SQL schema:

```bash
mysql -u root -p < database/schema.sql
```

---

### 6. Run Application

```bash
python app.py
```

Application will run on:

```text
http://127.0.0.1:5000/
```

---

## Database Design

The platform uses a relational MySQL database structure for:

* customer orders
* inventory management
* shipment tracking
* admin authentication
* enquiry workflows

Main entities:

* Orders
* Products
* Stock
* Enquiry
* Admins

---

## Security Measures

* Environment variable configuration
* Parameterized SQL queries
* Session-based admin authentication
* Hashed password verification
* Controlled order lifecycle validation

---

## Engineering Challenges

* Payment-state synchronization
* Duplicate callback prevention
* Shipment lifecycle validation
* Inventory consistency management
* Backend operational workflow integration

---

## Future Enhancements

* Multi-product support
* Customer account system
* Analytics dashboard
* Invoice generation
* Cloud deployment infrastructure
* Mobile application integration
* Real-time shipment APIs

---

## Documentation

Detailed architecture diagrams, workflows, and portfolio case study are available inside the `/docs` directory.

---

## Developer

### Thaman Siyo

Full Stack Web Developer

GitHub:
[https://github.com/THAMAN-SIYO](https://github.com/THAMAN-SIYO)

LinkedIn:
[https://www.linkedin.com/in/thamansiyo](https://www.linkedin.com/in/thamansiyo)

Email:
[email-thamansiyo19@gmail.com](mailto:email-thamansiyo19@gmail.com)

---

## License

This repository is intended for educational, portfolio, and demonstration purposes.
