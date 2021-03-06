FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y wget
RUN apt-get -y install software-properties-common
RUN  add-apt-repository ppa:alex-p/tesseract-ocr -y && apt-get update
RUN  apt-get install -y tesseract-ocr
RUN sed -i ~/.profile -e 's/mesg n || true/tty -s \&\& mesg n/g'

RUN mkdir -p /workspace
WORKDIR /workspace
COPY ./requirements.txt /workspace
COPY ./entrypoint.sh /workspace
COPY . /workspace

#RUN pip install -r requirements.txt
ENTRYPOINT ["/workspace/entrypoint.sh"]
