from aoc import results
import os

def hash_for_string(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def operation(string):

    if string.find('=') != -1:
        v = string.find('=')
        label = string[:v]
        val = string[v+1:]
        return label, val, True
    else:
        v = string.find('-')
        label = string[:v]
        val = ''
        return label, val, False


def get_value(file, second):

    strings = file[0].split(',')

    if not second:
        val = 0
        for string in strings:
            val += hash_for_string(string)
    else:
        boxes = {}

        for s in strings:
            label, val, eq = operation(s)
            hash_label = hash_for_string(label)
            in_dict = {label: val}
            if eq:
                if hash_label in boxes.keys():
                    boxes[hash_label][label] = val
                else:
                    boxes[hash_label] = in_dict
            else:
                if hash_label in boxes.keys():
                    if label in boxes[hash_label].keys():
                        del boxes[hash_label][label]

        total = 0
        for key in boxes.keys():
            for i, label in enumerate(boxes[key].keys()):
                total += (key + 1) * int(boxes[key][label]) * (i + 1)

        val = total
    return val


day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
