#!/bin/bash

ENV=$1

if [ "$ENV" == "development" ]; then
    echo "Deploying to Development..."
    docker run -d -p 9090:5000 -e FLASK_PORT=5000 my-app:${BUILD_NUMBER}
elif [ "$ENV" == "staging" ]; then
    echo "Deploying to Staging..."
    docker run -d -p 8081:5001 -e FLASK_PORT=5001 my-app:${BUILD_NUMBER}
elif [ "$ENV" == "production" ]; then
    echo "Deploying to Production..."
    docker run -d -p 8082:5002 -e FLASK_PORT=5002 my-app:${BUILD_NUMBER}
else
    echo "Invalid environment specified!"
    exit 1
fi
