from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/render")
def render():
    url = request.args.get("url")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=20000)
        html = page.content()
        browser.close()
        return jsonify({"html": html})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
