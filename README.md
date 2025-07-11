# SmartPOS-Django

SmartPOS is a responsive, web-based Point of Sale (POS) system built with Django. It provides store owners and staff with an easy-to-use platform to manage products, record sales, track revenue, and monitor stock levels.

---

## 🚀 Features

- 🔐 Secure login/logout system
- 📦 Product and stock management
- 💰 Sale recording with total revenue calculation
- 🔍 Product search functionality
- 🔔 Low stock alert system (stock ≤ 5)
- 📊 Sales report with Chart.js visualizations
- 📱 Mobile-friendly Bootstrap 5 interface
- ⚙️ Django Admin Panel for full CRUD access

---

## 🛠 Tech Stack

| Tech       | Usage                        |
|------------|------------------------------|
| Django     | Backend web framework        |
| SQLite     | Default database (for dev)   |
| Bootstrap  | Frontend styling             |
| Chart.js   | Sales data visualization     |
| FontAwesome| Icons                        |

---

## 📸 Screenshots

# Login Panel
<img width="1366" height="308" alt="image" src="https://github.com/user-attachments/assets/b4321169-ddfa-4a2f-9615-c0dc9a46cc20" />

# Dashboard
<img width="1366" height="421" alt="image" src="https://github.com/user-attachments/assets/91e18307-6804-40c2-a3c7-5e6687af7240" />

# Product List
<img width="1366" height="368" alt="image" src="https://github.com/user-attachments/assets/d9d5c72a-538b-42cf-abfb-81652756311d" />

# Sales Form
<img width="1366" height="367" alt="image" src="https://github.com/user-attachments/assets/3c966cfa-7549-4fae-b40b-d210633e8c5b" />

# Sales Report
<img width="1366" height="604" alt="image" src="https://github.com/user-attachments/assets/b86026f1-117c-46fc-9153-07cfd561f796" />

---

## 📦 Installation (Run Locally)

# 1. Clone the repository
git clone https://github.com/your-username/SmartPOS-Django.git

cd SmartPOS-Django

# 2. Set up virtual environment
python -m venv venv

venv\Scripts\activate  # On Windows

source venv/bin/activate  # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Start development server
python manage.py runserver

Visit: http://127.0.0.1:8000

## 📁 Project Structure

pos_project/

│

├── pos_system/         # Main project settings

│

├── posapp/             # Core app (views, models, urls)

│

├── templates/          # HTML templates (Bootstrap-based)

│

├── static/             # CSS, JS, images (if any)

│

├── db.sqlite3          # Development DB

│

├── requirements.txt    # Python dependencies

│

└── README.md           # Project overview

## 📃 License
This project is licensed under the MIT License.
