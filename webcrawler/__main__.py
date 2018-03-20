#!/usr/bin/env python
import sys
import argparse

# my lib
from src import base_station
from src import summary

__author__ = 'LJ Brown'


"""
                              Web Crawler
                             Command Line Tool

"""

# Default Parameters
SEED_URL = "http://lyle.smu.edu/~fmoore/"
MAX_URLS_TO_INDEX = None
STOPWORDS_FILE = "stopwords.txt"

parser = argparse.ArgumentParser( description='Scrape A Website.' )
parser.add_argument('-n', '--number', help='Maximum number of files to index. Will Crawl every page by default.', type=int, default=MAX_URLS_TO_INDEX)
parser.add_argument('-o', '--output', help='Output file name', required=True, type=str)
parser.add_argument('-i', '--input', help='Stopwords File path. Format: one word per line .txt file.', type=str, default=STOPWORDS_FILE)
parser.add_argument('-u', '--url', help='Website to crawl and index.', type=str, default=SEED_URL)
args = parser.parse_args()

# crawl site
bs = base_station.Base_Station()
bs.scrape_website(seed_url=args.url, output_directory=args.output, max_urls_to_index=args.number, stopwords_file=args.input)

# display summary
summary.summarize(args.output)
