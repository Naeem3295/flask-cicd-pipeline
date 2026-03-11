pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = "naeem3295"
        IMAGE_NAME      = "flask-cicd-pipeline"
        IMAGE_TAG       = "v${BUILD_NUMBER}"
        EMAIL_TO        = "abunaeem059322@gmail.com"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "================================"
                echo "Checking out from GitHub..."
                echo "Build: #${BUILD_NUMBER}"
                echo "================================"
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running unit tests..."
                sh """
                    docker run --rm \
                        -v \${WORKSPACE}:/app \
                        -w /app \
                        python:3.11-slim \
                        sh -c "pip install -r requirements.txt -q && pytest test_app.py -v"
                """
                echo "All tests passed!"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest ."
                echo "Image: ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Pushing to Docker Hub..."
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                    sh "docker logout"
                }
                echo "Pushed successfully!"
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                sh "docker stop flask-app 2>/dev/null || true"
                sh "docker rm flask-app 2>/dev/null || true"
                sh """
                    docker run -d \
                        --name flask-app \
                        -p 5050:5000 \
                        -e APP_VERSION=${IMAGE_TAG} \
                        ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest
                """
                echo "Deployed at http://localhost:5050"
            }
        }

        stage('Health Check') {
            steps {
                echo "Checking app health..."
                sh "sleep 5"
                sh "docker exec flask-app curl -f http://localhost:5000/health"
                echo "App is healthy!"
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh "docker image prune -f 2>/dev/null || true"
        }

        success {
            echo "Pipeline SUCCESS!"
            emailext(
                to: "${EMAIL_TO}",
                subject: "✅ SUCCESS: ${JOB_NAME} #${BUILD_NUMBER}",
                body: """<html>
<body style="font-family:Arial;padding:20px;">
<h2 style="color:#28a745;">✅ Pipeline Successful!</h2>
<table style="border-collapse:collapse;width:100%;">
<tr style="background:#f8f9fa;">
    <td style="padding:10px;border:1px solid #dee2e6;"><b>Job</b></td>
    <td style="padding:10px;border:1px solid #dee2e6;">${JOB_NAME}</td>
</tr>
<tr>
    <td style="padding:10px;border:1px solid #dee2e6;"><b>Build</b></td>
    <td style="padding:10px;border:1px solid #dee2e6;">#${BUILD_NUMBER}</td>
</tr>
<tr style="background:#f8f9fa;">
    <td style="padding:10px;border:1px solid #dee2e6;"><b>Duration</b></td>
    <td style="padding:10px;border:1px solid #dee2e6;">${currentBuild.durationString}</td>
</tr>
<tr>
    <td style="padding:10px;border:1px solid #dee2e6;"><b>Image</b></td>
    <td style="padding:10px;border:1px solid #dee2e6;">${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}</td>
</tr>
<tr style="background:#f8f9fa;">
    <td style="padding:10px;border:1px solid #dee2e6;"><b>App URL</b></td>
    <td style="padding:10px;border:1px solid #dee2e6;">
        <a href="http://localhost:5050">localhost:5050</a>
    </td>
</tr>
</table>
<br>
<a href="${BUILD_URL}"
   style="background:#28a745;color:white;padding:10px 20px;
          text-decoration:none;border-radius:5px;">
   View Build
</a>
</body>
</html>""",
                mimeType: 'text/html'
            )
        }

        failure {
            echo "Pipeline FAILED!"
            emailext(
                to: "${EMAIL_TO}",
                subject: "❌ FAILED: ${JOB_NAME} #${BUILD_NUMBER}",
                body: """<html>
<body style="font-family:Arial;padding:20px;">
<h2 style="color:#dc3545;">❌ Pipeline Failed!</h2>
<table style="border-collapse:collapse;width:100%;">
<tr style="background:#f8f9fa;">
    <td style="padding:10px;border:1px solid #dee2e6;"><b>Job</b></td>
    <td style="padding:10px;border:1px solid #dee2e6;">${JOB_NAME}</td>
</tr>
<tr>
    <td style="padding:10px;border:1px solid #dee2e6;"><b>Build</b></td>
    <td style="padding:10px;border:1px solid #dee2e6;">#${BUILD_NUMBER}</td>
</tr>
<tr style="background:#f8f9fa;">
    <td style="padding:10px;border:1px solid #dee2e6;"><b>Duration</b></td>
    <td style="padding:10px;border:1px solid #dee2e6;">${currentBuild.durationString}</td>
</tr>
</table>
<br>
<a href="${BUILD_URL}console"
   style="background:#dc3545;color:white;padding:10px 20px;
          text-decoration:none;border-radius:5px;">
   View Error
</a>
</body>
</html>""",
                mimeType: 'text/html'
            )
        }
    }
}
