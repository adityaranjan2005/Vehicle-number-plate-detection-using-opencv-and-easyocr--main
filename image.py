import cv2
import os

## xml file
harcascade = "model/haarcascade_russian_plate_number.xml"

## initializing camera
cap = cv2.VideoCapture(0)

## image dimaensions

# width
cap.set(3, 640)

# height
cap.set(4, 480)  

## loading the cadcade
plate_cascade = cv2.CascadeClassifier(harcascade)

## defining area
min_area = 500
count = 0

## creating plate folder
if not os.path.exists('plates'):
    os.makedirs('plates')

while True:
    success, img = cap.read()

   
    if not success:
        print("Error: Unable to read from camera.")
        break

    ##converting imag e to gray scale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detcting plates in the gray image
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:

            ## rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            ## extract the region of interest (ROI)
            img_roi = img[y: y + h, x: x + w]
            
            ##saving image
            plate_image_path = "plates/scanned_img_" + str(count) + ".jpg"
            cv2.imwrite(plate_image_path, img_roi)
            
            count += 1

    ### show the image

    cv2.imshow("Result", img)

    ## stop the loop by pressing 'q' 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
