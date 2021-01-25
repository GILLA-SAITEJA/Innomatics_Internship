if __name__ == '__main__':
    s = input()
    for i in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        if any(eval("a." + i + "()") for a in s):
            print(True)
        else:
            print(False)
