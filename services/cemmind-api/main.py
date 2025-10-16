from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="OM CemMind API (Prototype)",
              description="Kiln agent demo; health + homepage",
              version="0.1.0")

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h2>OM CemMind Prototype</h2><p>Landing page is working ✅</p>"

@app.get("/healthz")
def healthz():
    return JSONResponse({"ok": True})

# keep push endpoint stub (204) so future Pub/Sub won’t 404
@app.post("/pubsub/kiln")
async def pubsub_kiln(request: Request):
    try:
        _ = await request.json()
    except Exception:
        pass
    return Response(status_code=204)

@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)
