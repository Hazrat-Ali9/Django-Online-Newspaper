# 📰 Django Online Newspaper

A modern, feature-rich online newspaper platform built with Django. This application allows users to read news articles, rate them, and provides an editorial system for content management.

## ✨ Features

### 🔍 Core Features
- **News Articles**: Browse and read news articles organized by categories
- **Rating System**: Users can rate articles (0-4 stars) with comments
- **Category Management**: News organized by different categories
- **User Authentication**: Registration, login, and profile management
- **Editorial System**: Special editor accounts for content creation
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5

### 👥 User Roles
- **General Users**: Can read articles, rate them, and manage their profiles
- **Editors**: Can create, edit, and publish news articles
- **Administrators**: Full access to manage users, categories, and content

### 📊 Advanced Features
- **Article Views Tracking**: Monitor article popularity
- **Editor Performance**: Track editor statistics and ratings
- **Image Upload**: Support for article images
- **Search & Filter**: Browse articles by category
- **Admin Dashboard**: Comprehensive admin interface

## 🛠️ Technology Stack

- **Backend**: Django 4.2.5
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite (default) / PostgreSQL (production ready)
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Image Processing**: Pillow
- **Styling**: Custom CSS + Bootstrap 5

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django-online-newspaper-main
   ```

2. **Run the setup script**
   ```bash
   python setup.py
   ```

3. **Start the server**
   ```bash
   python run.py
   ```

### Option 2: Manual Setup

1. **Clone and navigate to the project**
   ```bash
   git clone <repository-url>
   cd django-online-newspaper-main
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv newspaper_env
   source newspaper_env/bin/activate  # On Windows: newspaper_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

6. **Create a superuser account**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## 🌐 Access Points

- **Main Website**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin
- **User Accounts**: http://127.0.0.1:8000/accounts/
- **Posts Management**: http://127.0.0.1:8000/posts/

## 📁 Project Structure

```
django-online-newspaper-main/
├── 📁 accounts/              # User management app
│   ├── 📁 migrations/        # Database migrations
│   ├── 📁 templates/         # Account-related templates
│   ├── models.py            # User and Editor models
│   ├── views.py             # Account views
│   ├── forms.py             # User forms
│   └── urls.py              # Account URLs
├── 📁 posts/                 # News articles app
│   ├── 📁 migrations/        # Database migrations
│   ├── 📁 templates/         # Post-related templates
│   ├── models.py            # Post, Category, Rating models
│   ├── views.py             # Post views
│   ├── forms.py             # Post forms
│   └── urls.py              # Post URLs
├── 📁 Newspaper_Site/        # Main project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── views.py             # Main views
│   └── wsgi.py              # WSGI configuration
├── 📁 templates/             # Global templates
├── 📁 static/                # Static files (CSS, JS, images)
├── 📁 media/                 # User uploaded files
├── 📁 staticfiles/           # Collected static files
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── setup.py                 # Automated setup script
├── run.py                   # Quick run script
└── README.md                # This file
```

## 🎯 Usage Guide

### For General Users

1. **Registration**: Create an account at `/accounts/register/`
2. **Login**: Access your account at `/accounts/login/`
3. **Browse News**: View articles on the homepage organized by categories
4. **Rate Articles**: Click "Give Rating" on any article to rate and comment
5. **View Details**: Click "Details" to read the full article
6. **Profile Management**: Update your profile information

### For Editors

1. **Apply for Editor Role**: Submit an application through the accounts section
2. **Wait for Approval**: Admin needs to approve your editor application
3. **Create Articles**: Once approved, create and publish news articles
4. **Manage Content**: Edit your published articles
5. **Track Performance**: View your editor statistics and ratings

### For Administrators

1. **Access Admin Panel**: Visit `/admin/` with superuser credentials
2. **Manage Users**: Approve editor applications, manage user accounts
3. **Content Management**: Oversee all articles and categories
4. **System Monitoring**: Track site statistics and user activity

## 🔧 Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Edit the `.env` file with your specific configuration:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration

**SQLite (Default)**
- No additional configuration needed
- Database file: `db.sqlite3`

**PostgreSQL (Production)**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newspaper_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📊 Models Overview

### User Management
- **ApplicationsForEditors**: Editor application requests
- **EditorsProfile**: Editor profile information
- **User**: Django's built-in user model (extended)

### Content Management
- **Category**: News categories (Sports, Politics, Technology, etc.)
- **Post**: News articles with metadata
- **Rating**: User ratings and comments for articles

## 🎨 Customization

### Styling
- Main CSS: `static/css/style.css`
- Bootstrap 5 integration
- Responsive design for mobile devices

### Templates
- Base template: `templates/base.html`
- Account templates: `accounts/templates/`
- Post templates: `posts/templates/`

## 🚀 Deployment

### Development
```bash
python manage.py runserver
```

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure proper database (PostgreSQL recommended)
- [ ] Set up static file serving
- [ ] Configure email backend
- [ ] Set up proper logging
- [ ] Use environment variables for sensitive data
- [ ] Set up SSL/HTTPS
- [ ] Configure allowed hosts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Troubleshooting

### Common Issues

**Migration Errors**
```bash
python manage.py makemigrations --empty accounts
python manage.py makemigrations --empty posts
python manage.py migrate
```

**Static Files Not Loading**
```bash
python manage.py collectstatic --clear
```

**Permission Errors**
```bash
chmod +x setup.py run.py
```

### Getting Help

- Check the Django documentation: https://docs.djangoproject.com/
- Review the error logs in the console
- Ensure all dependencies are installed correctly

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check existing documentation
- Review the troubleshooting section

---

**Happy Coding! 🎉**

Built with ❤️ using Django and Bootstrap