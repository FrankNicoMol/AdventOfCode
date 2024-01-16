from aoc import results, read_txt, remove_empty
import os
import numpy as np


def get_coords(where):
    coords = []
    for x,y in zip(where[0], where[1]):
        coords.append([x,y])
    return coords


def calc_dist(c1, c2, q):
    xi = [c1[0], c2[0]]
    yi = [c1[1], c2[1]]
    xi.sort()
    yi.sort()

    v = np.sum(q[xi[0]:xi[1], c1[1]])
    v += np.sum(q[c2[0], yi[0]:yi[1]])
    return v

def get_total_distance(coords, q):
    total = 0
    for i, c1 in enumerate(coords):
        for j, c2 in enumerate(coords[i + 1:]):
            total += calc_dist(c1, c2, q)
    return total

def dists(text, rep = 3):
    btext = text == '.'
    h, w = btext.shape
    cols = []
    rows = []

    for i in range(h):
        if np.sum(btext[i, :]) == w:
            cols.append(i)

    for i in range(w):
        if np.sum(btext[:, i]) == h:
            rows.append(i)

    ntext = np.ones(text.shape)

    for i in range(h):
        if np.sum(btext[i, :]) == w:
            ntext[i,:] = rep

    for i in range(w):
        if np.sum(btext[:, i]) == h:
            ntext[:,i] =  rep



    return ntext.astype(np.int64)
def get_value(file, second):
    text = read_txt(file)
    text = np.array([[*l] for l in text])
    if second:
        rep = 1000000
    else:
        rep = 2

    hashtags = np.where(text == '#')
    coords = get_coords(hashtags)
    d = dists(text, rep = rep)
    val = get_total_distance(coords, d)

    return val


day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
