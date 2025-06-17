# 📱 Vocalin - Django Social Media App

Vocalin is a feature-rich full-stack social media web application built using Django. It allows users to connect, share posts, and engage with the community in a clean, responsive UI.

---

## 🚀 Features

- 🔐 User registration, login, and logout
- 📝 Create, read, update, and delete posts (CRUD)
- 👤 User profile management (username, bio, profile picture)
- 💬 Commenting system for post engagement
- 📷 Media upload (images/videos if enabled)
- 🛡️ Secure session handling using Django’s built-in auth
- 🎨 Responsive UI using Tailwind CSS or Bootstrap

---

## 🛠️ Tech Stack

| Layer         | Technology        |
|---------------|-------------------|
| **Backend**   | Django, Python 3   |
| **Frontend**  | Django Templates, HTML, CSS (Tailwind/Bootstrap) |
| **Database**  | SQLite3 (default), PostgreSQL/MySQL supported |
| **Auth**      | Django Authentication |
| **Version Control** | Git + GitHub |

---

## 📦 Project Structure

```
Vocalin-Django-SocialMediaApp/
│
├── accounts/             # User auth & profile handling
├── posts/                # Core posting logic
├── templates/            # HTML templates
├── static/               # CSS, JS, media files
├── db.sqlite3            # Default SQLite database
├── manage.py             # Django project runner
├── requirements.txt      # Python dependencies
└── README.md             # Documentation (this file)
```

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/PratikTiwari5995/Vocalin-Django-SocialMediaApp.git
cd Vocalin-Django-SocialMediaApp
```

### 2. Set up a virtual environment
```bash
# Windows (PowerShell)
python -m venv env
.\env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin panel access)
```bash
python manage.py createsuperuser
```

### 6. Start the development server
```bash
python manage.py runserver
```

### 7. Open in your browser:
- App: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📌 Future Improvements

- ❤️ Like and reply system
- 📣 Real-time notifications
- ☁️ Deployment via Heroku or Render
- 📱 Mobile-friendly UI enhancements

---




