print("bienvenido a la calculadora de promedios de notas")
suma_notas = 0 

n_notas =  int(input("Ingrese la cantidad de notas que desea ingresar : "))

for i in range (1,n_notas+1) : 
    nota = int(input(f"Ingrese una su nota numero {i} : " ))
    suma_notas =+ nota

print(suma_notas)
    
