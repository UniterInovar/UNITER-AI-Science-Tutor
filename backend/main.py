"""
UNITER AI Science Tutor API

Main FastAPI application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.router import api_router

app = FastAPI(
    title="UNITER AI Science Tutor",
    description="AI-powered science education platform for students, teachers and schools.",
    version="0.1.0",
)

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:5175",
        "http://127.0.0.1:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Register all API routes
# -----------------------------
app.include_router(api_router)


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/", tags=["Root"])
def root():
    return {
        "application": "UNITER AI Science Tutor",
        "version": "0.1.0",
        "status": "running",
    }
