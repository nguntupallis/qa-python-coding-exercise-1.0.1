# Running tests

## Setup server locally using Kubernetes job

    Setup minikube (https://minikube.sigs.k8s.io/docs/start/)
    --------------

    Open new terminal

    cd server
    minikube start
    kubectl create -f job-config-file.yaml
    kubectl port-forward "$(kubectl get pods --no-headers -o custom-columns=":metadata.name")" 8000:8000  - (Leave terminal open)

## Setup server locally using Docker (If server was not setup using the kubernetes job)

    cd server
    docker build -t apiserver .
    docker run -p 8000:8000 -it apiserver (Port already allocated error will come up if kube job is still running in another terminal, the other terminal need to be closed in order for this image to run)

## Run Api tests using Docker

    cd tests
    docker build -f tests.dockerfile -t apitests .
    docker run --network=host apitests

## Generate test results

    Install Allure using ```brew install allure```    
    allure serve allure-results  (This will open the test results in a new browser. I tried hard to get allure-results to generate in Docker but failed)


## Github actions are setup to run the docker images and show the logs of the container running the tests

Note: [REQ-3.5] The 'data/decision_engine/overall' item should be 'Accept' unless one of the rules has an outcome of 'Decline' in which case the overall result should be 'Decline' was failing when one of the rules decision is decline. 

I requested for more clarification regarding this but since there was no feedback I had to accept that this test will fail for now. I will update the tests based on the feedback.

Note: [REQ-3.1] The /xml endpoint only supports the GET method and [REQ-3.3] A successful call to the POST /xml endpoint returns a status code of 201

Both the above requirements are contradicting each other. Xml endpoint only supports GET method. This could be an open-ended test. But I apologise to not come back in time to clarify the same.
    
