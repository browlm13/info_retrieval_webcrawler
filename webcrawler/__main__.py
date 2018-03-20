#!/usr/bin/env python
import argparse
import sys
import logging

# my lib
from src import base_station
from src import summary

__author__ = 'LJ Brown'
__version__ = "1.0.1"

"""
                              Web Crawler
                             Command Line Tool
"""

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("output/output_log.txt"))
logger.addHandler(logging.StreamHandler(sys.stdout))

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

# display summary and write term frequency matrix to output file
summary.display_summary(args.output)