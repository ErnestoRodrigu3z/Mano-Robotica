# Universidad Tecnológica de Tijuana
# Ingeniería en Mecatrónica
# Club de Programación
# Ernesto Rodríguez Corona
# Alonso Contreras Pacheco
# Rebeca Torres Ángeles
# Agregar banderas y contador osiosi
import cv2
import mediapipe as mp
import serial as arduino
import time
Arduino = arduino.Serial ('COM5', 9600)
time.sleep(2)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
fingerCount = 0
#Declaracion de variables para antirebote de datos
banderaPulgarArriba = False
banderaPulgarAbajo = False
banderaIndiceArriba = False
banderaIndiceAbajo = False
banderaMedioArriba = False 
banderaMedioAbajo = False
banderaAnularArriba = False
banderaAnularAbajo = False
banderaMenhiqueArriba = False
banderaMenhiqueAbajo = False
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Initially set finger count to 0 for each cap    

    if results.multi_hand_landmarks:

      for hand_landmarks in results.multi_hand_landmarks:
        # Get hand index to check label (left or right)
        handIndex = results.multi_hand_landmarks.index(hand_landmarks)
        handLabel = results.multi_handedness[handIndex].classification[0].label

        # Set variable to keep landmarks positions (x and y)
        handLandmarks = []

        # Fill list with x and y positions of each landmark
        for landmarks in hand_landmarks.landmark:
          handLandmarks.append([landmarks.x, landmarks.y])

        # Test conditions for each finger: Count is increased if finger is 
        #   considered raised.
        # Thumb: TIP x position must be greater or lower than IP x position, 
        #   deppeding on hand label.
        if (handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]) and banderaPulgarArriba == False:
          Arduino.write(b'1')
          fingerCount += 1
          banderaPulgarArriba = True
          banderaPulgarAbajo = False
        elif (handLabel == "Left" and handLandmarks[4][0] < handLandmarks[3][0]) and banderaPulgarAbajo == False:
          Arduino.write(b'2')
          fingerCount -= 1
          banderaPulgarArriba = False
          banderaPulgarAbajo = True           
        if (handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]) and banderaPulgarArriba == False:
          Arduino.write(b'1')
          fingerCount += 1
          banderaPulgarArriba = True
          banderaPulgarAbajo = False
        elif (handLabel == "Right" and handLandmarks[4][0] > handLandmarks[3][0]) and banderaPulgarAbajo == False:
          Arduino.write(b'2')
          fingerCount -= 1
          banderaPulgarArriba = False
          banderaPulgarAbajo = True
        # Other fingers: TIP y position must be lower than PIP y position, 
        #   as image origin is in the upper left corner.
        if (handLandmarks[8][1] < handLandmarks[6][1]) and banderaIndiceArriba == False:       #Index finger
            fingerCount += 1          
            Arduino.write(b'A')
            banderaIndiceArriba = True
            banderaIndiceAbajo = False
        if (handLandmarks [8][1] > handLandmarks [6][1]) and banderaIndiceAbajo == False:
            fingerCount -= 1
            Arduino.write(b'B')
            banderaIndiceArriba = False
            banderaIndiceAbajo = True
        if (handLandmarks[12][1] < handLandmarks[10][1]) and banderaMedioArriba == False:     #Middle finger
            Arduino.write(b'C')
            fingerCount += 1
            banderaMedioArriba = True
            banderaMedioAbajo = False
        if (handLandmarks[12][1] > handLandmarks[10][1]) and banderaMedioAbajo == False:     #Middle finger
            Arduino.write(b'D')
            fingerCount -= 1
            banderaMedioArriba = False
            banderaMedioAbajo = True           
        if (handLandmarks[16][1] < handLandmarks[14][1]) and banderaAnularArriba == False:     #Ring finger
            Arduino.write(b'E')
            fingerCount += 1
            banderaAnularArriba = True
            banderaAnularAbajo = False
        if (handLandmarks[16][1] > handLandmarks[14][1]) and banderaAnularAbajo == False:     #Ring finger
            Arduino.write(b'G')
            fingerCount -= 1
            banderaAnularArriba = False
            banderaAnularAbajo = True                                    
        if (handLandmarks[20][1] < handLandmarks[18][1]) and banderaMenhiqueArriba == False:     #Pinky
            Arduino.write (b'J')            
            fingerCount += 1
            banderaMenhiqueArriba = True
            banderaMenhiqueAbajo = False
        if (handLandmarks[20][1] > handLandmarks[18][1]) and banderaMenhiqueAbajo == False:     #Pinky
            Arduino.write (b'K')            
            fingerCount -= 1
            banderaMenhiqueArriba = False
            banderaMenhiqueAbajo = True           

        # Draw hand landmarks 
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    # Display finger count
    cv2.putText(image, str(fingerCount), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)

    # Display image
    cv2.imshow('Deteccion de manos', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
Arduino.close()
cap.release()