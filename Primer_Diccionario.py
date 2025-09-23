edades = {
    "Brayan": 25,
    "Luis": 30,
    "José": 22
}
print("Edad de Luis:", edades["Luis"])    
edades["Brayan"] = 28
print("\nDespués de añadir a Brayan:")
print(edades)                               

edades["Luis"] = 26
print("\nDespués de actualizar la edad de Luis:")
print(edades)                              

del edades["José"]
print("\nDespués de eliminar a José:")
print(edades)                               

print("\nRecorriendo el diccionario:")
for Nombre, Edad in edades.items():         
     print(f"{Nombre} tiene {Edad} años")