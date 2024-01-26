from aoc import results, read_txt, remove_empty
import os
import numpy as np
import itertools

def get_sets(p):
    string = ''.join(p)
    q = str(string).split('.')
    lens = [len(qi) for qi in q if len(qi) != 0]
    return lens


def rec(p, n,qms,  c):
    global tdict

    if c != len(qms):
        gsets =get_sets(p[:qms[c]])
        ti = np.array(gsets)
        if len(ti):
            ni = n[:len(ti)]


            if ti[-1] > ni[-1] or not np.array_equal(ti[:-1], ni[:-1]):
                tdict[str(gsets) + ',' + p[qms[c-1]] + ',' + str(c)] = 0
                return 0

        if c!= 0:
            if str(gsets) + ',' + p[qms[c-1]] + ',' + str(c) in tdict.keys():
                return tdict[str(gsets) + ',' + p[qms[c-1]] + ',' + str(c)]
        else:
            if str(gsets) + ',' + str(c) in tdict.keys():
                return tdict[str(gsets) + ',' + str(c)]

        t1 = p.copy()
        t1[qms[c]] = '#'
        t2 = p.copy()
        t2[qms[c]] = '.'

        a1 = rec(t1, n,qms, c+1)
        a2 = rec(t2, n,qms, c+1)
        val = a1 + a2
        if c!= 0:
            key = str(gsets) + ',' + p[qms[c-1]] + ',' + str(c)
        else:
            key = str(gsets) + ',' + str(c)
        tdict[key] = val
        return val
    else:
        if np.array_equal(np.array(get_sets(p)), n):
            key = str(get_sets(p)) + ',' + p[qms[c-1]] + ',' + str(c)
            tdict[key] = 1
            return 1
        else:
            key = str(get_sets(p)) + ',' + p[qms[c-1]] + ',' + str(c)
            tdict[key] = 0
            return 0


def get_line_val(line, second):
    global tdict
    tdict = {}

    v, n = line.split(' ')
    n = np.asarray(n.split(',')).astype(int)
    if second:
        v = '?'.join([v] * 5)

    n = list(n) * 5 if second else list(n)
    qms = np.where(np.array([*v]) == '?')


    total = rec(np.array([*v]), n, qms[0], 0)


    return total


def get_value(text, second):
    val = np.sum([get_line_val(line, second) for line in text])

    return val


def get_value(text, second):

    val = np.sum([get_line_val(line, second) for line in text])

    return val

tdict = {}
day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
