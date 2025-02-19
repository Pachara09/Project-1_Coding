Mass = float(input("Mass (kg)"))
Volume = float(input("Volume (m³)"))

Density = Mass / Volume

def classify_density(density):
  if density < 1000:
    return "Low Density"
  elif density < 5000:
    return "Mid Density"
  else:
    return "High Density"

print("Density is ", '%.2f' %Density, "kg/m³")
print("This material is", classify_density(Density))