import os
from .constants import *

def create_directory(path):
    try:
        os.makedirs(path)
        print(f"Directory {path} created successfully")
    except OSError as error:
        print(f"Error creating directory {path}: {error}")

def main():
    create_directory(THEMES_DIR)

main()