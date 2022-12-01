from fileReader import fileToStringList
from parser import parse
from robot import execute
from report import generate

# read file line by line
rawActions = fileToStringList("TestCases.txt")

# parse action and its arguments
actions = parse(rawActions)

# execute action
execute(actions)

# create report
generate(actions)