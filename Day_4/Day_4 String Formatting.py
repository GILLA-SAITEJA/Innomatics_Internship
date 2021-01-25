def print_formatted(number):
    # your code goes here
    w = len(str(bin(n)).replace('0b',''))

    for i in range(1, n+1):
        j = str(i).rjust(w)
        o = oct(int(i)).split('o')[1].rjust(w)
        h = hex(int(i)).split('x')[1].upper().rjust(w)
        b = bin(int(i)).split('b')[1].rjust(w)
        print(j, o, h, b)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
