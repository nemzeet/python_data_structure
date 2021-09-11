#재귀호출.py
def f1(num):
    tot=0
    for i in range(1,num+1):
        tot+=i
    return tot

def f2(num):
    if num==1:
        return 1
    return num+f2(num-1)



print(f1(10))
print(f2(10))

#10+f(9)
#10+(9+f(8))
#...
#10+9+8+7+6+5+4+3+2+1
