# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    a=input()
    if (len(a)==10 and a.isdigit()):
        if re.findall(r'[789]\d{9}',a):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
