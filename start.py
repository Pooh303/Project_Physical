#ORIGINAL_CODE_CREDIT:  https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py

#library ที่ต้องใช้สำหรับ face recognition
import face_recognition as face 
import numpy as np 
import cv2
import time

#library ที่ต้องใช้สำหรับ Arduino
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


#ดึงวิดีโอตัวอย่างเข้ามา, ถ้าต้องการใช้webcamให้ใส่เป็น0
video_capture = cv2.VideoCapture(1)

# โหลดรูปภาพใบหน้าที่คุณต้องการรู้จำ
bike_image = face.load_image_file("Train/bike/bike.jpg")
# # แปลงรูปภาพใบหน้าเป็นเวกเตอร์ลักษณะ
bike_face_encoding = face.face_encodings(bike_image)[0]

dream_image = face.load_image_file("Train/dream/dream.jpg")
dream_face_encoding = face.face_encodings(dream_image)[0]

mean_image = face.load_image_file("Train/mean/minny2.jpg")
mean_face_encoding = face.face_encodings(mean_image)[0]

#ประกาศตัวแปร
face_locations = []
face_encodings = []
face_names = []
face_percent = []

#ตัวแปรนี้ใช้สำหรับคิดเฟรมเว้นเฟรมเพื่อเพิ่มfps 
process_this_frame = True

# # สร้างรายชื่อใบหน้าที่รู้จำและเวกเตอร์
known_face_encodings = [bike_face_encoding, dream_face_encoding, mean_face_encoding]
known_face_names = ["BIKE", "DREAM", "MEAN"]


name = ""
command: str = ""

def sendCommand(message):
    command: str = message
    command = command.encode('utf-8')
    serial_inst.write(command)
    time.sleep(1)

#loopคำนวณแต่ละเฟรมของวิดีโอ
while True:
    print("Scanning...")
    time.sleep(1)
    command: str = ""
    command = command.encode('utf-8')
    serial_inst.write(command)

    #อ่านค่าแต่ละเฟรมจากวิดีโอ
    ret, frame = video_capture.read()
    if ret:
        #ลดขนาดสองเท่าเพื่อเพิ่มfps 
        small_frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
        #เปลี่ยน bgrเป็น rgb 
        rgb_small_frame = small_frame[:,:,::-1]

        face_names = []
        face_percent = []

        if process_this_frame:
            #ค้นหาตำแหน่งใบหน้าในเฟรม 
            face_locations = face.face_locations(rgb_small_frame, model="hog") #model="cnn" หรือ "hog"
            #นำใบหน้ามาหาfeaturesต่างๆที่เป็นเอกลักษณ์ 
            face_encodings = face.face_encodings(rgb_small_frame, face_locations)
            
            #เทียบแต่ละใบหน้า
            for face_encoding in face_encodings:
                face_distances = face.face_distance(known_face_encodings, face_encoding)
                best = np.argmin(face_distances)
                face_percent_value = 1-face_distances[best]

                #กรองใบหน้าที่ความมั่นใจ50% ปล.สามารถลองเปลี่ยนได้
                if face_percent_value >= 0.5:
                    name = known_face_names[best]
                    percent = round(face_percent_value*100,2)
                    face_percent.append(percent)
                else:
                    name = "UNKNOWN"
                    face_percent.append(0)
                face_names.append(name)

        #วาดกล่องและtextเมื่อแสดงผลออกมาออกมา
        for (top,right,bottom, left), name, percent in zip(face_locations, face_names, face_percent):
            top*= 2
            right*= 2
            bottom*= 2
            left*= 2

            if name == "UNKNOWN":
                print(name)
                color = [46,2,209]
                sendCommand("UNKNOWN")
            else:
                print(name)
                color = [255,102,51]
                if name == "BIKE":
                    sendCommand("BIKE")
                elif name == "DREAM":
                    sendCommand("DREAM")
                elif name == "MEAN":
                    sendCommand("MEAN")

            cv2.rectangle(frame, (left,top), (right,bottom), color, 2)
            cv2.rectangle(frame, (left-1, top -30), (right+1,top), color, cv2.FILLED)
            cv2.rectangle(frame, (left-1, bottom), (right+1,bottom+30), color, cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left+6, top-6), font, 0.6, (255,255,255), 1)
            cv2.putText(frame, "MATCH: "+str(percent)+"%", (left+6, bottom+23), font, 0.6, (255,255,255), 1)


        #สลับค่าเป็นค่าตรงข้ามเพื่อให้คิดเฟรมเว้นเฟรม
        process_this_frame = not process_this_frame

        # แสดงผลลัพท์ออกมา
        # cv2.imshow("Video", frame)
        # if cv2.waitKey(200) & 0xFF == ord('q'):
        #     break

    else:
        break

#ล้างค่าต่างๆเมื่อปิดโปรแกรม
video_capture.release()
cv2.destroyAllWindows()
