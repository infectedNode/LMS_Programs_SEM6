a = input()
b = input()
if not a.isdigit() or not b.isdigit():
    print('error')
else:
    print(int(a) + int(b))
