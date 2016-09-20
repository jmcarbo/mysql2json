FROM python:3.5

MAINTAINER Arturo Mejia (github:arturom)

WORKDIR /root/app

COPY requirements.txt /tmp/

RUN pip install --requirement /tmp/requirements.txt

COPY app /root/app/

RUN apt-get update && apt-get install -y wget 
RUN wget https://github.com/miku/esbulk/releases/download/v0.3.9/esbulk_0.3.9_amd64.deb
RUN dpkg -i esbulk_0.3.9_amd64.deb

CMD ["python","/root/app/app"]
