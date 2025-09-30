# Programa de Conversion de soles a dolares
def conversion_soles_dolares():
# Solicitar al usuario el monto en soles 
monto_soles = float(input ("S/1000.00 (PEN):"))
# preguntar la casa de cambio actual
casa_cambio = float(input("$ 3.85 ( 1 USD =? PEN):"))
# calcular el equivalente en dolares
monto_dolares = monto_soles/casa_cambio
# mostrar el resultado con dos decimales
print("/nconversion en global change")
print(f"monto en soles:s/{monto_soles:.2f}")
print(f"casa de cambio:1USD= S/{casa_cambio:.2f}")
print(f"equivalenete en dolares:$ {monto_dolares:.2f}")
# ejecutar el programa
conversion_soles_dolares()