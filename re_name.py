#!/usr/bin/env python3
"""
This is the script to organize all of text file with md format into a post
This is useful for lazy organizing and naming
"""
from datetime import datetime
from os import rename
import argparse

import yaml
from no_accent import create_name_for_link

current_date = str(datetime.now().date())


def get_information_header(filename):
    with open(filename, 'r') as file:
        yaml_head = ''
        counter = 0
        while counter < 2:
            line = file.readline()
            if line == '---\n':
                counter += 1
                continue
            yaml_head += line
        header = yaml.load(yaml_head)
    return header


def prepare_the_file(filename):
    header = get_information_header(filename)
    raw_title = header['title']
    if 'date' in header:
        current_date = str(header['date'])
    else:
        current_date = str(datetime.now().date())
    output_filename = '-'.join([current_date, create_name_for_link(raw_title)]) + '.md'
    rename(filename, output_filename)
    rename(output_filename, '../' + output_filename)


def main():
    parser = argparse.ArgumentParser(description='Process a file name.')
    parser.add_argument('filename', type=str,
                        help='Input the name of your post')
    args = parser.parse_args()
    filename = args.filename
    prepare_the_file(filename)


if __name__ == '__main__':
    main()
