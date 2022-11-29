import os
from app import app

if __name__ == "__main__":
    port = int(os.environ.get('FLASK_PORT', 80))
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    app.run(debug=True, host=host, port=port)
