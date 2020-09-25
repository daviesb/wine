#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:40:51 2020

@author: daviesb
"""

#%% import modules
import wine
import pandas as pd
import PySimpleGUI as sg

#%% import excel file and manipulate
df_raw = pd.read_excel('Wine2.xlsx')

### retain only necessary columns
df_wine = df_raw[['Vintage', 'Producer', 'Name', 'Identifier', 'Country', 'Region', 'Sub Region', 'Size (ml)', 'Cellar Location',
                  'Color', 'Sweetness', 'WA Rating Clean', 'My Rating', 'Price', 'Class', 'Tier', 'Store', 'Purchased']]

### remove any rows that have N/A for Producer column
df_wine = df_wine.dropna(subset=['Producer'])

### convert numeric columns
numeric_cols = ['Vintage', 'Size (ml)', 'WA Rating Clean', 'My Rating', 'Price', 'Class', 'Tier']
df_wine[numeric_cols] = df_wine[numeric_cols].apply(pd.to_numeric, errors='coerce')


#%% create list of WineBottle objects from Excel file

### return all attributes of WineBottle class
att_list = []
for att in vars(wine.WineBottle()):
    att_list.append(att)

### generate WineBottle objects and place into list
bottle_list = []
for bottle in range(0, len(df_wine)):
    value_list = df_wine.loc[bottle].values.tolist()
    bottle_args = dict(zip(att_list, value_list))
    bottle_list.append(wine.WineBottle(**bottle_args))
    
#%% create list of WineCase objects
### get list of all Cellar Locations
cellar_list = sorted(df_wine['Cellar Location'].unique().tolist())

wine_case_list = []
### generate WineCase objects based on cellar_list
for cellar in cellar_list:
    _temp_bottle_list = []
    for bottle in bottle_list:
        if bottle.cellar == cellar:
            _temp_bottle_list.append(bottle)
    wine_case_list.append(wine.WineCase(*_temp_bottle_list, name=_temp_bottle_list[0].cellar))
    

#%% print and play
for case in wine_case_list:
    case.show_bottles()

for case in wine_case_list:
    print('-------------------')
    print(case.name)
    print('Avg price: $' + str(round(case.get_average_metric('price'))))
    print('Avg vintage: ' + str(round(case.get_average_metric('vintage'))))
    print('Avg Wine Advocate rating: ' + str(round(case.get_average_metric('wa_rating'))))
    print('Avg My Rating: ' + str(round(case.get_average_metric('my_rating'))))



#%% GUI

sg.theme('SandyBeach')

column1 = [[sg.Text('Column 1', background_color='#d3dfda', justification='center', size=(10,1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]
layout = [
            [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
            [sg.Text('Here is some text.... and a place to enter text')],
            [sg.InputText('This is my text')],
            [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],
            [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
            [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
             sg.Multiline(default_text='A second multi-line', size=(35, 3))],
            [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 3)),
             sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
            [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
             sg.Column(column1, background_color='#d3dfda')],
            [sg.Text('_'  * 80)],
            [sg.Text('Choose A Folder', size=(35, 1))],
            [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
             sg.InputText('Default Folder'), sg.FolderBrowse()],
            [sg.Submit(), sg.Cancel()]
        ]


window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()





# sg.theme('Dark Brown')


# layout = [[sg.Text('Theme Browser')],
#           [sg.Text('Click a Theme color to see demo window')],
#           [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
#           [sg.Button('Exit')]]

# window = sg.Window('Theme Browser', layout)

# while True:  # Event Loop
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, 'Exit'):
#         break
#     sg.theme(values['-LIST-'][0])
#     sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

# window.close()

