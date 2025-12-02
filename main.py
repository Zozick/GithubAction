
#Алгоритм
def next_float(a,current,c,m):
    return ((a * current + c) % m)

#Проверка на совпадения
def has_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":

    b = []
    a = 1869525
    c= 1983904223
    m = 2**32
    b.append(next_float(a,76,c,m))
    sum = 0
    l = 0
    k=0
    B_m =0
    B_v = 0
    e = 10**6

    for i in range(e+1):
        b.append(next_float(a,b[i],c,m))
        b[i] = b[i]/m
        sum += b[i]
        #print(b[i], b[i]/m)
        if b[i] > 0.5:
            B_m += 1
        else:
            B_v += 1
    for j in range(e):
        l += (b[j]- sum/e) **2

    #Диспперсия
    ll = l/e
    lsum = sum/e




    print("Наличие повторяющихся чисел -",has_duplicates(b))
    print(f"мат ожидание = {sum/e}")
    print("Дисперсия", ll)
    print("Частотный тест", (lsum + ll**(1/2)) - (lsum - ll**(1/2)))
    print(f"меньше 0,5 = {B_m / e}, больше 0,5 = {B_v / e}")



