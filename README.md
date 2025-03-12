[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rMafNWiN)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18648387)
# Práctica 1. Estructura de control selectiva

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
