01:00 ●━━━━────── 3:04 ⇆ㅤ◁ㅤㅤ❚❚, [1/28/2022 5:59 AM]
FROM python:3.10.1-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
COPY . /kaal/
WORKDIR /kaal/
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
