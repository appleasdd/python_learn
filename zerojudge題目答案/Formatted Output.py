while True:
    try:
         x = eval(input())
         y = eval(input())
         print('Add:%10.3d'%(x+y))
         print('Mns:%10.3d'%(x-y))
         print('Mul:%10.3f'%(x*y))
         print('Div:%10.3f'%(x/y))
         print('Pwr:%10.3f'%(x**y))
         print('Qut:%10.3f'%(x//y))
         print('Mod:%10.3f'%(x%y))
         
    except:
        break
        

 