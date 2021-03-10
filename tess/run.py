from PIL import Image
import tempfile
import cv2
import imutils
import numpy as np
import subprocess
from utilities.image_process import set_image_dpi_ppi, set_sign_board_region, add_margin, process_text, set_text_region

def run(file_path):
    dection_text = []
    file_path = set_image_dpi_ppi(file_path)
    output, region = set_sign_board_region(file_path)
    for box in region:
        crop_sign_board_img = output[box[1]:box[3],box[0]:box[2]]
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        temp_filename = temp_file.name
        cv2.imwrite(temp_filename, crop_sign_board_img)
        temp_filename = set_image_dpi_ppi(temp_filename)
        crop_sign_board_img = Image.fromarray(crop_sign_board_img)
        output, region = set_text_region(temp_filename)
        for box in region:
            crop_text_region_img = output[min(box[2][1], box[0][1]):max(box[2][1], box[0][1]),min(box[2][0] + 20, box[0][0] + 20):max(box[2][0] - 20, box[0][0] - 20)]
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            temp_filename = temp_file.name
            cv2.imwrite(temp_filename, crop_text_region_img)
            temp_filename = add_margin(temp_filename, 200, 400, 400, 200, (255, 255, 255))
            temp_filename = set_image_dpi_ppi(temp_filename)
            temp_filename = process_text(temp_filename)
            temp_filename = set_image_dpi_ppi(temp_filename)
            args = ["tesseract", "-l", "katakana_15000", temp_filename, "stdout"]
            p1 = subprocess.Popen(args, stdout=subprocess.PIPE)
            rt = p1.communicate()[0].decode().strip().split('\n')
            if rt != ['']:
                #print("not null")
                dection_text = rt + dection_text
            #else:
                #print("null")
        return dection_text
