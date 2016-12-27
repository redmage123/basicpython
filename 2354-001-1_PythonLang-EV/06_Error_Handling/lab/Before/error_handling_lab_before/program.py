#!/usr/local/bin/python3
import os

import loc

def count_lines(folder):
    print("Counting python files and lines in:\n{0}".format(folder))

    counter = loc.PythonLineCounter(folder)
    print("Number of files in folder: {0}".format(counter.count_files()))
    print("Number of lines in all files: {0}".format(counter.count_all_lines()))
    print()


def main():
    base_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
    print(base_folder)
    game_folder = os.path.abspath(os.path.join(base_folder, "input_files", "game"))
    missing_folder = "~/this_is_a_missing_folder"
    bad_folder = os.path.abspath(os.path.join(base_folder, "input_files", "bad"))
    bad2_folder = os.path.abspath(os.path.join(base_folder, "input_files", "bad2"))

    count_lines(missing_folder)
    count_lines(game_folder)
    count_lines(bad_folder)
    count_lines(bad2_folder)


if __name__ == "__main__":
    main()

