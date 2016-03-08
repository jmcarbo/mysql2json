FROM python:3.5

RUN apt-get update && apt-get install -y \
    autoconf \
    bison \
    build-essential \
    flex \
    libtool

WORKDIR /root/app

COPY requirements.txt /tmp/

RUN pip install --requirement /tmp/requirements.txt

COPY app.py /root/app/

ENTRYPOINT ["python","/root/app/app.py"]