import PySimpleGUI as sg      
import random

#Functions
#defining the stat rolling function; individual scores
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

#compiling scores into sets of 6
def total_stats():
  total_stats = []
  for i in range(6):
    total_stats.append(roll_stat())
    total_stats.sort(reverse=True)
  return total_stats

#output; gives suggestions on where to put scores and updates text
def suggestion(character_class, total_stats):
  if character_class == "Barbarian":
    first = "Strength: " + str(total_stats[0])
    second = "Constitution: " + str(total_stats[1])
    class_string = ['The barbarian benefits aplenty from high constitution, and good strength.', first, second, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return class_string
  elif character_class == "Bard":
    first = "Charisma: " + str(total_stats[0])
    second = "Intelligence: " + str(total_stats[1])
    class_string = ['The bard benefits aplenty from high charisma, and good intelligence.', first, second, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return class_string
  elif character_class == "Cleric":
    first = "Wisdom: " + str(total_stats[0])
    second = "Charisma: " + str(total_stats[1])
    class_string = ['The cleric benefits aplenty from high wisdom, and good charisma.', first, second, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return class_string
  elif character_class == "Druid":
    first = "Wisdom: " + str(total_stats[0])
    second = "Dexterity: " + str(total_stats[1])
    class_string = ['The druid benefits aplenty from high wisdom, and good dexterity.', first, second, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return class_string
  elif character_class == "Fighter":
    first = "Strength: " + str(total_stats[0])
    second = "Constitution: " + str(total_stats[1])
    class_string = ['The fighter benefits aplenty from high strength, and good constitution.', first, second, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return class_string
  elif character_class == "Monk":
    first = "Dexterity: " + str(total_stats[0])
    second = "Wisdom: " + str(total_stats[1])
    class_string = ['The monk benefits aplenty from high dexterity, and good wisdom.', first, second, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return class_string
  elif character_class == "Paladin":
    first = "Charisma: " + str(total_stats[0])
    second = "Strength: " + str(total_stats[1])
    class_string = ['The paladin benefits aplenty from high charisma, and good strength.', first, second, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return class_string
  elif character_class == "Ranger":
    first = "Charisma: " + str(total_stats[0])
    second = "Strength: " + str(total_stats[1])
    class_string = ['The ranger benefits aplenty from high strength, and good dexterity.', first, second, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return class_string
  elif character_class == "Rogue":
    first = "Dexterity: " + str(total_stats[0])
    second = "Charisma: " + str(total_stats[1])
    class_string = ['The rogue benefits aplenty from high dexterity, and good charisma.', first, second, 'The rest of the scores may go wherever you please.', str(total_stats[2:])]
    return class_string

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