# Hello World Python Website

Minimal Flask website.

## Setup (Windows PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 in your browser.

## Setup (macOS / Linux)

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

That's it — the app serves a single page that says "Hello, World!".
