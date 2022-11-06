# Simple GREP CLI program with a lot of stuff cut out compared
# to the original GREP
# Only have 'w', 'i', and no option as the options


import os
import re
import sys


def get_args():
    """Gets the argument from the user using sys.argv
    If the argument is wrong, raises a ValueError

    Returns:
    args    - A list that consist of [mode, pattern, path]
    """

    args = []

    # Checks if the given argument is a list of 3 or 4 items
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        raise ValueError

    # Checks if the second argument is a [mode] option
    # and checks if the given argument is a list of 4 items
    if (sys.argv[1] == "-w" or sys.argv[1] == "-i") and not len(sys.argv) < 4:
        args.append(sys.argv[1])
        args.append(sys.argv[2])
        args.append(sys.argv[3])

    # Checks if the second argument is not an unspecified [mode] option
    # but is a pattern
    elif not sys.argv[1].startswith("-"):
        args.append(None)
        args.append(sys.argv[1])
        args.append(sys.argv[2])

    else:
        raise ValueError

    return args


def check_wildcard(pattern: str):
    """Checks if there is 1 or less wildcard (*)
    Returns True if there is 1 or less, False otherwise"""

    return pattern.count("*") < 2


def get_pattern(mode: str, pattern: str):
    """Gets a normalized pattern from the user's input by
    converting the wildcard (*) and the pattern into a
    re.Pattern object

    Args:
    mode    - Can be -w, -i, or None
    pattern - A str object containing the word/pattern being searched
              with empty strings still being a valid input

    Returns:
    re.Pattern obj - A Pattern object from the re module so searching
                     becomes more efficient
    """

    # Checks if there is 1 or less wildcard, if there are more, raises
    # a ValueError
    if check_wildcard(pattern):

        # If -w mode is chosen, changes * to \S*, meaning "anything that
        # is not a whitespace", ^ is to check if its at the start of the
        # string and $ is to check if its at the end of the string, 
        # the same applies to all other modes
        if mode == "-w":
            pattern = pattern.replace("*", "\S*")
            return re.compile(f'(^|\s){pattern}(\s|$)')

        # If -i mode is chosen, changes * to .*, meaning "anything" and
        # sets the IGNORECASE flag on
        if mode == "-i":
            pattern = pattern.replace("*", ".*")
            return re.compile(pattern, re.IGNORECASE)

        # If None mode, changes * to .*, similar to how it is on -i mode
        # but case-sensitive
        pattern = pattern.replace("*", ".*")
        return re.compile(pattern)

    else:
        raise ValueError


def print_match(path: str, line_num: int, line: str):
    """Prints the matching line, line number, and file in a formatted way
    when it matches the pattern

    Args:
    path     - The file where the match was found
    line_num - The line number where the match was found
    line     - The line where the match was found (may or may not include
               the matched word due to formatting)

    Format:
    path     - Left aligned, 40 spaces reserved (assumes path is always <= 40)
    line_num - Left aligned, 3 spaces reserved, starts from 1
    line     - Left aligned, only the first 40 chars
    """

    print(f'{path:<40} line {line_num:<3} {line[:40]:<40}')


def is_match(mode: str, pattern: str, line: str):
    """Checks if there is 'pattern' on the current 'line'

    Args:
    mode    - Can be -w, -i, or None
    pattern - A str object containing the word/pattern being searched
    line    - The line that wants to be searched

    Returns:
    re.Match obj - If a match is found, the re.Match object will always
                   be True, None (False) otherwise
    """

    ptrn = get_pattern(mode, pattern)
    return ptrn.search(line)


def scan_file(file_path: str, mode: str, pattern: str):
    """Opens a file and searches for the pattern inside the file
    by going 1 line at a time

    Args:
    file_path - Path to file
    mode      - Can be -w, -i, or None
    pattern   - A str object containing the word/pattern being searched
    """

    # Assume input can only be .txt files
    if not file_path.endswith('.txt'):
        raise ValueError

    with open(file_path) as f:
        line_count = 1
        for lines in f:
            if is_match(mode, pattern, lines):
                print_match(file_path, line_count, lines.strip())
            line_count += 1


def scan_dir(path: str, mode: str, pattern: str):
    """Iterate through all the subdirs and files inside a given root dir
    and performs scan_file on all the files

    Args:
    path    - Path to dir
    mode    - Can be -w, -i, or None
    pattern - A str object containing the word/pattern being searched
    """

    for root, dirs, files in os.walk(path):
        for file in files:
            fp = os.path.join(root, file)
            scan_file(fp, mode, pattern)


def main():
    """Main program to run, gets the argument first and checks if
    path is a file or a dir and calls the appropriate function
    If the path is not a file nor a dir, inform the user that said
    path can't be found and exits the program
    """

    mode, pattern, path = get_args()
    if os.path.isfile(path):
        scan_file(path, mode, pattern)

    elif os.path.isdir(path):
        scan_dir(path, mode, pattern)

    else:
        print(f'Path <{path}> not found')


if __name__ == '__main__':
    try:
        main()

    except ValueError:
        print("Invalid Argument(s)")

    except:
        print("Unexpected Exception")
