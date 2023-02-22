# Universidad Tecnológica de Tijuana
# Ingeniería en Mecatrónica
# Club de Programación
# Ernesto Rodríguez Corona
# Kenia Angulo Varela
# Juan de Dios Villa Carbajal
# Jesús Alfonso Rodríguez
# Ejercicio 1
import math
import cv2
import mediapipe as mp
import time
import SeguimientoManos as sm
detector = sm.detectormanos(Confdeteccion=0.75)
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
tip = [4,8,12,16,20]
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,255,255), thickness=3, circle_radius=5),
                    mp_drawing.DrawingSpec(color=(255,0,255), thickness=4, circle_radius=5))
        cv2.imshow('Deteccion de mano',frame)
        #Encontrar la posicion
        xlista = []
        ylista = []
        bbox = []
        lista = []
        if results.multi_hand_landmarks:
            miMano = results.multi_hand_landmarks[0]
            for id, lm in enumerate(miMano.landmark):
                alto, ancho, c = frame.shape  # Extraemos las dimensiones de los fps
                cx, cy = int(lm.x * ancho), int(lm.y * alto)  # Convertimos la informacion en pixeles
                xlista.append(cx)
                ylista.append(cy)
                lista.append([id, cx, cy])
                if True:
                    cv2.circle(frame,(cx, cy), 3, (0, 0, 0), cv2.FILLED)  # Dibujamos un circulo
            xmin, xmax = min(xlista), max(xlista)
            ymin, ymax = min(ylista), max(ylista)
            bbox = xmin, ymin, xmax, ymax
            if True:
                # Dibujamos cuadro
                cv2.rectangle(frame,(xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0,255,0),2)

        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()