def read_txt(path):
    """read .txt file and strip"""

    with open(path) as file:
        lines = file.readlines()

    text = [line.strip() for line in lines]

    return text

def remove_empty(line):
    """removes empties"""

    new_line = [item for item in line if item != '']

    return new_line

def print_result(day, type, second, result):

    print(f'{day} - {type} - Part {1 + second}: {result}')



def results(fun, day):


    path = f'input/{day}_'

    for second_part in range(2):
        for j in range(2):
            if j:
                input = 'input'
            else:
                input = 'example'

            value = fun(f'{path}{input}.txt')
            print_result(day, input, second_part, value)