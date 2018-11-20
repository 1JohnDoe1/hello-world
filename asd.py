a = []
sum = 0
for i in range(12):
    print("Введите кол-во осадков в",i+1,  "месяце(в мм)")
    x = int(input())
    a.append(x)
for i in range(12):
    sum += a[i]
    sredn = sum // 12
print("Среднее кол-во осадков(в мм) равно =",sredn)
max = 0
for i in range(12):
    if a[i] > max : max=a[i]
print("Максимальное кол-во осадков(в мм) равно =", max)