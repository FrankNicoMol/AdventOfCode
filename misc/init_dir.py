import os
from pathlib import Path
import shutil
import sys

if __name__ == "__main__":
    n_args = len(sys.argv)
    year = sys.argv[1]
    start_day = sys.argv[2] if n_args > 3 else 1

    path = Path('').absolute().parent

    year_path = str(path / str(year))

    if os.path.isdir(year_path):
        print(f'Folder {year} at path {year_path} already exists.')
    else:
        input_path = f'{year_path}/input'
        os.makedirs(year_path)
        os.makedirs(input_path)

        for i in range(start_day, 26):
            shutil.copyfile('template.py', f'{year_path}\\day{i:02d}.py')
            with open(f'{input_path}\\day{i:02d}_input.txt', 'w') as fp:
                pass
            with open(f'{input_path}\\day{i:02d}_example.txt', 'w') as fp:
                pass
        shutil.copytree('aoc', f'{year_path}\\aoc')