import cv2
import time

# start video for create video object
# 0 stand for system inbuilt camera
video = cv2.VideoCapture(0)

# for take time camera 1 s for open give time
time.sleep(1)

# create first frame for compare with all others frame and is None
first_frame = None

#  declare in side loop when loop break video was stopped
while True:
    # ret stand for true or false and frame is nampy arr of pixel
    ret, frame = video.read()

    #  convert frame in to gray scale because gray scale require low size
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    #  for cancel noice, ksize is amount of blur, 0 is SD
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    #  if FF is none we store first frame to compare with others
    if first_frame is None:
        first_frame = gray_frame_gau

    #  we find diff between FF and CF
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    #  create thresh frame
    thresh_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]

    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
