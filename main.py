from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from auth import router as auth_router
import secrets

app = FastAPI(title="ADS-SJSU Authentication System")

SECRET_KEY = secrets.token_hex(32)  

app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,
    session_cookie="ads_session",  
    max_age=3600,  
    same_site="lax",  
    https_only=False  
)

app.include_router(auth_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)