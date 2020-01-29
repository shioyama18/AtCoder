Sa = list(input())
Sb = list(input())
Sc = list(input())
next_turn = 'a'

while True:
    if next_turn == 'a':
        if len(Sa) == 0:
            print('A')
            break
        next_turn = Sa.pop(0)
    elif next_turn == 'b':
        if len(Sb) == 0:
            print('B')
            break
        next_turn = Sb.pop(0)
    else:
        if len(Sc) == 0:
            print('C')
            break
        next_turn = Sc.pop(0)
