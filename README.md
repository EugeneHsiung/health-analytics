# health-analytics
this assignment is a primer for 504/507

# Summary
```
oxygen_saturation = int(input('put in your current oxygen_saturation: '))
```
This is a number variable. The user is asked to put in their O2 Sat. 

```
heart_rate= int(input('put in your heart rate: '))
```
This is a 2nd number variable for the user to input their heart rate

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
heart_rate_levels = {
    'tachycardia': (100, 140),
    'bradycardia': (1,60),
    'normal': (60, 100)
```
This is a dictionary. These show what levels of heart rate indicate


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
def oxygensaturationchecker(oxygen_saturation, heart_rate): 
    if (oxygen_saturation >= 95 and oxygen_saturation <=100) and (heart_rate >=60 and heart_rate <100):
        result = 'normal'
    if oxygen_saturation < 95 and heart_rate <60: 
        result = 'below normal'
    else:
        result = 'above normal'
    return result
```
This is the function to check if you are normal, below normal, or above normal based on the O2 sat level and heart rate

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
def heart_rate_status(heart_rate_levels):
    if heart_rate_levels > 100: 
        you_are = 'tachycardia' 
    if heart_rate_levels <60:
        you_are= 'bradycardia'
    if heart_rate_levels >=60 and heart_rate_levels <=100: 
        you_are= 'normal heart rate'    
    return you_are
```
This is the function to categorize based on the level of heart rate.  


```
print('hello,', name,'.' , 'Your result is', oxygensaturationchecker(oxygen_saturation, heart_rate), 'with a SPO2 of', oxygen_saturation, '%.', 'you have', oxygenationstatus (oxygen_saturation) )
print('your heart rate is', heart_rate, 'indicating', heart_rate_status (heart_rate))
```
This is the print statement for both the o2 saturation checker, oxygenation status, and heart rate status.  

#Example

```
put in your current oxygen_saturation: 98
put in your heart rate: 90
enter Your Name: John
hello, John . Your result is above normal with a SPO2 of 98 %. you have normal oxygenation
your heart rate is 90 indicating normal heart rate
```


