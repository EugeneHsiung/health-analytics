# health-analytics
this assignment is a primer for 504/507

# Summary
```
oxygen_saturation = int(input('put in your current oxygen_saturation: '))
```
This is a number variable. The user is asked to put in their O2 Sat. 

```
name = input('enter Your Name: ')
```
This is a string variable. The user is asked to put in their name

```
symptoms_presented = ['headache', 'rapid heart rate', 'coughing', 
'cyanosis', 'vision disturbance', 'disorientation', 'dizziness']
```
This is a List. The is a list of symptoms presented

```
measurement_of_symptoms = {'headache' :'hypoxemia' , 'rapid heart rate': 'hypoxemia', 'coughing': 'hypoxemia', 'cyanosis': 'hypoxemia',
'vision disturbance': 'hyperoxia', 'disorientation': 'hyperoxia', 'dizziness': 'hyperoxia'}
```
This is a dictionary. This is what each of the symptoms means

```
oxygen_saturation_levels = {
    'hyperxia': (100, 120),
    'normal': (95, 100),
    'hypoxia': (60, 94)}
```
This is a dictionary. These show what each level of O2 saturation indicates. 

```
patient_data = {
'patient_1' : {'firstname, lastname': 'John Smith', 
            'symptoms':['dizziness', 'disorientation', 'visual disturbance']},

'patient_2' : {'firstname, lastname': 'Jason Smith', 
            'symptoms':['headache', 'rapid heart rate', 'coughing']},

'patient_3' : {'firstname, lastname': 'Kib Smith', 
            'symptoms':'none'}
}
```
This is a nested dictionary. It presented what the patient name is and what their symotoms are

```
def oxygensaturationchecker(oxygen_saturation): 
    if oxygen_saturation >= 95 and oxygen_saturation <=100:
        result = 'normal'
    if oxygen_saturation < 95:
        result = 'below normal'
    if oxygen_saturation > 100:
        result = 'above normal'
    return result
```
This is the function to check if you are normal, below normal, or above normal based on the O2 sat level

```
def oxygenationstatus(oxygen_saturation):
    if oxygen_saturation > 100 and oxygen_saturation <120:
        show = 'hyperxia'
    if oxygen_saturation >=60 and oxygen_saturation <94:
        show= 'hypoxia'
    if oxygen_saturation >94 and oxygen_saturation <=100:    
        show= 'normal oxygenation'    
    return show
```
This is the function to categorize based on the level of O2 saturation. 

```
print('hello,', name,'.' , 'Your result is', oxygensaturationchecker(oxygen_saturation), 'with a SPO2 of', oxygen_saturation, '%.', 'you have', oxygenationstatus (oxygen_saturation) )
```
This is the print statement for both the o2 saturation checker and oxygenation status (both functions). 

For example: if you put in an O2 saturation of 80 and the name of John, it will print: hello, John . Your result is below normal with a SPO2 of 80 %. you have hypoxia

