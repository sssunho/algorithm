word = input()
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

len_num = 0
for ca in croatia_alphabet:
    if ca in word:
        if ca == 'dz=':
            croatia_alphabet.remove('z=')
        len_num += len(ca)

print(len_num)
