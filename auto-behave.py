from os.path import exists
from os import makedirs
import click

@click.group()
def main():
    """Use: auto-behave start_project <path_name>"""
    pass

@main.command(help='Create path structure')
@click.argument('path')
def start_project(path):
    if exists(path):
        print("Path existis")
    else:
        #Create paths
        makedirs(path)
        makedirs("{}/features/steps".format(path))
        makedirs("{}/helpers".format(path))

        #Create files
        readme = open("{}/README.md".format(path), "w")
        readme.write("## Autobehave")
        readme.close()

        feature = open("{}/features/example.feature".format(path), "w")
        feature.write("Feature: Tests\n")
        feature.write("\tScenario: Test1\n")
        feature.write("\tGiven\n")
        feature.write("\tWhen\n")
        feature.write("\tThen\n")
        feature.close()

        steps = open("{}/features/steps/steps.py".format(path), "w")
        steps.write("from behave import *")
        steps.write("\n\n")
        steps.write("@step('\"{test}\"')\n")
        steps.write("def test(context, test):\n")
        steps.write("\tpass")
        steps.close()

if __name__ == '__main__':
    main()
