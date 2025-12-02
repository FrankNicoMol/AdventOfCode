import pandas as pd
import os
from pathlib import Path


def get_github_page(year, day):
    """Get url for the GitHub page."""

    github_page = ''
    if year in [2022, 2023, 2024]:
        github_page = f'https://github.com/FrankNicoMol/AdventOfCode/blob/main/{year}/day{day:02d}.py'
    if year in [2021, 2025]:
        github_page = f'https://github.com/FrankNicoMol/AdventOfCode/blob/main/{year}/day{day:02d}/day{day:02d}.py'

    return github_page


def get_stars(df, year, day):
    """Get number of stars acquired for given day."""

    stars = ' '
    stars_day = df[str(year)][day - 1]
    if stars_day > 0:
        stars = f' {":star:" * stars_day} '

    return stars


def get_string_per_day(df, years, day):
    """Get string per day."""

    day_string = f'| Day {day:02d} |'
    for year in years:
        if year == 2025 and day > 12:
            day_string += f':no_entry_sign: |'
        else:
            stars = get_stars(df, year, day)
            github_page = get_github_page(year, day)
            advent_of_code_url = f'https://adventofcode.com/{year}/day/{day}'
            day_name = f':page_facing_up:'  # f'Day {day:02d}'

            day_string += f' [{day_name}]({advent_of_code_url}) : [{stars}]({github_page}) |'
    day_string += '\n'
    return day_string


def get_years(df):
    """Get all years in DataFrame."""

    years = [int(year) for year in df.columns[1:]]

    return years


def get_all_days(df):
    """Get string with stars for all days for each year."""

    years = get_years(df)
    all_years_string = ''
    for day in df['Day']:
        all_years_string += get_string_per_day(df, years, day)

    return all_years_string


def get_table_header(df):
    """Get MarkDown table header for all years."""

    years = get_years(df)
    header = '| '
    for year in years:
        advent_of_code_url = f'https://adventofcode.com/{year}'
        github_url = f'https://github.com/FrankNicoMol/AdventOfCode/tree/main/{year}'
        header += f'| [{year}]({advent_of_code_url}) - [Repo]({github_url}) '
    header += '|\n'

    for _ in range(len(years) + 1):
        header += '|:-----'
    header += '|\n'

    return header


def get_markdown_table(csv_name, data_path='misc/data'):
    csv_path = os.path.join(data_path, csv_name)
    df = pd.read_csv(csv_path)

    markdown_table = get_table_header(df)
    markdown_table += get_all_days(df)

    markdown_header = "# Advent of Code\n\nSolutions to the puzzles of [Advent Of Code (AOC)](https://adventofcode.com/)\n\nPuzzles solved:\n\n"
    markdown_readme = markdown_header + markdown_table

    # with open(os.path.join(data_path, 'md.txt'),  'w') as file:
    with open("README.md", 'w') as file:
        file.write(markdown_readme)


if __name__ == '__main__':
    csv_file = 'stars.csv'

    get_markdown_table(csv_file)
