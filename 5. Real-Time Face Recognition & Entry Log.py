##from pydrive.auth import GoogleAuth
##from pydrive.drive import GoogleDrive
import cv2
import sys
from mail import sendEmail
from flask import Flask, render_template, Response
from camera import VideoCamera
from imutils.video.pivideostream import PiVideoStream
import time
from skimage.feature import hog
from skimage import feature
from skimage import data, exposure
import threading
import pickle
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#email_update_interval = 2 # sends an email only once in this time interval
video_camera = VideoCamera(flip=True) # creates a camera object, flip vertically
object_classifier = cv2.CascadeClassifier("models/face_detection2.xml") # an opencv classifier

# App Globals (do not edit)
app = Flask(__name__)
last_epoch = 0
##gauth = GoogleAuth()
### Try to load saved client credentials
##gauth.LoadCredentialsFile("mycreds.txt")
##if gauth.credentials is None:
##    # Authenticate if they're not there
##    gauth.LocalWebserverAuth()
##elif gauth.access_token_expired:
##    # Refresh them if expired
##    gauth.Refresh()
##else:
##    # Initialize the saved creds
##    gauth.Authorize()
### Save the current credentials to a file
####gauth.SaveCredentialsFile("mycreds.txt")
##
##drive = GoogleDrive(gauth)

f=open('log_entry.txt','w');
f.close()
os.remove('log_entry.txt');
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
client = gspread.authorize(creds)


sheet = client.open("log").sheet1

def recog():
        a=time.time()
        #frame, found_obj = video_camera.get_object(object_classifier)
        no, frame = video_camera.get_frame()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #gray = cv2.resize(gray,(100,100)) 
        faces = object_classifier.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
                )
        box=[]
        
        for (x, y, w, h) in faces:
                #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
                box.append(x)
                box.append(y)
                box.append(h)
                box.append(w)
                
                if len(box)!=0:
                        crop_img = gray[box[1]:box[1]+box[2], box[0]:box[0]+box[3]]
                        crop_img=cv2.resize(crop_img,(128,128))
                        clf = pickle.load(open('svm.pickle', 'rb'))
                        (h, hogImage) = feature.hog(crop_img, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2, 2), transform_sqrt=True, visualise=True)
                        
                        c=hstr.split(',')
                        c=c[:-1]
                        Z=[c]
                        z = clf.predict(Z)
                        confidence = clf.predict_proba(Z)
                        f=open('log_entry.txt','a')
                        t=time.localtime()
                        s=''
                        t_ime = str(t[3])+':'+str(t[4])+':'+str(t[5])
                        d_ate =  str(t[2])+'/'+str(t[1])+'/'+str(t[0])
                                        
                        #print(confidence[0])
                        if len(faces) >= 1:
                                if z[0]==1 and confidence[0][0] >= 0.70:
                                        print('Rahul')
                                        s=str(01)+','+str(t[3])+':'+str(t[4])+':'+str(t[5])+','+str(t[2])+'/'+str(t[1])+'/'+str(t[0])+'\n'
                                        i_d=1
                                        sheet.insert_row([i_d, t_ime, d_ate],index=2)
                                        f.write(s)
                                elif z[0]==2 and confidence[0][1] >= 0.70:
                                        print('Prabhas')
                                        s=str(02)+','+str(t[3])+':'+str(t[4])+':'+str(t[5])+','+str(t[2])+'/'+str(t[1])+'/'+str(t[0])+'\n'
                                        i_d=2
                                        sheet.insert_row([i_d, t_ime, d_ate],index=2)        
                                        f.write(s)
                                elif z[0]==3 and confidence[0][2] >= 0.70:
                                        print('Aashirvad')
                                        s=str(03)+','+str(t[3])+':'+str(t[4])+':'+str(t[5])+','+str(t[2])+'/'+str(t[1])+'/'+str(t[0])+'\n'
                                        i_d=3
                                        sheet.insert_row([i_d, t_ime, d_ate],index=2)
                                        f.write(s)
                                elif z[0]==4 and confidence[0][3] >= 0.70:
                                        print('Vinay')
                                        s=str(04)+','+str(t[3])+':'+str(t[4])+':'+str(t[5])+','+str(t[2])+'/'+str(t[1])+'/'+str(t[0])+'\n'
                                        i_d=4
                                        sheet.insert_row([i_d, t_ime, d_ate],index=2)
                                        f.write(s)
                                else:
                                        print('Unknown')
                                        s=str(-1)+','+str(t[3])+':'+str(t[4])+':'+str(t[5])+','+str(t[2])+'/'+str(t[1])+'/'+str(t[0])+'\n'

                                        s1='Unknown'+'/'+'1.jpg'
                                        cv2.imwrite(s1, crop_img)
##                                        file2 = drive.CreateFile()
##                                        file2.SetContentFile('Unknown/1.jpg')
##                                        file2.Upload()
                                        
                                        i_d=-1
                                        sheet.insert_row([i_d, t_ime, d_ate],index=2)
                                        f.write(s)
                        f.close()
                box=[]        
        print(time.time()-a)

def check_for_objects():
	global last_epoch
	while True:
		recog()
			

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame , a = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    t = threading.Thread(target=check_for_objects, args=())
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', debug=False)
