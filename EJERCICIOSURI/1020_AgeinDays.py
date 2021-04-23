days = int(input())
years = int(days/365)
days -= years*365
months = int(days/30)
days -= months*30
print(format(years) +' ano(s)')
print(format(months) +' mes(es)')
print(format(days) +' dia(s)')