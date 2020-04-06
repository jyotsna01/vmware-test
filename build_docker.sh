#!/bin/bash

set -e

DOCKER_IMAGE_NAME=gcr.io/poc-project/vmware-test

echo "Building Docker image ${DOCKER_IMAGE_NAME}:${BUILD_BUILDNUMBER}"
docker build -t ${DOCKER_IMAGE_NAME}:${BUILD_BUILDNUMBER} .
echo "Login info"
gcloud auth list
gcloud config list
echo "Login to gcr.io using GCLOUD SDK credentials"
docker login -u oauth2accesstoken -p "$(gcloud auth application-default print-access-token)" https://gcr.io
echo "Pushing Docker image to Google Container Registry"
docker push ${DOCKER_IMAGE_NAME}:${BUILD_BUILDNUMBER}
echo "Retagging Docker image with latest"
gcloud container images add-tag ${DOCKER_IMAGE_NAME}:${BUILD_BUILDNUMBER} ${DOCKER_IMAGE_NAME}:latest --quiet

echo "Cleaning up ${DOCKER_IMAGE_NAME}:${BUILD_BUILDNUMBER}"
docker rmi ${DOCKER_IMAGE_NAME}:${BUILD_BUILDNUMBER}
