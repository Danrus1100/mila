import argparse
from .constants import *
from .filesystem import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", "-v", action="version", version=VERSION)
    subparsers = parser.add_subparsers(dest='command')
    
    parser_init = subparsers.add_parser('init')
    parser_init.add_argument('file', type=str, help='File(s) to process')
    
    args = parser.parse_args()

if __name__ == "__main__":
    main()