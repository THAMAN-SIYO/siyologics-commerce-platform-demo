```python
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from flask_mail import Mail, Message
import razorpay

# ---------- LOAD ENV ----------
load_dotenv()

# ---------- ENV VARIABLES ----------
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

# ---------- CREATE APP ----------
app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

# ---------- DATABASE ----------
def get_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# ---------- MAIL CONFIG ----------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = MAIL_USERNAME

mail = Mail(app)

# ---------- RAZORPAY ----------
client = None

if RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET:
    client = razorpay.Client(
        auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)
    )

# =========================================================
# ROUTES
# =========================================================

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/product", methods=["GET", "POST"])
def product():

    if request.method == "POST":

        # ---------- FORM DATA ----------
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        quantity = int(request.form["quantity"])

        # ---------- SAMPLE PRICING ----------
        if quantity == 1:
            total_amount = 389
        elif quantity == 2:
            total_amount = 569
        else:
            flash("Invalid quantity selected.")
            return redirect(url_for("product"))

        amount_paise = total_amount * 100

        # ---------- SAMPLE DATABASE INSERT ----------
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO orders
            (name, phone, email, quantity, total_amount)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (name, phone, email, quantity, total_amount)
        )

        conn.commit()
        order_id = cursor.lastrowid

        cursor.close()
        conn.close()

        # ---------- CREATE PAYMENT ORDER ----------
        razorpay_order = client.order.create({
            "amount": amount_paise,
            "currency": "INR",
            "payment_capture": 1
        })

        return render_template(
            "product.html",
            key_id=RAZORPAY_KEY_ID,
            razorpay_order_id=razorpay_order["id"],
            amount=amount_paise,
            amount_display=total_amount,
            demo_order_id=order_id
        )

    return render_template("product.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # ---------- STORE ENQUIRY ----------
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO enquiry (name, email, message)
            VALUES (%s, %s, %s)
            """,
            (name, email, message)
        )

        conn.commit()

        cursor.close()
        conn.close()

        # ---------- SEND CONFIRMATION EMAIL ----------
        try:
            msg = Message(
                subject="Enquiry Received",
                recipients=[email]
            )

            msg.body = f"""
Hi {name},

Thank you for contacting us.

We have received your enquiry and will get back to you shortly.

Regards,
Siyologics
"""

            mail.send(msg)

        except Exception as e:
            print("MAIL ERROR:", e)

        flash("Thank you! Your enquiry has been received.")

        return redirect(url_for("contact"))

    return render_template("contact.html")


@app.route("/payment-success")
def payment_success():

    payment_id = request.args.get("payment_id")

    # ---------- SAMPLE PAYMENT SUCCESS FLOW ----------
    flash("Payment successful! Order confirmed.")

    return render_template(
        "product.html",
        payment_success=True,
        payment_id=payment_id
    )


@app.route("/payment-failed")
def payment_failed():

    flash("Payment failed or cancelled.")

    return redirect(url_for("product"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # ---------- DEMO AUTH FLOW ----------
        if username == "admin" and password == "demo":
            flash("Demo login successful.")
            return redirect(url_for("admin"))

        flash("Invalid credentials.")

    return render_template("login.html")


@app.route("/admin")
def admin():

    # ---------- DEMO DASHBOARD ----------
    dashboard_stats = {
        "orders": 125,
        "revenue": 45230,
        "inventory": 78,
        "shipments": 34
    }

    return render_template(
        "admin.html",
        dashboard_stats=dashboard_stats
    )


@app.route("/track-order")
def track_order():

    # ---------- DEMO TRACKING ----------
    sample_tracking = {
        "payment_status": "paid",
        "order_status": "SHIPPED",
        "tracking_id": "DEMO123456IN"
    }

    return render_template(
        "product.html",
        order_tracking=sample_tracking
    )


@app.route("/legal")
def legal():
    return render_template("legal.html")


# =========================================================
# RUN APP
# =========================================================
if __name__ == "__main__":
    app.run()
```

# Notes

This is a simplified public demo version of the backend architecture intended for portfolio and educational showcase purposes.

The production implementation contains additional:

* operational workflows
* inventory synchronization
* shipment lifecycle management
* transactional validations
* security layers
* administrative operations

