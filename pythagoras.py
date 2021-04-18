#ask_pythagoras v2.py

import PySimpleGUI as sg
import math

form = sg.FlexForm('ASK PYTHAGORAS', size = (260, 240))

# set up layout with initial values in text and combo fields

layout = [ [sg.Txt('How'),
            sg.Combo(values = ('far did', 'high can', 'far can'), size = (8, 3), readonly = True, default_value = 'far did', enable_events = True, key = 'question'),
            sg.Txt('I fly?')],
           [sg.Txt('Change in ground position', size=(40,1), key='describeA')],
           [sg.In(size=(4,1), key='inA'),
            sg.Txt('ft.')],
           [sg.Txt('_'  * 10)],
           [sg.Txt('Change in height', size=(40,1), key='describeB')],
           [sg.In(size=(4,1), key='inB'),
            sg.Txt('ft.')],
           [sg.Txt('Enter values in ft.', size=(15,1), key='output')  ],
           [sg.ReadFormButton('Calculate', bind_return_key=True)]]

form.Layout(layout)

while True:
    button, values = form.Read()
    combo = values['question']

    # changing text fields to match current drop down
    
    if combo == 'high can':
        form.FindElement('describeA').Update('Change in ground position')
        form.FindElement('describeB').Update('Total movement available')
    elif combo == 'far did':
        form.FindElement('describeA').Update('Change in ground position')
        form.FindElement('describeB').Update('Change in height')
    elif combo == 'far can':
        form.FindElement('describeA').Update('Change in height')
        form.FindElement('describeB').Update('Total movement available')

    if button is not None:
        try:
            inA = int(values['inA'])
            inB = int(values['inB'])
            if combo == 'high can':
                calc = math.sqrt((inB ** 2) - (inA ** 2))
                calc = calc - (calc % 5)        # rounding down to nearest 5
            elif combo == 'far did':
                calc = math.sqrt((inA ** 2) + (inB ** 2))
                if (calc % 5) > 0:
                    calc = calc + (5 - calc % 5)    # this one rounds up becuase
            elif combo == 'far can':                # no partial mvmt in D&D
                calc = math.sqrt((inB ** 2) - (inA ** 2))
                calc = calc - (calc % 5)        # rounds down
            calc = int(calc)
            calc = str(calc) + ' ft.'
            
            form.FindElement('output').Update(calc)
        except:
            calc = 'Enter values in'            # presumably breaks friendly
    else:
        break
