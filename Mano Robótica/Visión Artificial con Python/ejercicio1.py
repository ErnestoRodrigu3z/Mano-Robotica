# Universidad Tecnológica de Tijuana
# Ingeniería en Mecatrónica
# Club de Programación
# Ernesto Rodríguez Corona
# Alonso Contreras Pacheco
# Rebeca Torres Ángeles
# Agregar banderas y contador osiosi
import cv2
import mediapipe as mp
from time import sleep
from pyfirmata import Arduino, SERVO
from scipy.interpolate import interp1d
import numpy as np
Y = [0, 180] #Valores para servo

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
fingerCount = 0
#Declaracion de variables para antirebote de datos

#funciones
def calculate_distance(x1, y1, x2, y2):
    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])
    return np.linalg.norm(p1 - p2)

def detect_finger_down(hand_landmarks, puntoMayor, puntoMenor):
    finger_down = False

    xBaseMenor = int(hand_landmarks.landmark[9].x * width)
    yBaseMenor = int(hand_landmarks.landmark[9].y * height)

    x_index = int(hand_landmarks.landmark[8].x * width)
    y_index = int(hand_landmarks.landmark[8].y * height)
    
    d_base_index = calculate_distance(xBaseMenor, yBaseMenor, x_index, y_index)

    return d_base_index
# Funciones para Dedo Pulgar
def interpolacionPulgar (x,y,z):
    valorServoPulgar = interp1d(x, y)
    return valorServoPulgar (z)

# Funciones para Dedo Indice
def interpolacionIndice (x,y,z):
    valorServoIndice = interp1d(x, y)
    return valorServoIndice (z) 

# Funciones para Dedo Medio
def interpolacionMedio (x,y,z):
    valorServoMedio = interp1d(x, y)
    return valorServoMedio (z)

# Funciones para Dedo anular
def interpolacionAnular (x,y,z):
    valorServoAnular = interp1d(x, y)
    return valorServoAnular (z)

# Funciones para Dedo menhique
def interpolacionMenhique (x,y,z):
    valorServoMenhique = interp1d(x, y)    
    return valorServoMenhique (z)
# For webcam input:
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8) as hands:
  while cap.isOpened():
    success, image = cap.read()
    height, width, _ = image.shape
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

        # Declaramos la variable que mantendra los valores de la posicion en x de los valores xd
        handLandmarks = []

        # Llena la lista con la localización de x, y de los puntos de los dedos
        for landmarks in hand_landmarks.landmark:
          handLandmarks.append([landmarks.x, landmarks.y])        
        #Obtencion de distancia del dedo pulgar
        xPulgar = [-2,1] 
        distanciaPulgar = handLandmarks[4][0] - handLandmarks[3][0]
        valorPulgar = interpolacionPulgar (xPulgar, Y, distanciaPulgar)

        #Obtencion de distancia del dedo indice        
        xIndice = [-2,1]
        distanciaIndice = handLandmarks[8][1] - handLandmarks[6][1]
        valorIndice = interpolacionIndice(xIndice, Y, distanciaIndice)

        #Obtencion de distancia del dedo medio
        xMedio = [-2,1]
        distanciaMedio = handLandmarks[12][1] - handLandmarks[10][1]
        valorMedio = interpolacionMedio(xMedio, Y, distanciaMedio)
        #Obtencion de distancia del dedo anular
        xAnular = [-2,1]
        distanciaAnular = handLandmarks[16][1] - handLandmarks[14][1]
        valorAnular = interpolacionAnular (xAnular, Y, distanciaAnular)

        #Obtencion de distancia del dedo menhique
        xMenhique = [-2,1]
        distanciaMenhique = handLandmarks[20][1] - handLandmarks[18][1]
        valorMenhique = interpolacionMenhique (xMenhique, Y, distanciaMenhique)

        distancia = detect_finger_down(hand_landmarks, 4, 3)
        print (distancia)
        # Dibuja los dedos en la pantalla
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    
    # Muestra la imagen en un ventana
    cv2.imshow('M-CODE Software', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()