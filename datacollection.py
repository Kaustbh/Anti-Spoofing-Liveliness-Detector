from cvzone.FaceDetectionModule import FaceDetector
import cv2
import cvzone
import mediapipe as mp
from time import time
####################################################

classId=0 # 0 for fake , 1 for real
outputFolderPath='Datasets/Datacollect'
confidence = 0.8
# For increasing the height and weight of the rectangle
offsetPercentageW=10
offsetPercentageH=10

debug=False
# 640,480
camwidth,camheight=720,540
floatingpoint=6
save=True
blurThreshold=35  # Larger is more Focus

####################################################

# Initialize the webcam
# '2' means the third camera connected to the computer, usually 0 refers to the built-in webcam
cap = cv2.VideoCapture(0)
cap.set(3,camwidth)
cap.set(4,camheight)

# Initialize the FaceDetector object
# minDetectionCon: Minimum detection confidence threshold
# modelSelection: 0 for short-range detection (2 meters), 1 for long-range detection (5 meters)
detector = FaceDetector(minDetectionCon=0.5, modelSelection=0)

# Run the loop to continually get frames from the webcam
while True:
 # Read the current frame from the webcam
        # success: Boolean, whether the frame was successfully grabbed
        # img: the captured frame
        success, img = cap.read()
        imgout=img.copy()

        # Detect faces in the image
        # img: Updated image
        # bboxs: List of bounding boxes around detected faces
        img, bboxs = detector.findFaces(img, draw=False)
        
        listBlur=[]    # True False values indicating if the faces are blur or not 
        listInfo=[]    # The Normalized values and the class name for the label txt file

        # Check if any face is detected
        if bboxs:
            # Loop through each bounding box
            for bbox in bboxs:
                # bbox contains 'id', 'bbox', 'score', 'center'

                # ---- Get Data  ---- #
                # center = bbox["center"]
                x, y, w, h = bbox['bbox']
                score = bbox['score'][0]
                
                 #------ Check the Score --------#
                if score>confidence:

                    # width 
                    offsetW = (offsetPercentageW/100)*w
                    x=int(x-offsetW)
                    w=int(w+offsetW*2)

                    # height
                    offsetH = (offsetPercentageH/100)*h
                    y=int(y-offsetH*3.2)
                    h=int(h+offsetH*3.5)
                    
                    #------ To avoid values below 0 --------#
                    
                    if x<0: x=0
                    if y<0: y=0
                    if w<0: w=0
                    if h<0: h=0
                    #------ Find Blurriness --------#
                    
                    #----- Find the Face -----#
                    
                    imgface=img[y:y+h,x:x+w]
                    # cv2.imshow("img",imgface)
                    blurvalue=int(cv2.Laplacian(imgface,cv2.CV_64F).var())

                    if blurvalue>blurThreshold:
                         listBlur.append(True)
                    
                    else:
                         listBlur.append(False)
                    
                    #----- Normalize Values -----#
                    
                    ih, iw, _ =img.shape
                    xc,yc = x+w/2 , y+h/2
                    # print(xc,yc)
                    xcn = round(xc/iw,floatingpoint)
                    ycn = round(yc/ih,floatingpoint)

                    wn = round(w/iw,floatingpoint)
                    hn = round(h/ih,floatingpoint)

                    #----- To avoid values above 1 -----#

                    if xcn>1: xcn=1
                    if ycn>1: ycn=1
                    if wn>1: wn=1
                    if hn>1: hn=1 
                    

                    listInfo.append(f"{classId} {xcn} {ycn} {wn} {hn}\n")


                    # ---- Draw Data  ---- #
                    # cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
                    # cvzone.putTextRect(img, f'{score}%', (x, y - 10))
                    # cvzone.cornerRect(img, (x, y, w, h))
                    cv2.rectangle(imgout,(x,y,w,h),(255,0,0),3)
                    cvzone.putTextRect(imgout,f'Score:{int(score*100)}% Blur: {blurvalue}',(x,y-12),scale=2,thickness=2)
                    
                    if debug:
                        cv2.rectangle(img,(x,y,w,h),(255,0,0),3)
                        cvzone.putTextRect(img,f'Score:{int(score*100)}% Blur: {blurvalue}',(x,y-12),scale=2,thickness=2)


            # ---- To Save  ---- #
            if save:

                if all(listBlur) and listBlur!=[]:
                
                 # ---- Save Image  ---- #

                 timenow =time()  # For getting unique images names , so avoid conflict

                 timenow=str(timenow).split('.')
                 timenow=timenow[0]+timenow[1]
                 print(timenow)

                 cv2.imwrite(f"{outputFolderPath}/{timenow}.jpg",img)
                 
                 # ---------- save label and text file ------------ #

                 for info in listInfo:
                      
                      f=open(f"{outputFolderPath}/{timenow}.txt",'a')
                      f.write(info)
                      f.close()

                     

        # Display the image in a window named 'Image'
        cv2.imshow("Image", imgout)
        if cv2.waitKey(25) & 0xFF ==ord('q'):
               break