import pandas as pd 
import numpy as np 


oxygen_saturation = int(input('put in your current oxygen_saturation: '))

name = input('enter Your Name: ')

symptoms_presented = ['headache', 'rapid heart rate', 'coughing', 
'cyanosis', 'vision disturbance', 'disorientation', 'dizziness']

measurement_of_symptoms = {'headache' :'hypoxemia' , 'rapid heart rate': 'hypoxemia', 'coughing': 'hypoxemia', 'cyanosis': 'hypoxemia',
'vision disturbance': 'hyperoxia', 'disorientation': 'hyperoxia', 'dizziness': 'hyperoxia'}

oxygen_saturation_levels = {
    'hyperxia': (100, 120),
    'normal': (95, 100),
    'hypoxia': (60, 94)}

#patient 1: John Smith, symptoms: dizziness, disorientation, visual disturbance
#patient 2: Jason Smith, symptoms: headache, rapid heart rate, coughing
#patient 3: Kib Smith, symptoms: none

patient_data = {
'patient_1' : {'firstname, lastname': 'John Smith', 
            'symptoms':['dizziness', 'disorientation', 'visual disturbance']},

'patient_2' : {'firstname, lastname': 'Jason Smith', 
            'symptoms':['headache', 'rapid heart rate', 'coughing']},

'patient_3' : {'firstname, lastname': 'Kib Smith', 
            'symptoms':'none'}
}


def oxygensaturationchecker(oxygen_saturation): 
    if oxygen_saturation >= 95 and oxygen_saturation <=100:
        result = 'normal'
    if oxygen_saturation < 95:
        result = 'below normal'
    if oxygen_saturation > 100:
        result = 'above normal'
    return result

def oxygenationstatus(oxygen_saturation):
    if oxygen_saturation > 100 and oxygen_saturation <120:
        show = 'hyperxia'
    if oxygen_saturation >=60 and oxygen_saturation <94:
        show= 'hypoxia'
    if oxygen_saturation >94 and oxygen_saturation <=100:    
        show= 'normal oxygenation'    
    return show

#example: 
print('hello,', name,'.' , 'Your result is', oxygensaturationchecker(oxygen_saturation), 'with a SPO2 of', oxygen_saturation, '%.', 'you have', oxygenationstatus (oxygen_saturation) )

