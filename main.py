n = int( input( 'n = ' ) )
k = int( input( 'k = ' ) )
m, rem = divmod( n, k )
res = []
print(k,rem,m)
for i in range(rem):
    res.append( m+1 )
for i in range( k-rem ):
    res.append(m)
print( f'Разбиение массива длиной {n} на {k} подмассивов с длинами:' )
print(res)