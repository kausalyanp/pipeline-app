#!/bin/bash

ENV=$1

if [ "$ENV" == "development" ]; then
    echo "Deploying to Development..."
    docker run -d -p 8080:8080 my-app:latest
elif [ "$ENV" == "staging" ]; then
    echo "Deploying to Staging..."
    docker run -d -p 8081:8080 my-app:latest
elif [ "$ENV" == "production" ]; then
    echo "Deploying to Production..."
    docker run -d -p 8082:8080 my-app:latest
else
    echo "Invalid environment specified!"
    exit 1
fi
