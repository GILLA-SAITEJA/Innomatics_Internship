# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab=int(input())
bc=int(input())
hyp=math.hypot(ab,bc)
ad=bc
op=str(int(round(math.degrees(math.acos(ad/hyp)))))
print(op+"°")
