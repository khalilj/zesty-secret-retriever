from app import app

@app.route('/health')
def health():
    return {
        "status": "Healthy!",
        "container": "https://docker.registry.com/somepath"
    }

@app.route('/v1/test')
def test():
    return 'this is Salt security'
