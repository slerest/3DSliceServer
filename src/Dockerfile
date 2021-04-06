FROM ubuntu:20.04

# Setup timezone data
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Refresh package list
RUN apt-get update -y  --fix-missing
RUN apt-get clean
RUN apt-get upgrade -y

RUN apt-get install -y python3-dev python3-pip

# push App and Pip stuff
COPY ./app /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirement.txt

# App
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
