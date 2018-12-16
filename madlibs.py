# This script reads a MadLib story from a .txt file and asks the user for a
# value for each section of text surrounded by ""
# For example, if "NOUN" is in the .txt, the user will be asked to provide a
# noun. Once the user enters a value for each section, the edited story will
# be printed.
import re
from pathlib import Path

def get_story():
    # Read in a MadLib story from a .txt file
    return Path("vacation_short.txt").read_text()

def get_matches(story):
    # Final all sections surrounded by ""
    # These will be the sections to be replaced in the story
    return re.findall(r'"[\w\s]+"', story)

# def sub_matches(matches, story):
#     # For each found section, ask the user for a value and place this value in the
#     # story
#     for match in matches:
#         value = input('Enter a ' + match + ':')
#         story = re.sub(match, value, story, 1)
#     return story

def sub_matches(matches, values, story):
    # For each found section, ask the user for a value and place this value in the
    # story
    for i, match in enumerate(matches):
        # value = input('Enter a ' + match + ':')
        story = re.sub(match, values[i], story, 1)
    return story

# # Print out the edited story
# print(story)
# story = get_story()
# matches = get_matches(story)
# print(sub_matches(matches, story))