FROM python:3.8

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]

RUN pip install --upgrade pip

# Set the working directory
WORKDIR /tests

# Copy the current directory contents into the container at /app
ADD . /tests

# Install pytest and other required dependencies
RUN pip install -r requirements.txt

# Run pytest when the container starts
ENTRYPOINT pytest -m version

# ENTRYPOINT tox