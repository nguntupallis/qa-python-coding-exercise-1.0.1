# Run tests with Docker

## Run Build server Docker

    cd server
    docker build -t apiserver .
    docker run -p 8000:8000 -it apiserver


## Run Api tests Docker

    cd tests
    docker build -f tests.dockerfile -t apitests .
    docker run --network=host apitests

---------------------------------------------------------


- Get the server up and running
- Write tests covering as many requirements as possible as detailed in the Requirements.md file
