#!/usr/bin/env python
"""
Given a directory path, this searches all files in the path for a given text string 
within the 'word/document.xml' section of a MSWord .dotm file.
"""
# Your awesome code begins here!

import argparse
import glob
import os 
import sys
import zipfile

def search(criteria, path):
    count = 0
    matches = 0
    os.chdir(path)
    files = glob.glob('*.dotm')
    for file in files:
        count += 1
        zf = zipfile.ZipFile(file, 'r')
        content = zf.read('word/document.xml')
        if criteria in content:
            matches += 1
            index = content.index(criteria)
            match_text = 'Match in file {}, at ___{}____'.format(file, content[index - 40: index + 40])
            print (match_text)
    print ('Files searched: {}').format(count)
    print ('Matches found: {}').format(matches)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='choose text to seach for')
    parser.add_argument('--dir', help='add a directory, default is cwd')
    args = parser.parse_args()

    criteria = args.text
    directory = args.dir
    if directory:
        search(criteria, directory)
    else: 
        print ('ERROR: please type a valid command')
        sys.exit(1)
if __name__ == "__main__":
    main()