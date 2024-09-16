import cv2
import pytesseract
import pandas as pd
import os

# teseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# plates folder path
plates_folder = 'plates'

# storing csv folder path
csv_file_path = os.path.join(plates_folder, 'license_plate_numbers.csv')

# empty list to store 
license_plate_numbers = []

def extract_text_from_image(image_path):


    ## reading the image using opencv
    image = cv2.imread(image_path)


    ##convertying the image to gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    ## use Tesseract to do OCR on the gray scale image
    text = pytesseract.image_to_string(gray_image)
    return text.strip()

# image processing
for filename in os.listdir(plates_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        ## full file path
        image_path = os.path.join(plates_folder, filename)

        ##extract text from the image
        text = extract_text_from_image(image_path)
        license_plate_numbers.append({'Image Name': filename, 'License Plate Number': text})

## converting into dataframe
df = pd.DataFrame(license_plate_numbers)

## csv file save
df.to_csv(csv_file_path, index=False)

print(f'License plate numbers have been saved to {csv_file_path}')
