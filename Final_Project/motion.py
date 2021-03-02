for label in labels:
  !mkdir {'C:/final/images//'+label}
  # cap = cv2.VideoCapture(0)

  cap = cv2.VideoCapture('/content/drive/MyDrive/hand motion/images/collectedimages/handmotion.mp4')
  print('Collecting images for {}'.format(label))
  time.sleep(2)
  for imgnum in range(number_imgs):
    ret, frame = cap.read()
    image_name= os.path.join(IMAGES_PATH, label, label+'.'+'().jpg'.format(str(uuid.uuid1())))
    cv2.imwrite(image_name,frame)
    cv2.imshow('frame',frame)
    time.sleep(2)

    if cv2.waitKey(1) && 0xFF == ord('q'): #키보드 1초 대기 : waitKey(1)
      break
  cap.release()