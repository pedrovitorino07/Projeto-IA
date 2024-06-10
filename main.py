import cv2
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

#Cores
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

#classes
class_names = []
with open("coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

#pesos da rede neural
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")

#parâmetros da rede neural
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(608, 608), scale=1/255)

#detectar objetos
def detect_objects(frame):
    start = time.time()
    classes, scores, boxes = model.detect(frame, 0.1, 0.2)
    end = time.time()

    for (classid, score, box) in zip(classes.flatten(), scores.flatten(), boxes):
        color = COLORS[int(classid) % len(COLORS)]
        label = f"{class_names[classid]} : {score}"
        cv2.rectangle(frame, box, color, 2)
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    fps_label = f"FPS: {round((1.0 / (end - start)), 2)}"
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    return frame

#capturar vídeo da webcam
def webcam_detection():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = detect_objects(frame)
        cv2.imshow("detections", frame)
        if cv2.waitKey(1) == 27:  # 27 é o código ASCII para a tecla Esc
            break
    cap.release()
    cv2.destroyAllWindows()

#selecionar e detectar objetos em uma imagem
def image_detection():
    image_path = filedialog.askopenfilename()
    if image_path:
        image_path = os.path.normpath(image_path)
        image = cv2.imread(image_path)
        if image is None:
            messagebox.showerror("Erro", "Não foi possível carregar a imagem. Verifique o caminho do arquivo.")
            return
        frame = detect_objects(image)
        cv2.imshow("detections", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#selecionar e detectar objetos em um vídeo
def video_detection():
    video_path = filedialog.askopenfilename()
    if video_path:
        video_path = os.path.normpath(video_path)
        cap = cv2.VideoCapture(video_path)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = detect_objects(frame)
            cv2.imshow("detections", frame)
            if cv2.waitKey(1) == 27:  # 27 é o código ASCII para a tecla Esc
                break
        cap.release()
        cv2.destroyAllWindows()

#interface gráfica com Tkinter
root = tk.Tk()
root.title("Detector de objetos")

#tamanho da janela
root.geometry("608x608")  # Largura x Altura

btn_webcam = tk.Button(root, text="Detectar pela Camera", command=webcam_detection)
btn_webcam.pack(pady=10)

btn_image = tk.Button(root, text="Detectar em Imagem", command=image_detection)
btn_image.pack(pady=10)

btn_video = tk.Button(root, text="Detectar em Vídeo", command=video_detection)
btn_video.pack(pady=10)

root.mainloop()
