import pandas as pd 
import numpy as np 


oxygen_saturation = int(input('put in your current oxygen_saturation: '))
heart_rate= int(input('put in your heart rate: '))

name = input('enter Your Name: ')

symptoms_presented = ['headache', 'rapid heart rate', 'coughing', 
'cyanosis', 'vision disturbance', 'disorientation', 'dizziness']

measurement_of_symptoms = {'headache' :'hypoxemia' , 'rapid heart rate': 'hypoxemia', 'coughing': 'hypoxemia', 'cyanosis': 'hypoxemia',
'vision disturbance': 'hyperoxia', 'disorientation': 'hyperoxia', 'dizziness': 'hyperoxia'}

oxygen_saturation_levels = {
    'hyperxia': (100, 120),
    'normal': (95, 100),
    'hypoxia': (60, 94)}

heart_rate_levels = {
    'tachycardia': (100, 140),
    'bradycardia': (1,60),
    'normal': (60, 100)
}

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


def oxygensaturationchecker(oxygen_saturation, heart_rate): 
    if oxygen_saturation > 100 and heart_rate >100:
        result = 'above normal'
    if oxygen_saturation < 95 and heart_rate <60: 
        result = 'below normal'
    else:
        result = 'normal'
    return result

def oxygenationstatus(oxygen_saturation):
    if oxygen_saturation > 100 and oxygen_saturation <120:
        show = 'hyperxia' 
    if oxygen_saturation >0 and oxygen_saturation <94:
        show= 'hypoxia'
    else:     
        show= 'normal oxygenation'    
    return show

def heart_rate_status(heart_rate_levels):
    if heart_rate_levels > 100: 
        you_are = 'tachycardia' 
    if heart_rate_levels <60:
        you_are= 'bradycardia'
    if heart_rate_levels >=60 and heart_rate_levels <=100: 
        you_are= 'normal heart rate'    
    return you_are 


#example: 
print('hello,', name,'.' , 'Your result is', oxygensaturationchecker(oxygen_saturation, heart_rate), 'with a SPO2 of', oxygen_saturation, '%.', 'you have', oxygenationstatus (oxygen_saturation) )
print('your heart rate is', heart_rate, 'indicating', heart_rate_status (heart_rate))

