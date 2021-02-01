# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
v=input()
v1=''.join(v.split())
b=re.findall(r'(?<=[BDCFGHJKLMNPQRSTVWXYZbdcfghjklmnpqrstvwxyz])([AEIOUaeiou]{2,})(?=[DBCFGHJKLMNPQRSTVWXYZdcbfghjklmnpqrstvwxyz])',v1)

if b:
    for x in b:
        print(x)
else:
    print('-1')
#import re
#s = '[qwrtypsdfghjklzxcvbnm]'
#a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
#print('\n'.join(a or ['-1']))
