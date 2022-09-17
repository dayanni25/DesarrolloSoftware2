a=float(input("Digite el valor de a: "))
b=float(input("Digite el valor de b: "))
c=float(input("Digite el valor de c: "))
delta=b**2-4*a*c
if delta==0:
  print(-b/(2*a))
elif delta<0:
  print("La ecuacion no tiene soluciones reales")
else:
  print((-b+(b**2-4*a*c)**(1/2))/(2*a))
  print((-b-(b**2-4*a*c)**(1/2))/(2*a))

 # https://forms.office.com/r/uYLQg0PLmQ
  
  
        
