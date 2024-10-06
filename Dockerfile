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