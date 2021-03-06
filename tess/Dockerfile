FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y wget && \
    apt-get -y install software-properties-common && \
    add-apt-repository ppa:alex-p/tesseract-ocr -y && apt-get update && \
    apt-get install -y tesseract-ocr && \
    sed -i ~/.profile -e 's/mesg n || true/tty -s \&\& mesg n/g' && \
    apt-get install -y python3-all-dev && \
    apt-get install -y python3 python3-pip

RUN mkdir -p /workspace
WORKDIR /workspace
COPY ./requirements.txt /workspace
COPY ./entrypoint.sh /workspace
COPY . /workspace

RUN pip3 install -r requirements.txt
ENTRYPOINT ["/workspace/entrypoint.sh"]
