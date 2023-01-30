FROM python:3.8

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]

ENV SLACK_WEBHOOK_URL=<slack-webhook-url>

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:qameta/allure
RUN pip install allure-python-commons

# Set the working directory
WORKDIR /tests

# Copy the current directory contents into the container at /app
ADD . /tests
RUN mkdir -p allure-results

# Install pytest and other required dependencies
RUN pip install -r requirements.txt

# Run pytest when the container starts
ENTRYPOINT tox

# RUN if [ $? -ne 0 ]; then curl -X POST -H 'Content-type: application/json' --data '{"text":"Test Failed :disappointed: Please check the logs"}' $SLACK_WEBHOOK_URL; else curl -X POST -H 'Content-type: application/json' --data '{"text":"Test Passed :smile:"}' $SLACK_WEBHOOK_URL; fi
# CMD allure serve allure-results && tail -f /dev/null