#This app.py is a simple Flask application that serves as a demonstration 
# for CI/CD to Google Kubernetes Engine (GKE). 
# It has two routes: the root route ("/") which returns a message indicating that CI/CD to GKE is working, and a health check route ("/health") which returns an "OK" status with a 200 HTTP status code. The application listens on all available interfaces on port 8080.
from flask import Flask

app = Flask(__name__)

@app.route('/')  # Root route that returns a message indicating CI/CD to GKE is working
def home():
    return "CI/CD to GKE is Working!"

@app.route('/health')  # Health check route that returns an "OK" status with a 200 HTTP status code
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 
