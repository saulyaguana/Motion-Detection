import streamlit as st
import cv2
import numpy as np
from motion import VideoMotion, OpError

st.title("Aplicación de OpenCV con Detección de Movimiento")

# Selección de cámara
device_options = {"Webcam interna": 0, "Cámara externa": 1}
device_name = st.selectbox("Selecciona el dispositivo de video", list(device_options.keys()))
device_index = device_options[device_name]

# Inicializar detección de movimiento
motion_detector = VideoMotion(history=100, path=device_index)

# Crear contenedores para las imágenes
col1, col2 = st.columns(2)
frame_placeholder1 = col1.empty()
frame_placeholder2 = col2.empty()

start = st.button("Iniciar cámara")
stop = st.button("Detener cámara")

if start:
    motion_detector.motion_detection()

if stop:
    st.write("Cámara detenida")