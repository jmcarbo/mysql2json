FROM python:3.5

MAINTAINER Arturo Mejia (github:arturom)

WORKDIR /root/app

COPY requirements.txt /tmp/

RUN pip install --requirement /tmp/requirements.txt

COPY app /root/app/

ENTRYPOINT ["python","/root/app/app"]
