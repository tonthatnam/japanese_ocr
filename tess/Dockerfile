FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install software-properties-common
RUN  add-apt-repository ppa:alex-p/tesseract-ocr -y && apt-get update
RUN  apt-get install -y tesseract-ocr
RUN mkdir ~/tess && cd ~/tess

WORKDIR /tess
COPY ./requirements.txt /tess
COPY ./entrypoint.sh /tess
COPY . /tess

#RUN pip install -r requirements.txt
ENTRYPOINT ["/tess/entrypoint.sh"]
