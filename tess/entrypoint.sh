echo "export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/" >> ~/.profile && source ~/.profile
#download jpn_best model
wget https://github.com/tesseract-ocr/tessdata_best/raw/master/jpn.traineddata -O $TESSDATA_PREFIX/jpn_best.traineddata
#change jpn_best to foramat for training LSTM
combine_tessdata -e $TESSDATA_PREFIX/jpn_best.traineddata ~/tess/jpn_best.lstm
