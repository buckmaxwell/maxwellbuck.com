FROM ubuntu:16.04


RUN mkdir /home
WORKDIR /home
RUN apt-get update -y
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get install -y perl
RUN apt-get install -y git
COPY ~/.githubpass /home/.githubpass 

