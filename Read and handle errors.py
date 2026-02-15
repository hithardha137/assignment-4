try:
    with open('sample.txt','rt') as fh:
        content=fh.readlines()
        for i in content:
            print(f'Line{content.index(i)+1}:{i}')


except FileNotFoundError:
    print('Error:The file \'sample.txt\' was not found')