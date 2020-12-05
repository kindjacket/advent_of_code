import re
from pathlib import Path

import requests
import os
from dotenv import load_dotenv


def get_input_for_day(day: int):
    """
    loads input data from advent of code webpage

    Returns:

    """
    load_dotenv()
    session_token = os.getenv("SESSION_TOKEN")
    response = requests.get(
        f"https://adventofcode.com/2020/day/{day}/input",
        headers={"Cookie": f"session={session_token}"},
    )
    return [i.decode("utf-8") for i in response.iter_lines()]


def get_day():
    day = int(re.findall("[\d]+", Path.cwd().name)[0])
    return int(day)


def get_input():
    day = get_day()
    return get_input_for_day(day)
