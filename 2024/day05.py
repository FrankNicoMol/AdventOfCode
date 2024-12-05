from aoc import get_lines, print_header, run_examples, print_solution
import os
import numpy as np
import itertools
from collections import defaultdict, deque




def get_day_number():
    """Obtain day number from filename."""

    filename = os.path.basename(__file__)
    no_extension = filename.split(".")[0]
    day_number = no_extension[-2:]
    day_integer = int(day_number)

    return day_integer


def print_solutions(lines, part=1):
    """Generate results and print solutions."""

    name = 'Part II' if part - 1 else 'Part I'
    print_solution(part=name, solution=get_solution(lines, part=part))
    if part - 1:
        print('')


def solver(day):
    """Generate the solutions for all data for given day."""

    # Load data
    lines = get_lines(day=day)

    # Part 1
    run_examples(day, lambda x: get_solution(x, part=1))
    print_solutions(lines, part=1)

    # Part 2
    run_examples(day, lambda x: get_solution(x, part=2))
    print_solutions(lines, part=2)


def get_solution(lines, part=1):
    """Generate the solution with given input lines."""

    # General applicability

    # Part I
    if not part - 1:
        solution = 0
        index = lines.index('')
        rules = [line.split('|') for line in lines[:index]]
        rules = np.array([[int(line[0]), int(line[1])]for line in rules])
        updates = lines[index+1:]
        updates = [[int(val) for val in line.split(',')] for line in updates]

        for update in updates:
            urules = [[a,b] for a,b in rules if a in update and b in update]
            correct = True
            for a,b in urules:
                if update.index(a) > update.index(b):
                    correct = False
                    break
            if correct:
                solution += update[len(update)//2]


    # Part II
    else:

        solution = 0
        index = lines.index('')
        rules = [line.split('|') for line in lines[:index]]
        rules = np.array([[int(line[0]), int(line[1])]for line in rules])
        updates = lines[index+1:]
        updates = [[int(val) for val in line.split(',')] for line in updates]

        for update in updates:
            urules = [[a,b] for a,b in rules if a in update and b in update]
            correct = True
            for a,b in urules:

                if update.index(a) > update.index(b):
                    correct = False
                    break
            if not correct:

                graph = defaultdict(list)
                indegree = defaultdict(int)
                indegree = defaultdict(int)

                for a, b in urules:
                    graph[a].append(b)
                    indegree[b] += 1
                    indegree[a] += 0
                queue = deque([node for node in indegree if indegree[node] == 0])
                result = []

                while queue:
                    current = queue.popleft()
                    result.append(current)
                    for neighbor in graph[current]:
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 0:
                            queue.append(neighbor)


                solution += result[len(result) // 2]



    return solution


if __name__ == "__main__":
    day = get_day_number()
    print_header(day=day)
    solver(day)
