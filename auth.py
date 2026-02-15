from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter() 
templates = Jinja2Templates(directory="templates")

USERS = {
    "anushka": "password"
}

# Home Page
@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    username = request.session.get("username")
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "username": username,
            "is_logged_in": username is not None
        }
    )

#Login Page
@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    if request.session.get("username"):
        return RedirectResponse(url="/dashboard", status_code=303)
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "error": None
        }
    )

#Post Login
@router.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username in USERS and USERS[username] == password:
        request.session["username"] = username
        return RedirectResponse(url="/dashboard", status_code=303)
    else:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "Invalid username or password. Please try again."
            }
        )

#Dashboard Page
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    username = request.session.get("username")
    
    if not username:
        return RedirectResponse(url="/login", status_code=303)
    
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "username": username
        }
    )

#Logout
@router.get("/logout")
async def logout(request: Request):
    request.session.clear()

    return RedirectResponse(url="/", status_code=303)


