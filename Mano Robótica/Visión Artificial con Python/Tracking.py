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
valorNuevo = 'A1B1C1D1E1'
valorActual = 'A0B0C0D0E0'
valoresDedos = [1,1,1,1,1] 
def manoLevantada ():

   return    
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
        if ((handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]) or (handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0])):
           valoresDedos[0] = 1
        else:
           valoresDedos [0] = 0

        # Other fingers: TIP y position must be lower than PIP y position, 
        #   as image origin is in the upper left corner.
        if (handLandmarks[8][1] < handLandmarks[6][1]):       #Index finger       
            valoresDedos [1] = 1
        else:
           valoresDedos [1] = 0          
        if (handLandmarks[12][1] < handLandmarks[10][1]):     #Middle finger
           valoresDedos[2] = 1
        else:
           valoresDedos [2] = 0
        if (handLandmarks[16][1] < handLandmarks[14][1]):     #Ring finger
           valoresDedos [3] = 1
        else:
           valoresDedos [3] = 0                                    
        if (handLandmarks[20][1] < handLandmarks[18][1]):     #Pinky
           valoresDedos [4] = 1
        else:
           valoresDedos [4] = 0                  
        valorNuevo = 'IA' + str(valoresDedos[0]) + 'B' + str(valoresDedos[1]) + 'C'+ str(valoresDedos[2]) + 'D'+ str(valoresDedos[3]) + 'E' + str(valoresDedos[4]) + ","
        if (valorActual != valorNuevo):
            Arduino.write(valorNuevo.encode("ascii"))
            print (valorNuevo)
            valorActual = valorNuevo        
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