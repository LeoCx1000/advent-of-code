from aoc import input_for
import numpy as np


def pt_1():
    """(N/W/S/E) = North, West, South, East"""
    puzzle_in = input_for(day=8)
    array = np.array([np.fromstring(" ".join(x), sep=" ") for x in puzzle_in.splitlines()])
    vt = 0  # Visible trees count
    for ix, tree_arr in enumerate(array):
        for iy, tree in enumerate(tree_arr):

            arN = array[:ix, iy : iy + 1]
            if not arN.size or tree > arN.max():
                vt += 1
                continue

            arW = array[ix : ix + 1, :iy]
            if not arW.size or tree > arW.max():
                vt += 1
                continue

            arS = array[ix + 1 :, iy : iy + 1]
            if not arS.size or tree > arS.max():
                vt += 1
                continue

            arE = array[ix : ix + 1, iy + 1 :]
            if not arE.size or tree > arE.max():
                vt += 1
                continue
    return vt


def pos(tup: tuple[np.ndarray]):
    if tup[0].size:
        return tup[0].min() + 1
    return None


def pt_2():
    """(N/W/S/E) = North, West, South, East"""
    puzzle_in = input_for(day=8)
    array = np.array([np.fromstring(" ".join(x), sep=" ") for x in puzzle_in.splitlines()])
    ms = 0  # max score
    for ix, tree_arr in enumerate(array):
        for iy, tree in enumerate(tree_arr):
            arN = array[:ix, iy : iy + 1].flatten()[::-1]
            vsN = pos(np.where(arN >= tree)) or arN.size
            arW = array[ix : ix + 1, :iy].flatten()[::-1]
            vsW = pos(np.where(arW >= tree)) or arW.size
            arS = array[ix + 1 :, iy : iy + 1].flatten()
            vsS = pos(np.where(arS >= tree)) or arS.size
            arE = array[ix : ix + 1, iy + 1 :].flatten()
            vsE = pos(np.where(arE >= tree)) or arE.size
            score = vsN * vsW * vsS * vsE
            if score > ms:
                ms = score

    return ms


if __name__ == "__main__":
    print("part one: ", pt_1())
    print("part two: ", pt_2())
