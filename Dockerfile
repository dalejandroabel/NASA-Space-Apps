<<<<<<< HEAD
FROM python:3.12.3
ENV PYTHONUNBUFFERED=True

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt

ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY /app $APP_HOME/app

# Copy the rest of the codebase into the image
COPY --chown=app:app . ./
USER app

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available in Cloud Run.
CMD exec gunicorn --bind :$PORT --log-level info --workers 1 --threads 8 --timeout 0 app:server
=======
# Python image to use.
FROM python:3.12-alpine

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .
ENV PORT=8080
# Run app.py when the container launches
ENTRYPOINT ["python", "app.py"]
>>>>>>> af1bfabf8795de6140482c06d6902a2af1f45e29
