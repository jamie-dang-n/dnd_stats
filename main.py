import PySimpleGUI as sg      
import random

def roll_stat():
  #rolling the dice
  min = 1
  max = 6
  stat_rolls = []
  for i in range(4):
    new_roll = random.randint(min,max)
    stat_rolls.append(new_roll)

  #removing lowest value
  stat_rolls.sort()
  stat = stat_rolls[1:]

  #receiving total
  total = 0
  for ele in range(0, len(stat)):
    total = total + stat_rolls[ele]

  return total

def total_stats():
  total_stats = []
  for i in range(6):
    total_stats.append(roll_stat())
    total_stats.sort(reverse=True)
  return total_stats

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text('Enter your class', key='-CHARCLASS-')],      
          [sg.Input(key='-IN-')],    
          [sg.Text(key='-OUTPUT-')],
          [sg.Text(key='-CLASSOUT-')],  
          [sg.Button('Roll'), sg.Exit()]]      

window = sg.Window('DND Stat Roller', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    if event == 'Roll':
      final_stats = total_stats()
      window['-OUTPUT-'].update(final_stats)
      # if values['-CHARCLASS-'] == "bard":
      #   window['-CLASSOUT-'].update()

window.close()