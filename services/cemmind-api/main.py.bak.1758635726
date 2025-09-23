from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="OM CemMind API (Prototype)")

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h2>OM CemMind Prototype</h2><p>Landing page is working ✅</p>"

@app.get("/healthz")
def healthz():
    return JSONResponse({"ok": True})
