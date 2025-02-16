Yojana Buddy: Django Chatbot Application
Yojana Buddy is a Django-based web application designed to assist users in navigating and understanding various government schemes. The chatbot provides interactive assistance, allowing users to inquire about different schemes and their eligibility criteria.

Features
User Authentication: Secure user registration and login functionality.
Interactive Chatbot: Engage in conversations to learn about various government schemes.
Responsive Design: User-friendly interface compatible with both desktop and mobile devices.
Prerequisites
Python 3.x
Django 3.x or higher
pip (Python package installer)
Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/yourusername/yojana_buddy.git
cd yojana_buddy
Create a Virtual Environment:

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply Migrations:

bash
Copy
Edit
python manage.py migrate
Create a Superuser:

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up the superuser account.

Run the Development Server:

bash
Copy
Edit
python manage.py runserver
Access the application at http://127.0.0.1:8000/.

Project Structure
plaintext
Copy
Edit
yojana_buddy/
├── chatbot/
│   ├── migrations/
│   ├── static/
│   │   └── chatbot/
│   │       ├── style.css
│   │       └── script.js
│   ├── templates/
│   │   └── chatbot/
│   │       ├── index.html
│   │       ├── login.html
│   │       └── signup.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   ├── views.py
│   └── urls.py
├── yojana_buddy/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── requirements.txt
Usage
Accessing the Chatbot: After logging in, navigate to the chatbot interface to start interacting.
Admin Panel: Access the Django admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

License
This project is licensed under the MIT License.
