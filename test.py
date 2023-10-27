# https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py
import face_recognition as face
import numpy as np
import cv2
import time

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serial_inst = serial.Serial()
ports_list = []

for port in ports:
    ports_list.append(str(port))
    print(str(port))

val: str = input('Select Port: COM')
# val: str = '3'

for i in range(len(ports_list)):
    if ports_list[i].startswith(f'COM{val}'):
        port_var = f'COM{val}'
        # print(port_var)

serial_inst.baudrate = 9600
serial_inst.port = port_var
serial_inst.open()


# เปิดกล้องหรือวิดีโอ
video_capture = cv2.VideoCapture(0)

# โหลดรูปภาพใบหน้าที่คุณต้องการรู้จำ
bike_image = face.load_image_file("Train/bike/bike.jpg")
dream_image = face.load_image_file("Train/dream/dream.jpg")
minny_image = face.load_image_file("Train/mean/minny2.jpg")

# แปลงรูปภาพใบหน้าเป็นเวกเตอร์ลักษณะ
bike_face_encoding = face.face_encodings(bike_image)[0]
dream_face_encoding = face.face_encodings(dream_image)[0]
minny_face_encoding = face.face_encodings(minny_image)[0]

# สร้างรายชื่อใบหน้าที่รู้จำและเวกเตอร์
known_face_encodings = [bike_face_encoding, dream_face_encoding, minny_face_encoding]
known_face_names = ["Bike", "Dream", "Minny"]

name = ""
command: str = ""

while True:
    time.sleep(1)
    command = ""
    command = command.encode('utf-8')
    serial_inst.write(command)
    ret, frame = video_capture.read()
    if not ret:
        break

    # ลดขนาดเฟรมเพื่อเพิ่มประสิทธิภาพ
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face.face_locations(rgb_small_frame)
    face_encodings = face.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    face_percent = []

    for face_encoding in face_encodings:
        # เปรียบเทียบใบหน้าในวิดีโอกับใบหน้าที่รู้จำ
        face_distances = face.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        face_percent_value = 1 - face_distances[best_match_index]

        if face_percent_value >= 0.5:
            name = known_face_names[best_match_index]
            percent = round(face_percent_value * 100, 2)
        else:
            name = "UNKNOWN"
            percent = 0

        face_names.append(name)
        face_percent.append(percent)

    # วาดกล่องรอบใบหน้าและแสดงชื่อและเปอร์เซ็นต์บนวิดีโอ
    for (top, right, bottom, left), name, percent in zip(face_locations, face_names, face_percent):
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        if name == "UNKNOWN":
            print(name)
            color = [46,2,209]  # สีแดงสำหรับใบหน้าที่ไม่รู้จำ
            # command = "OFF"
            # serial_inst.write(command.encode('utf-8'))
        else:
            print(name)
            color = [255,102,51]  # สีฟ้าสำหรับใบหน้าที่รู้จำ
            command: str = "DETECTED"
            command = command.encode('utf-8')
            serial_inst.write(command)
            

        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, color, 1)
        cv2.putText(frame, f"MATCH: {percent}%", (left + 6, bottom + 23), font, 0.5, color, 1)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
video_capture.release()
cv2.destroyAllWindows()

#testGit
