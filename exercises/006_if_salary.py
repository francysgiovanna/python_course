#calcular prima de antiguedad 
#si tiene menos de 5 años es 0
#si esta entre 6 y 10 años es 100
#entre 10 y 15 años 200
#entre 15 y 20 años 300
#mayor de 20 años 500
print('calculo de salario')
print('ingrese sueldo')
salary = float (input())
print('ingrese año de servicio')
years = float (input())
if (years >= 6 and years <= 10):
    prima = 100
elif (years >= 11 and years <= 15):
    prima = 200
elif (years >= 16 and years <= 20):
    prima = 300
elif (years >= 21):    
    prima = 500
else:
    prima = 0
total = salary + prima 
print('total salario =', total)