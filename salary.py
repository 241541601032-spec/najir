basic = float(input("Enter basic salary: "))

hra = basic * 20 / 100
da = basic * 10 / 100
ta = basic * 5 / 100

gross = basic + hra + da + ta

print("HRA (20%):", hra)
print("DA (10%):", da)
print("TA (5%):", ta)
print("Gross Salary:", gross)
