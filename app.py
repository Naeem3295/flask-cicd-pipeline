from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Home endpoint
@app.route('/')
def home():
    return jsonify({
        'status': 'success',
        'message': 'Flask CI/CD Pipeline App',
        'developer': 'MD ABU NAEEM',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'timestamp': datetime.now().isoformat()
    })


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'flask-cicd-pipeline',
        'uptime': 'running'
    })

# API info endpoint
@app.route('/api/info')
def info():
    return jsonify({
        'app': 'Flask CI/CD Demo',
        'tech_stack': [
            'Python Flask',
            'Docker',
            'Jenkins',
            'GitHub'
        ],
        'pipeline_stages': [
            'Checkout',
            'Install Dependencies', 
            'Run Tests',
            'Build Docker Image',
            'Push to Docker Hub',
            'Deploy',
            'Notify'
        ]
    })

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )
