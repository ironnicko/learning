# n = int(input('Enter the limit:'))
# print(*[i for i in range(1, n + 1)])
# for i in range(n - 1, 1, -1):
#     print(f' '*(2*(i-1)) + f'{i}')
# print(*[i for i in range(1, n+1)])

result_str=""    
for row in range(0,25):    
    for column in range(0,25):     
        if (((row == 0 or row == 24) and column >= 0 and column <= 24) or row+column==24):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)