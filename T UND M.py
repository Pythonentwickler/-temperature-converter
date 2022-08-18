'''
celsius = 37.5
fahrenheit = (celsius * 1.8) + 32
celsius = (fahrenheit - 32) / 1.8
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
'''
'''
def convert_SI(val, unit_in, unit_out):
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
    return val*SI[unit_in]/SI[unit_out]
convert_SI(1, 'm', 'km')
0.001
convert_SI(1, 'km', 'm')
1000.0
convert_SI(1, 'cm', 'm')
0.01
'''

#temperature/measurement converter Program
###################################



while True :    
    def print_menu():
        print('1. Inches to Centimeters')
        print('2. Inches to Meters')
        print('3. Inches to Kilometers')

    def inch_cm():
        inch = float (input('Enter a Number in inch : '))
        cm = inch / 2.54
        print(cm)
        print('-----------------------------')

    def inch_m():
        inch = float (input('Enter a Number in inch : '))
        m = inch /0.0254 
        print(m)
        print('-----------------------------')
        
    def inch_km():
        inch = float (input('Enter a Number in inch : '))
        km = inch /0.00003
        print(km)
        print('-----------------------------')

    print_menu()


    choice = input('which conversion would you like to do?')
    if choice == '1' :
        inch_cm()
    if choice == '2' :
        inch_m()
    if choice == '3':
        inch_km()
