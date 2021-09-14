import cv2
import time
import dropbox
import random

startTime = time.time()

def Capture_Pic():
    Rand = random.randint(0,100)

    vid= cv2.VideoCapture(0)
    result= True

    while (result):
        ret, frame = vid.read()
        imageName= "img" + str(Rand) + ".png"
        cv2.imwrite(imageName, frame)

        startTime = time.time ()

        result = False

    return imageName

    print("Snapshot Taken")
    
    vid.release()
    
    cv2.destroyAllWindows()

def upload_File(imageName):
    access_token = ("sl.A4eMRoQIqYSv3xk8Kl40GKdx57OLVonysexhwliO1zpoqdFrSAv9_v416sm0YzvyMZQVzR6c_FZx5olIqXiJPENBCw2gfysyTh7L2CiZaULvr77nY2IBWmJgx7NqsZdFimX0aJ8")

    file = imageName
    file_from = file
    file2 = "/newFolder/" + str(imageName)

    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file2, mode = dropbox.files.WriteMode.overwrite )
        print("files uploaded")

def main():
    while True:
        if ((time.time()-startTime)>=10):
            pic = Capture_Pic()
            upload_File(pic)

main()

        






