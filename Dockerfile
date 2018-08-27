FROM ubuntu:latest
MAINTAINER Alexander Danilov "alexander.danilov@gmail.com"

RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential
COPY . ./
WORKDIR ./
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]