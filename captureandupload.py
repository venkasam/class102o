import time
import random
import cv2
import dropbox
startime=time.time()
def takeSnapShot() :
    num=random.randint(0,100)
    videocapture=cv2.VideoCapture(0)
    reo=True
    while (reo):
        ret,frame=videocapture.read()
        imgname="img"+str(num)+".png"
        cv2.imwrite(imgname,frame)
        startime=time.time
        reo=False
    return imgname
    print("snapshottaken")
    videocapture.release()
    cv2.destroyAllWindows()

def uploadfile(image):
    acesstoken="DWZ5UYIxHlUAAAAAAAAAAYQk5C_B6GU_W2Pudm_LkPSP-lYJeULZ7pXDj-dVVNOH"
    file=image
    filefrom=file
    fileto="/testfolder/"+(image)
    dbx=dropbox.Dropbox(acesstoken)
    with open(filefrom,"rb") as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print ("fileUploaded")

def main():
    while (True):
        if ((time.time()-startime)>=5):
            name=takeSnapShot()   
            uploadfile(name)
main()