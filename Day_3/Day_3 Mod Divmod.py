# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = [int(input()) for i in '12']
print((a//b),(a%b),divmod(a,b),sep="\n")
