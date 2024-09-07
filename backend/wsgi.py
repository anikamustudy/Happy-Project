from waitress import serve
from app import app

if _name_ == "_main_":
    serve(app, host="0.0.0.0", port=8000)
