import os 
import json
import shutil
from subprocess import PIPE, run
import sys


def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join()



if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("Mast pass a source -only.")
    
    source, target = args[1:]
    main(source, target)


