#кількість рядків
a,b = int(input()), int(input())
#кількість стовбців
c,d = int(input()), int(input())

#табуляція в першому рядку
print('\t',end='')
#формує перший рядок після табуляції
for i in range(c,d+1):
    print(i,end ='\t')
print('', end='\n')
# сама табличка перемножених значень
for i in range (a,b+1):
    print(i,end = '\t')
    for j in range (c,d+1):
        print(i*j, end='\t')
    # починатиме з нового рядка 
    print('')

