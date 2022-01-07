import PySimpleGUI as sg      
import stat_roller as sr

#GUI Layout
sg.theme('DarkAmber')    

layout = [[sg.Text('Select your class', size=(60, 1))],      
          [sg.Combo(['Bard','Cleric','Barbarian', 'Druid','Fighter','Monk','Paladin','Ranger', 'Rogue'],default_value='Bard',key='-IN-')],    
          [sg.Text('Your Stat Scores:'),sg.Text(key='-OUTPUT-')],
          [sg.Text( key='-CLASSOUTFIRST-')],
          [sg.Text(key='-CLASSOUTSEC-')],
          [sg.Text(key='-CLASSOUTTHIRD-')], 
          [sg.Text(key='-CLASSOUTFOUR-')],
          [sg.Text(key='-CLASSOUTFIVE-')], 
          [sg.Button('Roll'), sg.Exit()]]      

window = sg.Window('DND Stat Roller', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    if event == 'Roll':
      final_stats = sr.total_stats()
      window['-OUTPUT-'].update(final_stats)
      character_class = values['-IN-']
      suggest = sr.suggestion(character_class, final_stats)
      window['-CLASSOUTFIRST-'].update(suggest[0])
      window['-CLASSOUTSEC-'].update(suggest[1])
      window['-CLASSOUTTHIRD-'].update(suggest[2])
      window['-CLASSOUTFOUR-'].update(suggest[3])
      window['-CLASSOUTFIVE-'].update(suggest[4])

window.close()