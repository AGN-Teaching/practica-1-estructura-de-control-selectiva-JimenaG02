"""
Programa practica1.py

Este programa calcula el salario de trabajadores, se calcula segun las horas de trabajo si estan dentro de ciertos rangos
horas <= 160 ---Salario por hora
horas >160 && horas<200 --- Salario por hora y hrs > se pagan a 1.5
horas >200 --- Anterior y hrs > a 200 se pagan al doble

También calcula el ISR usando la tabla de tarifas progresivas del SAT:
1. Se identifica el rango del ingreso bruto
2. Se aplica el porcentaje correspondiente al nivel salarial.
3. Se resta el límite inferior del rango
4.Se suma la cuota fija del SAT

Para la seguridad social, se descuenta el 2.5% del sueldo bruto.

Si el empleado es parte de la caja de ahorros, se aplica:
1. Cuota fija: $1,000.00 mensuales.
2. Cuota porcentual: 3% o 5% del sueldo bruto.

Para el fondo de ahorro para el retiro, el empleado puede:
1. No participar.
2. Aportar el 1% del sueldo bruto.
3. Aportar el 2% del sueldo bruto.
"""



# Sueldo Bruto
horas = int(input("Ingresa las horas trabajadas: "))
salarioxhr = float(input("Ingresa tu salario por hora: "))
sueldo_bruto = 0.0

if horas <= 160:
    sueldo_bruto = salarioxhr * horas

elif 160 < horas <= 200:
    # Calcula las horas excedentes a 160
    horas_excedente = horas - 160
    sueldo_bruto = (160 * salarioxhr) + (horas_excedente * salarioxhr * 1.5)
    # Sueldo bruto: Las primeras 160 horas se pagan al salario normal y las horas excedentes se pagan

else:
    # Primera parte: 160 horas al salario normal
    sueldo_normal = 160 * salarioxhr

    # Segunda parte: 40 horas (de 161 a 200) a 1.5 veces el salario
    sueldo_excedente161 = 40 * (salarioxhr * 1.5)

    # Tercera parte: horas excedentes a 200 al doble del salario
    horas_excedentes200 = horas - 200
    sueldo_extra_200 = horas_excedentes200 * (salarioxhr * 2)

    # Sueldo bruto total
    sueldo_bruto = sueldo_normal + sueldo_excedente161 + sueldo_extra_200

print("\nSueldo bruto:", sueldo_bruto)

# ISR
#Asignamos valores a la cuota, limite inferior y porcentaje excedente para poder calcular el ISR dependiendo de su rango
if 0.01 <= sueldo_bruto <= 746.04:
    limite_inferior = 0.01
    cuota = 0
    porcentaje_excedente = 1.92
elif 746.05 <= sueldo_bruto <= 6332.05:
    limite_inferior = 746.05
    cuota = 14.32
    porcentaje_excedente = 6.40
elif 6332.06 <= sueldo_bruto <= 11128.01:
    limite_inferior = 6332.06
    cuota = 371.83
    porcentaje_excedente = 10.88
elif 11128.02 <= sueldo_bruto <= 12935.82:
    limite_inferior = 11128.02
    cuota = 893.63
    porcentaje_excedente = 16
elif 12935.83 <= sueldo_bruto <= 15487.71:
    limite_inferior = 12935.83
    cuota = 1182.88
    porcentaje_excedente = 17.92
elif 15487.72 <= sueldo_bruto <= 31236.49:
    limite_inferior = 15487.72
    cuota = 1640.18
    porcentaje_excedente = 21.36
elif 31236.50 <= sueldo_bruto <= 49233.00:
    limite_inferior = 31236.50
    cuota = 5004.12
    porcentaje_excedente = 23.52
elif 49233.01 <= sueldo_bruto <= 93993.90:
    limite_inferior = 49233.01
    cuota = 9236.89
    porcentaje_excedente = 30
elif 93993.91 <= sueldo_bruto <= 125325.20:
    limite_inferior = 93993.91
    cuota = 22665.17
    porcentaje_excedente = 32
elif 125325.21 <= sueldo_bruto <= 375975.61:
    limite_inferior = 125325.21
    cuota = 32691.18
    porcentaje_excedente = 34
else:
    limite_inferior = 375975.62
    cuota = 117912.32
    porcentaje_excedente = 35
#formula ISR y se lo restamos al sueldo neto
isr = cuota + (sueldo_bruto - limite_inferior) * (porcentaje_excedente / 100)
sueldo_neto = sueldo_bruto - isr

print("ISR:", isr)

# Seguro Social
aportacion_ss = sueldo_bruto * 0.025 #2.5% = 0.025
sueldo_neto -= aportacion_ss
print("Aportación Seguro Social:", aportacion_ss,"\n")

# Caja de Ahorro
print("<| Caja de ahorro |>")
op = int(input("¿Qué tipo de cuota tienes?\n1. Cuota fija\n2. Cuota porcentual del 3%\n3. Cuota del 5%\n"))
if op == 1: #cuota fija
    sueldo_neto -= 1000
elif op == 2: #Cuota porcentual 3%
    sueldo_neto -= sueldo_bruto * 0.03 #3% = 0.03
elif op == 3: # Cuota del 5%
    sueldo_neto -= sueldo_bruto * 0.05 #5% = 0.05

# Ahorro para el retiro
print("<| Ahorro para el retiro |>")
op2 = int(input("Elige alguna de las siguientes opciones:\n1. No participar\n2. Aportar 1%\n3. Aportar 2%\n"))
#No hay op2==1 debido a que los valores del sueldo neto no se modifican
if op2 == 2: #Aportar 1%
    sueldo_neto -= sueldo_neto * 0.01
elif op2 == 3: #Aportar 2%
    sueldo_neto -= sueldo_neto * 0.02

print("\nSueldo neto final: $",sueldo_neto)
