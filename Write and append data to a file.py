with open('output.txt','wt') as fh:
    a=input('enter text to write to the file:\n')
    fh.write(f'{a}\n')
    print('Data successfully written to output.txt')
with open('output.txt', 'a+') as fh:
    a=input('Enter the additional text to append\n')
    fh.write(a)
    print('Data successfully appended.')
with open('output.txt', 'rt') as fh:
    b=fh.read()
    print(f'Final content of output.txt:\n{b}')