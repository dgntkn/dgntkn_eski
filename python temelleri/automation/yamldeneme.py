import yaml
import sys
with open("c:/Users/davutd/Documents/github/python temelleri/list.yaml") as yamlFile:
    yamlDict = yaml.full_load(yamlFile)
    print(yamlDict)
