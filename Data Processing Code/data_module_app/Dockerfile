# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# RUN apt-get install -y python3-pip python-dev

ENV APP_HOME /data
WORKDIR $APP_HOME
COPY . ./

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.

EXPOSE 8080
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["data.py"]
