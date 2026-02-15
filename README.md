# 🔐 FastAPI Authentication System - ADS SJSU

A modern web authentication system built with FastAPI and Bootstrap for the Department of Applied Data Science at San José State University.

![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📸 Screenshots

### Login Page
![Login Page](screenshots/login.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

## ✨ Features

- 🔒 **Secure Authentication** - Session-based login/logout system
- 🛡️ **Route Protection** - Protected routes accessible only to authenticated users
- 🎨 **Bootstrap Styling** - Modern, responsive UI design
- 📱 **Mobile Responsive** - Works seamlessly on all devices
- ⚡ **FastAPI Backend** - High-performance async Python framework
- 🔐 **Session Management** - Secure cookie-based sessions with Starlette middleware
- 🚨 **Error Handling** - User-friendly error messages with Bootstrap alerts

## 🛠️ Tech Stack

- **Backend**: FastAPI 0.104.1
- **Frontend**: Bootstrap 5.3, Jinja2 Templates
- **Session Management**: Starlette SessionMiddleware
- **Server**: Uvicorn
- **Language**: Python 3.10+

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/fastapi-auth-system.git
cd fastapi-auth-system
```

### 2. Create Virtual Environment

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python main.py
```

The application will be available at: `http://127.0.0.1:8000`

## 🔑 Demo Credentials

For testing purposes, use these credentials:

| Username | Password |
|----------|----------|
| admin | password123 |
| student | sjsu2024 |
| professor | ads@sjsu |

## 📁 Project Structure
```
fastapi-auth-system/
│
├── main.py                 # FastAPI app initialization & middleware
├── auth.py                 # Authentication router with all routes
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── README.md              # This file
│
└── templates/             # Jinja2 HTML templates
    ├── base.html         # Base template with navbar
    ├── home.html         # Home page
    ├── login.html        # Login form
    └── dashboard.html    # Protected dashboard
```

## 🔒 Security Features

- ✅ Signed session cookies (prevents tampering)
- ✅ CSRF protection via same-site cookies
- ✅ Session expiration (1 hour)
- ✅ Route protection with authentication checks
- ✅ Automatic redirect for unauthorized access

**⚠️ Note**: This is a demonstration project. For production:
- Use database instead of hardcoded credentials
- Hash passwords with bcrypt or Argon2
- Store secret keys in environment variables
- Enable HTTPS and set `https_only=True`
- Add rate limiting to prevent brute force attacks

## 🎯 Routes

| Route | Method | Description | Protected |
|-------|--------|-------------|-----------|
| `/` | GET | Home page with conditional content | ❌ |
| `/login` | GET | Display login form | ❌ |
| `/login` | POST | Process login credentials | ❌ |
| `/dashboard` | GET | User dashboard | ✅ |
| `/logout` | GET | Destroy session and logout | ✅ |

## 🎨 Bootstrap Components Used

- **Navbar** - Responsive navigation with dynamic links
- **Cards** - Content containers with shadow effects
- **Buttons** - Styled action buttons (primary, danger)
- **Alerts** - Error/success messages with dismiss functionality
- **Forms** - Styled input fields with validation
- **Grid System** - Responsive layout

## 🧪 Testing

### Manual Testing Checklist

- [ ] Home page displays correctly (logged out state)
- [ ] Login with invalid credentials shows error alert
- [ ] Login with valid credentials redirects to dashboard
- [ ] Dashboard shows personalized welcome message
- [ ] Dashboard is inaccessible without authentication
- [ ] Logout destroys session and redirects to home
- [ ] Navbar updates based on authentication state
- [ ] All pages are responsive on mobile devices

### Test Scenarios
```bash
# 1. Test home page
curl http://127.0.0.1:8000

# 2. Test protected route (should redirect)
curl -I http://127.0.0.1:8000/dashboard

# 3. Test login (requires form data)
curl -X POST http://127.0.0.1:8000/login \
  -d "username=admin&password=password123"
```

## 📚 Documentation

### Session Management

The application uses Starlette's SessionMiddleware for managing user sessions:
```python
app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,      # Signs cookies
    session_cookie="ads_session", # Cookie name
    max_age=3600,               # 1 hour expiration
    same_site="lax",            # CSRF protection
    https_only=False            # Set True in production
)
```

### Authentication Flow
```
User visits home → Not logged in → Shows "Login" button
                      ↓
                  Click Login
                      ↓
            Enter credentials (POST /login)
                      ↓
         Validate against USERS dictionary
                      ↓
              Valid credentials?
                /              \
              YES              NO
               ↓                ↓
    Create session         Show error alert
               ↓                ↓
    Redirect to dashboard   Stay on login
               ↓
    Dashboard checks session
               ↓
       Logged in? Show content
```

## 🐛 Troubleshooting

### Common Issues

**"Module not found: fastapi"**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

**"Templates not found"**
```bash
# Ensure templates/ folder is in the same directory as main.py
ls -la
# Should show: main.py, auth.py, templates/
```

**"Port 8000 already in use"**
```bash
# Use a different port
uvicorn main:app --port 8001
```

**Session not persisting**
```bash
# Check that SessionMiddleware is configured in main.py
# Ensure secret_key is set correctly
```

## 🚀 Deployment

### Deploy to Render

1. Create `render.yaml`:
```yaml
services:
  - type: web
    name: fastapi-auth
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
```

2. Connect GitHub repo to Render
3. Deploy automatically on push

### Deploy to Railway
```bash
railway login
railway init
railway up
```

### Deploy to Heroku

1. Create `Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

## 📈 Future Enhancements

- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Password hashing (bcrypt/Argon2)
- [ ] User registration functionality
- [ ] Password reset via email
- [ ] Remember me functionality
- [ ] Two-factor authentication (2FA)
- [ ] OAuth integration (Google, GitHub)
- [ ] User roles and permissions
- [ ] Rate limiting
- [ ] API endpoints with JWT authentication
- [ ] Admin dashboard
- [ ] Audit logging

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- Email: your.email@sjsu.edu
- LinkedIn: [Your Name](https://linkedin.com/in/your-profile)

## 🎓 Academic Context

This project was created as an assignment for the Applied Data Science program at San José State University. It demonstrates:
- Web application development with FastAPI
- Session-based authentication
- Frontend design with Bootstrap
- Security best practices
- Code organization and structure

## 🙏 Acknowledgments

- **FastAPI** - Modern web framework
- **Bootstrap** - Responsive UI framework
- **Starlette** - ASGI framework and session management
- **SJSU ADS Department** - Project inspiration

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/YOUR_USERNAME/fastapi-auth-system/issues) page
2. Create a new issue with detailed information
3. Contact: your.email@sjsu.edu

---

**⭐ If you found this project helpful, please give it a star!**

*Made with ❤️ for ADS-SJSU*
