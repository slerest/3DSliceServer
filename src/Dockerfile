FROM ubuntu:20.04

# Setup timezone data
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get install -y apt-transport-https

# Refresh package list
RUN apt-get update -y  --fix-missing
RUN apt-get clean
RUN apt-get upgrade -y

RUN apt-get install -y python3-dev python3-pip

# push App and Pip stuff
COPY ./app /usr/src/app
WORKDIR /usr/src/app

# Use root in docker container is dangerous
# Bily is a nice name
#RUN useradd --create-home bily
#USER bily
RUN pip3 install --upgrade pip
RUN --mount=type=cache,mode=0755,target=/root/.cache pip3 install -r ./requirement.txt

# create and activate virtualenv
#RUN python3.9 -m venv /opt/venv
#ENV PATH="/opt/venv/bin:$PATH"


# App
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
