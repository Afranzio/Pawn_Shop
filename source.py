import eel

##Select The Folder of FrontEnd File
eel.init("web")


@eel.expose
def connectDB():
    
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Shop"]
    global mycol
    mycol = mydb["Pawn"]

def addData():
    import json
    with open(r'./Data/data.json') as f: #Enter your data.json file path
        data = json.load(f)
    len(data["main"])
    for each in data["main"]:
        mycol.insert_one(each)


@eel.expose
def fetchUser(name, number):
#     Name = str(input("Enter name to filter : ")).title()
    print("working", name.title(), number)
    c = mycol.find({"Name":name.title(), "Number": number})
    for d in c:
        print(d)
        return(d)
    
def fetchImg(imgID):
    
    # Imports PIL module 
    from PIL import Image 

    # open method used to open different extension image file 
    im = Image.open(r"./photos/"+imgID+".jpg") 

    # This method will show image in any image viewer 
    im.show()

@eel.expose   
def newUser(Number, Amount,Name,Relation,Location,Place,Item,itemType, mobile, Pledged,Weight):
    mydict={
        "Number" :Number ,
        "Amount" :Amount,
        "Name" :Name,
        "S/O W/O D/O" : Relation ,
        "Location" : Location ,
        "Place" :Place ,
        "Item" : Item,
        "Item Type" : itemType,
        "Mobile" : mobile,
        "Pledged Date" :Pledged,
        "Weight" : Weight
    }

    mycol.insert_one(mydict)
    
def interestCal(Name):
    import datetime

#     Name = input("Enter Name : ").title()
    a = mycol.find({"Name": Name.title()})

    for i in a:

        rates=0

        if i['Item'] == "G":
            rates=0.03
        else:
            rates=0.02

        date = i["Pledged Date"]
        amount = int(i["Amount"])
        interest=amount*rates
        final = date.replace('.','')
        date_str = final
        format_str = '%d%m%y' # The format
        datetime_obj = datetime.datetime.strptime(date_str, format_str).date()
        # print(datetime_obj)

        curent=datetime.datetime.now().date()

        surrendered = curent - datetime_obj

        check= surrendered.days/30

        print("₹",i['Amount'], "--" ,"₹",int(check*interest), "--" , i['Item'], "--" , i['Weight'] )


@eel.expose
def capture(Name):
    import cv2 

    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd 
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename=Name+'.jpg', img=frame)
                webcam.release()
                img_new = cv2.imread('person.jpg', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
    #             print("Processing image...")
    #             img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
    #             print("Converting RGB image to grayscale...")
    #             gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
    #             print("Converted RGB image to grayscale...")
    #             print("Resizing image to 28x28 scale...")
    #             img_ = cv2.resize(gray,(280,280))
    #             print("Resized...")
    #             img_resized = cv2.imwrite(filename='./'+ Name +'Person1.jpg', img=img_)
    #             print("Image saved!")
            
                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
        
capture("Mani")
    

eel.start('index.html',size = (1024,500),cmdline_args=['--start-fullscreen'])