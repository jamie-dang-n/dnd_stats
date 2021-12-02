import PySimpleGUI as sg      

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text('Enter your class')],      
          [sg.Input(key='-IN-')],      
          [sg.Button('Roll'), sg.Exit()]]      

window = sg.Window('DND Stat Roller', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

window.close()