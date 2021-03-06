#!/bin/bash
echo "export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/" >> ~/.profile && source ~/.profile
#download jpn_best model
wget https://github.com/tesseract-ocr/tessdata/raw/master/jpn.traineddata -P $TESSDATA_PREFIX
wget https://github.com/tesseract-ocr/tessdata_best/raw/master/eng.traineddata -O $TESSDATA_PREFIX/eng_best.traineddata
wget https://github.com/tesseract-ocr/tessdata_best/raw/master/jpn.traineddata -O $TESSDATA_PREFIX/jpn_best.traineddata
wget https://github.com/tesseract-ocr/tessdata_best/raw/master/jpn_vert.traineddata -P $TESSDATA_PREFIX
#change jpn_best to foramat for training LSTM
combine_tessdata -e $TESSDATA_PREFIX/jpn_best.traineddata jpn_best.lstm
#pwd
#ls
#tesseract --list-langs
#tesseract -l jpn_best tests/test1.png stdout
