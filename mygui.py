import PySimpleGUI as sg
from twilio.rest import Client
import ImageGenerator
import letsgo

def sendAiImages(phonenumber, promptStringList):
    account_sid = 'AC20dd6ee6e1757acbb77659101963a8c8'
    auth_token = '70a2e1f815eb503bc6c84bcf0913df7a'
    client = Client(account_sid, auth_token)

    links = ImageGenerator.main(promptStringList)

    for x in range(len(links)):
        message = client.messages \
                        .create(
                            body=links[x],
                            from_='+18658004332',
                            to=phonenumber
                        )

sg.theme("DarkBlue3")

firstName = ""
lastName = ""
phoneNum = ""
lowlist = letsgo.web_scraper()

layout = [
    [sg.Text("Hello. Welcome to MyCamp, your one stop shop for all camping purposes. Here, you can use our updated checklist to make sure you dont' miss any fundamentals for camping, and can also get some really cool AI camping generated images.")],
    [sg.Text("Enter First Name: ", size=(25,1))],
    [sg.InputText(do_not_clear=False)],
    [sg.Text("Enter Last Lame: ", size=(25,1))],
    [sg.InputText(do_not_clear=False)],
    [sg.Text("Enter Phone Number: ", size=(25,1))],
    [sg.InputText(do_not_clear=False)],
    [sg.Text("Enter Phrase for AI Generated Object: ", size=(35,1))],
    [sg.InputText(do_not_clear=False)],
    [sg.Checkbox("Tent", default=False)],
    [sg.Checkbox("Backpack", default=False)],
    [sg.Checkbox("Sleeping Bag", default=False)],
    [sg.Checkbox("Flashlight", default=False)],
    [sg.Checkbox("Sleeping Pad", default=False)],
    [sg.Checkbox("Pillow", default=False)],
    [sg.Checkbox("First Aid Kit", default=False)],
    [sg.Button("OK")]
]

window = sg.Window("Demo", layout)

while True:
    event, values = window.read()

    if event == 'OK'or event == sg.WIN_CLOSED:
        firstName = values[0]
        lastName = values[1]
        phoneNum = values[2]
        userString = "Camping " + values[3]
        tent = values[4]
        backpack = values[5]
        sleeping_bag = values[6]
        flashlight = values[7]
        sleeping_pad = values[8]
        pillow = values[9]
        toilet_paper = values[10]
    
    validNums = []
    if tent == True:
        validNums.append(0)
    if backpack == True:
        validNums.append(1)
    if sleeping_bag == True:
        validNums.append(2)
    if flashlight == True:
        validNums.append(3)
    if sleeping_pad == True:
        validNums.append(4)
    if pillow == True:
        validNums.append(5)
    if toilet_paper == True:
        validNums.append(6)


        print("First Name: ", firstName)
        print("Last Name: ", lastName)
        print("Phone Num: ", phoneNum)

        print("Box1", tent)
        print("Box2", backpack)
        print("Box3", sleeping_bag)
        print("Box4", flashlight)
        print("Box5", sleeping_pad)
        print("Box6", pillow)
        print("Box7", toilet_paper)
        #print(lowlist)

        break
window.close()

import PySimpleGUI as sg2
sg2.theme("DarkBlue3")

layout2 = []
layout2Words = ["Best Camping Tent:", "Best Camping Backpack:", "Best Camping Sleeping Bag:", "Best Camping Flashlight:", "Best Camping Sleeping Pad:", "Best Camping Pillow:", "Best First Aid Kit:"]
for i in range (len(validNums)):
    myStr = layout2Words[i] + " " + str(lowlist[validNums[i]])
    layout2.append([sg2.Text(myStr)])
layout2.append([sg2.Button("OK")])

window2 = sg2.Window("Demo", layout2)
while True:
    event, values = window2.read()
    break

sendAiImages(phoneNum,userString.split())



