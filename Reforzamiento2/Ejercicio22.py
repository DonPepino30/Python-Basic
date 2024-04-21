"""Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar el valor
de salario en consola."""
empleado = {
    "nombre": "Juan",
    "edad": 19,
    "salario": 2234.50,
    "posicion": "Tester"
}
empleado["dni"] = "70844887"
print("Salario:", empleado["salario"])