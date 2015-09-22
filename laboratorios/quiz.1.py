base = 5
height = 7

area = base + height
perimeter = area * 2

__to_meters = 100
__to_inches = 2.54

print("Area: %dcm" % area)
print("Perimetro: %dcm\n" % perimeter)

# @note Redondeado a 2 decimales
print("Area en Metros: %.2fm" % (area / __to_meters))
print("Perimetro en Metros: %.2fm\n" % (perimeter / __to_meters))

print("Area en Pulgadas: %.2finch" % (area / __to_inches))
print("Perimetro en Pulgadas: %.2finch\n" % (perimeter / __to_inches))
