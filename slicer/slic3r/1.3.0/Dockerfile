FROM ubuntu:20.04

# Setup timezone data
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Refresh package list
RUN apt-get update -y  --fix-missing
RUN apt-get upgrade -y

RUN apt-get install -y slic3r=1.3.0+dfsg1-3ubuntu1

# App
COPY app /usr/src/app
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
