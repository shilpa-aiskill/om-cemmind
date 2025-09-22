
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!doctype html>
    <html lang="en"><head>
      <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>OM CemMind Prototype</title>
      <style>
        body {font-family: system-ui, Arial; margin:0; background:#0b132b; color:#fff;}
        header {padding:18px 24px; background:#1c2541;}
        .badge {background:#3a506b; color:#fff; padding:4px 10px; border-radius:999px; font-size:12px;}
        main {max-width:960px; margin:24px auto; padding:0 16px;}
        .card {background:#1c2541; border-radius:14px; padding:20px; margin-bottom:16px;}
        a.btn {display:inline-block; padding:10px 14px; background:#5bc0be; color:#000; border-radius:8px; text-decoration:none; font-weight:600;}
        .grid {display:grid; gap:16px; grid-template-columns:repeat(auto-fit,minmax(240px,1fr));}
        footer {text-align:center; color:#9fb3c8; padding:24px 0;}
      </style>
    </head><body>
      <header>
        <div style="display:flex;align-items:center;gap:10px;">
          <div class="badge">OM CemMind</div>
          <div style="opacity:.75;">4–7 Day Demo Prototype</div>
        </div>
      </header>
      <main>
        <div class="card">
          <h2 style="margin-top:0;">Welcome 👋</h2>
          <p>This is the client-facing URL for the demo prototype (Desktop & Mobile ready).</p>
          <div class="grid">
            <div class="card">
              <h3 style="margin-top:0;">Health</h3>
              <p>Quick liveness probe for the service.</p>
              <a class="btn" href="/healthz">Open /healthz</a>
            </div>
            <div class="card">
              <h3 style="margin-top:0;">Kiln Decision (Illustrative)</h3>
              <p>POST <code>/api/v1/kiln/act</code> with JSON to simulate a recommendation.</p>
            </div>
            <div class="card">
              <h3 style="margin-top:0;">Override (Illustrative)</h3>
              <p>POST <code>/api/v1/override</code> to simulate human override flow.</p>
            </div>
          </div>
        </div>
      </main>
      <footer>© OM CemMind Prototype</footer>
    </body></html>
    """
