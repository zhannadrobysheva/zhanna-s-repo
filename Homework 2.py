a = int(input('На этом факультете есть ')) 
b = str(a) 
if 10 < a < 20 or a == 0 or a == 5 or a == 6 or a == 7 or a == 8 or a == 9: 
 print( a, 'магистратур') 
elif b[-1] == 0 or b[-1] == 5 or b[-1] == 6: 
 print( a, 'магистратур') 
elif b[-1] == 7 or b[-1] == 8 or b[-1] == 9: 
 print(a, 'магистратур') 
elif b[-1] == 1: 
 print(a, 'магистратура') 
elif a == 1: 
 print( a, 'магистратура') 
else: 
 print( a, 'магистратуры')