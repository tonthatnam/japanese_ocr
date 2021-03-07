from PIL import Image
import tempfile
import cv2
import imutils
import numpy as np

def set_image_dpi_ppi(file_path):
    im = Image.open(file_path)
    length_x, width_y = im.size
    factor = float(length_x/width_y)
    size = int(600), int(600/factor)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(800, 800))
    return temp_filename

def set_sign_board_region(file_path):
    image = cv2.imread(file_path)
    height = image.shape[0]
    width = image.shape[1]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.bilateralFilter(gray, 25, 15, 15)
    thresh = cv2.threshold(blurred, 110, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite("result/thresh.png", thresh)
    output = image.copy()
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    region = []
    for c in cnts:
        epsilon = 0.02 * cv2.arcLength(c, True)
        c = cv2.approxPolyDP(c, epsilon, True)
        area = cv2.contourArea(c)
        print(height, width)
        print(height*width)
        if area < int(height*width/3):
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),2)
        region.append((x,y,x+w,y+h))
    return output, region

def add_margin(file_path, top, right, bottom, left, color):
    image = Image.open(file_path)
    width, height = image.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(image.mode, (new_width, new_height), color)
    result.paste(image, (left, top))
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_filename = temp_file.name
    result.save(temp_filename, dpi=(800, 800))
    return temp_filename

def process_text(file_path):
    image = cv2.imread(file_path)
    height = img.shape[0]
    width = img.shape[1]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.bilateralFilter(gray, 25, 15, 15)
    thresh = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)[1]
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_filename = temp_file.name
    cv2.imwrite(temp_filename, thresh)
    return temp_filename
