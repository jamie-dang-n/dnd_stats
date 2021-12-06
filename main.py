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

def suggestion(character_class, total_stats):
  if character_class == "Barbarian":
    strength = "Strength: " + str(total_stats[1])
    constitution = "Constitution: " + str(total_stats[0])
    barbarian_string = ['The barbarian benefits aplenty from high constitution, and good strength.', constitution, strength, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return barbarian_string
  elif character_class == "Bard":
    charisma = "Charisma: " + str(total_stats[0])
    intelligence = "Intelligence: " + str(total_stats[1])
    bard_string = ['The bard benefits aplenty from high charisma, and good intelligence.', charisma, intelligence, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return bard_string
  elif character_class == "Cleric":
    wisdom = "Wisdom: " + str(total_stats[0])
    charisma = "Charisma: " + str(total_stats[1])
    cleric_string = ['The cleric benefits aplenty from high wisdom, and good charisma.', wisdom, charisma, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return cleric_string

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text('Select your class', size=(60, 1))],      
          [sg.Combo(['Bard','Cleric','Barbarian', 'Druid','Fighter','Monk','Paladin','Ranger', 'Rogue'],default_value='Bard',key='-IN-')],    
          [sg.Text(key='-OUTPUT-')],
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
      final_stats = total_stats()
      window['-OUTPUT-'].update(final_stats)
      character_class = values['-IN-']
      suggest = suggestion(character_class, final_stats)
      window['-CLASSOUTFIRST-'].update(suggest[0])
      window['-CLASSOUTSEC-'].update(suggest[1])
      window['-CLASSOUTTHIRD-'].update(suggest[2])
      window['-CLASSOUTFOUR-'].update(suggest[3])
      window['-CLASSOUTFIVE-'].update(suggest[4])

window.close()