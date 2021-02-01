# Enter your code here. Read input from STDIN. Print output to STDOUT
#n=input()
#n1=input()
#import re
#index = 0
#if re.search(n1, n):
 #   while index+len(n1) < len(n):
  #      m = re.search(n1, n[index:]) #begins search with new index

   #     print("({0}, {1})".format(index+m.start(), index+m.end()-1))

    #    index += m.start() + 1 #assign new index by +1
#else:
#    print((-1, -1))

import re
n=input()
n1=re.compile(input())
n1.search(n)
#index = 0
m = n1.search(n) #begins search with new index
if not m:
    print((-1, -1))
while m:
    print((m.start(), m.end()-1))
    m = n1.search(n,m.start()+1)
