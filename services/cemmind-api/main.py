from fastapi import FastAPI, Response

app = FastAPI(title="OM CemMind – Prototype", version="0.1.0")

@app.get("/healthz", include_in_schema=False)
def healthz():
    return {"ok": True}

@app.get("/", include_in_schema=False)
def home():
    return Response(
        "<h1>OM CemMind – Prototype</h1>"
        "<p><a href='/docs'>API Docs</a> · <a href='/healthz'>Health</a></p>",
        media_type="text/html"
    )
