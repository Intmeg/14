f = open(r'.\products.txt')
k = 0
for a in f:
    s = ''.join(a)
    x = open(r'.\products_new.csv')
    x[k].append(s)
    k += 1
    x.close()
f.close()

# НЕ РАБОТАЕТ
