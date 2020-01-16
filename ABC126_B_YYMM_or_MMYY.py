S = input()
first_half = int(S[:2])
second_half = int(S[2:])
is_month = lambda x: 1 <= x and x <= 12

if is_month(first_half) and is_month(second_half):
    print('AMBIGUOUS')
elif is_month(first_half) and not is_month(second_half):
    print('MMYY')
elif not is_month(first_half) and is_month(second_half):
    print('YYMM')
else:
    print('NA')

