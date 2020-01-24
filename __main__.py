import os
import argparse

os.chdir(os.path.dirname(os.path.realpath(__file__)))

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cli", help="run command line interface",
                    action="store_true")
parser.add_argument("-g", "--gui", help="run graphical user interface",
                    action="store_true")
args = parser.parse_args()
if args.gui:
    os.system("python ./gui/__main__.py")
elif args.cli:
    os.system("python ./cli/__main__.py")
else:
    parser.print_help()
