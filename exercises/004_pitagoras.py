import math
# calculo de pitagora
print('calculo de hipotenusa')
print('ingrese cateto opuesto')
cateto_opuesto = float (input())
print('ingrese cateto adyacente')
cateto_adyacente = float (input())
result = math.sqrt((cateto_opuesto**2)+(cateto_adyacente**2))
print('el valor de la hipotenusa es:  ', result)
print('calculo de cateto opuesto')
print('ingrese hipotenusa')
hipotenusa = float (input())
print('ingrese cateto adyacente')
cateto_adyacente = float (input())
result = math.sqrt((hipotenusa**2)-(cateto_adyacente**2))
print('el valor del cateto opuesto es:  ', result)
print('calculo cateto adyacente')
print('ingrese hipotenusa')
hipotenusa = float (input())
print('ingrese cateto opuesto')
cateto_opuesto = float (input())
result = math.sqrt((hipotenusa**2)-(cateto_opuesto**2))
print('el valor del cateto adyacente es:  ', result)