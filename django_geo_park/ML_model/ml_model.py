from ultralytics import YOLO
from PIL import Image
import cv2
from keras.models import load_model


def ml():
    model = YOLO('../geo_park/best.pt')
    im1 = Image.open("../geo_park/kvarc_mineral_2.jpg")
    results = model.predict(source=im1, save=True)
    print(results)