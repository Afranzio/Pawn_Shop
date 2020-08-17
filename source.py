
mycol=""

def __init__():
    connectDB()

def connectDB():
    import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Shop"]
    mycol = mydb["Pawn"]
    if addCustomer == "" :
        addCustomer()
    elif getCustomer == "" :
        getCustomer()
    elif getInterest == "" :
        getInterest()

def openCV():
    import cv2
    cam = cv2.VideoCapture(1)
    s, im = cam.read() # captures image
    cv2.imshow("Test Picture", im) # displays captured image
    cv2.imwrite("test.bmp",im) # writes image test.bmp to disk

def addCustomer():
    Number = str(input("Number : "))
    Amount = int(input("Amount : "))
    Name = str(input("Name : "))
    Relation = str(input("S/O W/O D/O : "))
    Location = str(input("Location : "))
    Place = str(input("Place : "))
    Item_type = str(input("Item type : "))
    Item = str(input("Item : "))
    Pledged = str(input("Pledged Date : "))
    Weight = int(input("Weight : "))

    mydict={
        "Number" :Number ,
        "Amount" :Amount,
        "Name" :Name,
        "S/O W/O D/O" : Relation ,
        "Location" : Location ,
        "Place" :Place ,
        "Item Type" : Item_type,
        "Item" : Item,
        "Pledged Date" :Pledged,
        "Weight" : Weight
    }

    mycol.insert_one(mydict)

def getCustomer():
    Name = str(input("Enter name to filter : ")).title()

    if Name == "":

        Number = str(input("Enter number to filter : "))
        c = mycol.find({"Number": Number})
        for d in c:
            print(d["Name"])

    a = mycol.find({"Name": Name})

    for b in a:
        print(b)

def getInterest():
    import datetime

    Name = input("Enter Name : ").title()
    a = mycol.find({"Name": Name})

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