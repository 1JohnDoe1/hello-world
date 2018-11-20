def elem(a):
    for i in range(12):
        print("Введите кол-во осадков в", i+1,"месяце(в мм)")
        x = int(input())
        a.append(x)
def sredn(a):
    sum = 0
    for i in range(12):
        sum += a[i]
    sum = sum // 12
    print("Среднее кол-во осадков(в мм) равно =",sum)
def max(a):
    max = 0
    for i in range(12):
        if a[i] > max : max=a[i]
    print("Максимальное кол-во осадков(в мм) равно =", max)

array=[] 
elem(array) 
sredn(array) 
max(array)
