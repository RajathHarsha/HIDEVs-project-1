
import webbrowser
from pathlib import Path
from threading import Thread

try:
    from deep_translator import GoogleTranslator
except Exception:
    GoogleTranslator = None  # fallback to returning original text

from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Multilingual → English</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial; margin: 22px; background:#f7f9fc; color:#111; }
    .container { max-width:900px; margin: 0 auto; background:white; padding:18px; border-radius:8px; box-shadow: 0 6px 20px rgba(18,38,63,0.07); }
    textarea { width:100%; min-height:140px; padding:10px; border-radius:6px; border:1px solid #dfe6ef; font-size:14px; resize:vertical; }
    button { background:#2563eb; color:white; border:none; padding:10px 14px; border-radius:6px; font-weight:600; cursor:pointer; }
    .row { display:flex; gap:12px; margin-bottom:12px; align-items:center; }
    .small { font-size:13px; color:#555; }
    pre { background:#f3f6fb; padding:12px; border-radius:6px; white-space:pre-wrap; word-wrap:break-word; }
    .footer { margin-top:12px; font-size:13px; color:#666; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Multilingual → English</h2>
    <p class="small">Paste text in any language below and click <strong>Translate</strong>.</p>

    <form method="post" action="{{ url_for('translate') }}">
      <label for="input_text"><strong>Input (any language)</strong></label>
      <textarea id="input_text" name="input_text" placeholder="Paste text here...">{{ input_text or '' }}</textarea>

      <div class="row">
        <button type="submit">Translate →</button>
        <form method="get" action="{{ url_for('index') }}" style="display:inline;">
          <button type="submit" style="background:#6b7280; margin-left:6px;">Clear</button>
        </form>
        <div style="margin-left:auto" class="small">Status: {{ status }}</div>
      </div>
    </form>

    <label for="output"><strong>Output (English)</strong></label>
    <pre id="output">{{ output_text or '' }}</pre>

    <div class="footer">
      <strong>Notes:</strong> This app uses <code>deep-translator</code> when installed. If it's not available, the input will be shown unchanged (safe fallback).
    </div>
  </div>
</body>
</html>
"""


def translate_text(input_text: str) -> str:
    """Translate to English, or return original text on failure / missing package."""
    if not input_text:
        return ""
    if GoogleTranslator:
        try:
            return GoogleTranslator(source="auto", target="en").translate(input_text)
        except Exception as e:
            return f"[Translation error] {e}"
    # fallback
    return input_text


@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_TEMPLATE, input_text="", output_text="", status="Ready")


@app.route("/translate", methods=["POST"])
def translate():
    input_text = (request.form.get("input_text") or "").strip()
    if not input_text:
        return redirect(url_for("index"))

    output = translate_text(input_text)
    return render_template_string(HTML_TEMPLATE, input_text=input_text, output_text=output, status="Done")


def open_browser(url: str):
    """Open the default browser to a URL (run in a thread)."""
    try:
        webbrowser.open_new(url)
    except Exception:
        pass


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5000
    url = f"http://{host}:{port}/"
    # open browser after server starts (threaded)
    Thread(target=lambda: open_browser(url), daemon=True).start()
    # run flask app
    app.run(host=host, port=port, debug=False)
