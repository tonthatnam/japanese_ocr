![apm](https://img.shields.io/apm/l/vim-mode.svg) 

Create a auxiliary sign detection, and recognition REST API by using technologies below
 
 * Tesseract
 * Django
 * Docker
 * PostgreSQL

Fine-tuning a pre-trained model of Japanese Tesseract to recognize auxiliary sign in picture.

## Local Deploymnet
#### Contents
- [Installation](#Installation)
- [Model](#model)
- [Build](#build)
- [Run](#run)
- [Result](#result)
- [References](#references)

## Installation
#### Clone repository
 ```console
 git clone https://github.com/tonthatnam/japanese_ocr.git
 cd japanese_ocr
```
## Model
#### Download source code for tesstrain.sh
 ```console
 cd tess
 git clone --depth 1 https://github.com/tesseract-ocr/tesseract.git
 ```
 #### Download source code for all language configuration file
 ```console
 cd tess
 git clone --depth 1 https://github.com/tesseract-ocr/langdata.git
 ```
## Build
#### Docker build
```console
docker-compose up -d --build
```
## Run
#### Run test on local

## Result
#### Find text in pictures
##### Input image

##### Output

#### Get response

## References
#### Articles and guides that cover face_detection
