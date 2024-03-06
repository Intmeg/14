f = open(r'C:\Users\TEMP.DT.001\PycharmProjects\predprof14\products.txt')
k = 0
for a in f:
    s = ''.join(a)
    x = open(r'C:\Users\TEMP.DT.001\PycharmProjects\predprof14\products_new.csv')
    x[k].append(s)
    k += 1
    x.close()
f.close()

# НЕ РАБОТАЕТ