'''link'''
def main():
    '''link'''
    link = input()
    link1 = 'https://ijudge.it.kmitl.ac.th/problems/'
    if not link.startswith(link1):
        print('INVALID')
        return
    code = link[len(link1):]
    if code.endswith('/'):
        code = code[:-1]
    if len(code) == 4 and code.isdigit() and code[0] in '0123':
        print(f'{code[0]} STAR')
    else:
        print('INVALID')
main()
