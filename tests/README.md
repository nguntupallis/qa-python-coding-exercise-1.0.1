# Run tests with Docker

## Setup server locally using Kubernetes job

    Setup minikube (https://minikube.sigs.k8s.io/docs/start/)
    --------------

    Open new terminal

    cd server
    minikube start
    kubectl create -f job-config-file.yaml
    kubectl get pods (To get the pod name)
    kubectl port-forward <pod-name> 8000:8000 (Leave terminal open)

## Setup server locally using Docker (If server was not setup using the kubernetes job)

    cd server
    docker build -t apiserver .
    docker run -p 8000:8000 -it apiserver

## Run Api tests using Docker

    cd tests
    docker build -f tests.dockerfile -t apitests .
    docker run --network=host apitests
