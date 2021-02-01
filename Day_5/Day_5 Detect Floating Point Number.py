# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    print(bool(re.match(r'[+-]?\d*\.\d+$',input())))
