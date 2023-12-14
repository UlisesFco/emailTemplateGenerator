 #  Archivo de python de la aplicación emailTemplateGenerator.
 #
 #  @author     Ulises Francisco Alejandre Navarro
 #  @since      2023-12-14
 #  @licence    MPL 2.0
 # 
 #  Este codigo fuente está sujeto a los términos de la Licencia Pública
 #  de Mozilla, v. 2.0. Si una copia de la licencia no fue distribuída con
 #  este archivo, la puede encontrar en http://mozilla.org/MPL/2.0/.


import PySimpleGUI as sg
import pyperclip as pc
from pathlib import Path
import webbrowser as wb
import pandas as pd
import csv
import os

names = []
adds = []
text_box = []

exists = os.path.exists('appAdd.csv')
if not exists:
    myfile = Path("appAdd.csv")
    myfile.touch(exist_ok=True)
    f = open(myfile, 'w')
    f.write('NAME,ADDRESS')
    f.close()

df = pd.read_csv('appAdd.csv')
sorted_df = df.sort_values(['NAME', 'ADDRESS'])
sorted_df.to_csv('appAdd.csv', index=False)

with open('appAdd.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        names.append(row[0])
        adds.append(row[1])
        text_box.append(row[0] + ', ' + row[1])

sg.theme("LightGreen")

left_col = [
    [sg.Text("Input data to generate email:")],
    [sg.Text("Enter delivery order number")],
    [sg.Text("Enter pickup address")],
    [sg.Text("Enter pickup's additional details (phone, name, etc.)")],
    [sg.Text("Enter pickup appointment date and time")],
    [sg.Text("Enter carrier")],
    [sg.Text("Enter driver")],
    [sg.Text("Enter driver's phone")],
    [sg.Text("Enter rate")],
    [sg.Text("Enter notes")],

    [sg.Text("Enter weight")],
    [sg.Text("Enter quantity")],
    [sg.Text("Enter temperature (°F)")],
    [sg.Text("Enter palets")],

    [sg.Text("")],
    [sg.Text("Appointment details (separated by commas if there's multiple entries):")],
    [sg.Text("Enter app. number")],
    [sg.Text("Enter app. expected delivery date and time")],
    [sg.Text("Enter SO")],
    [sg.Text("Enter PO")],
    [sg.Text("Enter app. destination names")],
    [sg.Text("Enter app. destination address")],
    [sg.Text("")],
    # [sg.Text("")],
    [sg.Button("Generate e-mail", key="-SEND-")]
]

right_col = [
    [sg.Text("")],
    [sg.In(size=(67, 0), enable_events=True, key="-DEL_NUM-")],
    [sg.In(size=(67, 0), enable_events=True, key="-PU_ADD-")],
    [sg.In(size=(67, 0), enable_events=True, key="-ADD_DET-")],
    [sg.In(size=(67, 0), enable_events=True, key="-PU_DATE-")],
    [sg.In(size=(67, 0), enable_events=True, key="-CARRIER-")],
    [sg.In(size=(67, 0), enable_events=True, key="-DRIVER-")],
    [sg.In(size=(67, 0), enable_events=True, key="-DVR_PHONE-")],
    [sg.In(size=(67, 0), enable_events=True, key="-RATE-")],
    [sg.In(size=(67, 0), enable_events=True, key="-NOTES-")],
    [sg.In(size=(67, 0), enable_events=True, key="-LBS-")],
    [sg.In(size=(67, 0), enable_events=True, key="-QTY-")],
    [sg.In(size=(67, 0), enable_events=True, key="-TEMP-")],
    [sg.In(size=(67, 0), enable_events=True, key="-PAL-")],
    [sg.Text("")],
    [sg.Text("")],
    [sg.In(size=(67, 0), enable_events=True, key="-APP_NUM-")],
    [sg.In(size=(67, 0), enable_events=True, key="-DEL_ADD-")],
    [sg.In(size=(67, 0), enable_events=True, key="-SO-")],
    [sg.In(size=(67, 0), enable_events=True, key="-PO-")],
    [sg.In(size=(67, 1), enable_events=True, key="-DEST_NAME-")],
    [sg.Multiline(size=(65, 3), enable_events=True, key="-DEST_ADD-")],
    # [sg.Text("")],
    [sg.Text("")],
]

saving_col = [
    [sg.Text("")],
    [sg.Text("Enter destination ADDRESS to be saved in csv file (appAdd.csv)")],
    [sg.In(size=(52, 0), enable_events=True, key="-NEW_ADD-")],
    [sg.Text("Enter dest. add. NAME to be saved in csv file (appAdd.csv)")],
    [sg.In(size=(52, 0), enable_events=True, key="-NEW_NAME-")],
    [sg.Button("Add address", enable_events=True, key="-ADD_BTN-")],
    # [sg.Text("Saved destination names")],
    # [sg.Multiline(size=(50, 8), enable_events=True, key="-SAVED_NAMES-")],
    [sg.Text("Saved destinations")],
    [sg.Multiline(size=(50, 18), enable_events=True, key="-SAVED_ADD-")]
]

layout = [
    [
        sg.Column(left_col),
        # sg.VSeperator(),
        sg.Column(right_col),
        sg.VSeperator(),
        sg.Column(saving_col)
    ]
]

message = """
<html>
    <head>
    <style>
        table {{
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        }}

        td, th {{
        border: 1px solid #000000;
        text-align: left;
        padding: 8px;
        }}

    </style>
    </head>
    <body>

        <b>Delivery Order:</b> <span style="color: red;">{ORDER}</span>
        <br><br>
        <b>Pickup Address:</b> <span>{puADD}</span>
        <br><br>
        <table>
        <tr>
            <td>Pickup Appointment</td>
            <td style="color:red">{puAPP}</td>
        </tr>
        <tr>
            <td>Carrier</td>
            <td>{CARRIER}</td>
        </tr>
        <tr>
            <td>Driver</td>
            <td>{DRIVER}</td>
        </tr>
        <tr>
            <td>Rate</td>
            <td>{RATE}</td>
        </tr>
        <tr>
            <td>Notes</td>
            <td>{NOTES}</td>
        </tr>
        </table>

        <br><br>

        <table>
            <!-- NEXT -->
        </table>
        <br>

        <p>Lbs: {LBS}</p>
        <br>

        <p>Qty: {QTY}</p>
        <br>

        <p>Temp: {TEMP} °F</p>
        <br>

        <p>Palets: {PAL}</p>

    </body>
</html>
"""

plain_msg = """
Delivery Order: {ORDER}\n
Pickup address: {puADD}\n

-------------------------------------------------------
Pickup Appointment: {puAPP}
Carrier: {CARRIER}
Driver: {DRIVER}
Rate: {RATE}
Notes: {NOTES}
-------------------------------------------------------

<>

Lbs: {LBS}
Qty: {QTY}
Temp: {TEMP} °F
Palets: {PAL}
"""

# Create the window
main = sg.Window("e-Mail generator", layout, finalize=True)
for tb in text_box:
    main['-SAVED_ADD-'].print("* " + tb)

# Create an event loop
while True:
    event, values = main.read()
    if event == "-SEND-":
        appNum = values['-APP_NUM-'].split(',')
        appDate = values['-DEL_ADD-'].split(',')
        appSO = values['-SO-'].split(',')
        appPO = values['-PO-'].split(',')
        appNames = values['-DEST_NAME-'].split(',')
        appAdds = values['-DEST_ADD-'].split(',')

        cond1 = len(appNum) == len(appDate) and len(appNum) == len(appSO) and len(appNum) == len(appPO) and len(appNum) == len(appNames) and len(appNum) == len(appAdds)
        cond2 = len(appDate) == len(appSO) and len(appNum) == len(appPO) and len(appNum) == len(appNames) and len(appNum) == len(appAdds)
        cond3 = len(appSO) == len(appPO) and len(appSO) == len(appNames) and len(appSO) == len(appAdds)
        cond4 = len(appPO) == len(appNames) and len(appPO) == len(appAdds)
        cond5 = len(appNames) == len(appAdds)

        if cond1 and cond2 and cond3 and cond4 and cond5:
            puAdd = values["-PU_ADD-"] + '<br>\n' + 'Details: ' + values['-ADD_DET-']
            puAdd_pl = values["-PU_ADD-"] + '\n' + 'Details: ' + values['-ADD_DET-']
            driver = values["-DRIVER-"] + ', Phone: ' + values['-DVR_PHONE-']
            form_msg = message.format(
                        ORDER=values["-DEL_NUM-"], puADD=puAdd, puAPP=values["-PU_DATE-"], CARRIER=values["-CARRIER-"],
                        DRIVER=driver, RATE=values["-RATE-"], NOTES=values["-NOTES-"], LBS=values['-LBS-'],
                        QTY=values['-QTY-'], TEMP=values['-TEMP-'], PAL=values['-PAL-'])
            form_plain = plain_msg.format(
                        ORDER=values["-DEL_NUM-"], puADD=puAdd_pl, puAPP=values["-PU_DATE-"], CARRIER=values["-CARRIER-"],
                        DRIVER=driver, RATE=values["-RATE-"], NOTES=values["-NOTES-"], LBS=values['-LBS-'],
                        QTY=values['-QTY-'], TEMP=values['-TEMP-'], PAL=values['-PAL-'])
            appText  = ''
            for i in range(0, len(appSO)):
                table_line = """
                            <tr>
                                <td>{APP}</td>
                                <td>{ADD}</td>
                            </tr>
                            <!-- NEXT -->
                            """
                plain_line = """=======================================================
{APP}
-------------------------------------------------------
{ADD}
=======================================================
<>"""
                appCell = '<p><span style="color:red;">Appointment: ' + appDate[i] + '</span></p><br>' + '<p>Number:' + appNum[i] + '</p><br>' + \
                            '<p>SO:' + appSO[i] + ', PO:' + appPO[i] + '</p>'
                appCell_pl = 'Appointment: ' + appDate[i] + '\n' + 'Number:' + appNum[i] + '\n' + \
                            'SO:' + appSO[i] + ', PO:' + appPO[i] + '\n'
                appText = table_line.format(APP=appCell, ADD=appNames[i] + '<br><br>' + appAdds[i])
                appText_pl = plain_line.format(APP=appCell_pl, ADD=appNames[i] + '\n\n' + appAdds[i])
                form_msg = form_msg.replace('<!-- NEXT -->', appText)
                form_plain = form_plain.replace('<>', appText_pl)
            f = open('msg.html', 'w')
            f.write(form_msg)
            f.close()
            pc.copy(form_plain)
            wb.open('msg.html')
            sg.Popup("Generated email text opened in web browser window.", keep_on_top=True)
        else:
            sg.Popup("Please, fill all the appointment entries correctly")
    elif event == "-ADD_BTN-":
        if values['-NEW_ADD-'] != '' and values['-NEW_NAME-'] != '':
            new_add =  values['-NEW_NAME-'] + ', ' + values['-NEW_ADD-']
            main['-SAVED_ADD-'].print('* ' + new_add)
            myfile = Path("appAdd.csv")
            myfile.touch(exist_ok=True)
            f = open(myfile, 'a+')
            f.write('\n' + new_add)
            f.close()
        else:
            sg.Popup("Please, input the name and the address you want to save", keep_on_top=True)
    elif event == sg.WIN_CLOSED:
        break

main.close()

