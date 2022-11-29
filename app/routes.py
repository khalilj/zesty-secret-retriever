from app import app
import os

@app.route('/health')
def health():
    return {
        "status": "Healthy!",
        "container": os.environ.get('CONTAINER_IMAGE', '"khalilj/zesty-secret-retriever"')
    }

@app.route('/secret')
def secret():
    return {
        "codeName": "<YOUR_CODENAME>",
        "secretCode": "<SECRET_CODE>"
    }
