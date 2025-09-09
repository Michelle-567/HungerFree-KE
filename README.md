# HungerFree KE 

HungerFree KE is a community-driven platform built with Django to connect people, donors, volunteers, and organizations in the fight against hunger.  
It enables users to donate, volunteer, request support, and stay updated on initiatives and impact.

---

##  Features

- **User Accounts** – Sign up, log in, and manage profiles  
- **Donations** – Donate funds or resources securely  
- **Requests** – Submit requests for help and support  
- **Notifications** – Get updates on activities and initiatives  
- **Partners** – Collaborations with organizations and donors  
- **Responsive Design** – Mobile-friendly and easy to navigate  

---

##  Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (default, but extendable to PostgreSQL/MySQL)  
- **Other Tools:** Django Widget Tweaks  

---

## 🚀 Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.x  
- pip  
- virtualenv (recommended)  

### Installation

```bash
# Clone the repository
git clone https://github.com/Michelle-567/HungerFree-KE.git
cd HungerFree-KE

# Create virtual environment
python -m venv venv
source venv/bin/activate  

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
