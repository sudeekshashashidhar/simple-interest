def simple_interest(p, t, r):
  print("The principle is", p)
  print("The time period is", t)
  print("The rate of interest is", r)

  si = (p  * t * r)/100
  print("The simple interest rate is Rs.", si)

  return si

p = float(input("Enter the principle amount: "))
t = float(input("Eneter the time period: "))
r = float(input("Enter the rate of interest: "))

simple_interest(p, t, r)