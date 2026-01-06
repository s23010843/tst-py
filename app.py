from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return (
        "<!doctype html>"
        "<html><head><meta charset='utf-8'><title>Hello World</title>"
        "<style>body{font-family:Arial,Helvetica,sans-serif;margin:40px}</style>"
        "</head><body><h1>Hello, World!</h1>"
        "<p>This is a minimal Flask website.</p>"
        "</body></html>"
    )


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    print(f"Server is running on http://localhost:{port} (bind: {host}:{port})")
    app.run(debug=True, host=host, port=port)
