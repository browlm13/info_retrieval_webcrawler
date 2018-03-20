from src import webpage_accessor
import logging

# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#
#   Read robots.txt file and return list of normalized disallowed urls
#

def read_robots_dissaloud(site_url):
    forbidden_urls = []

    # get the robots.txt url for the seed url
    robots_url = site_url + "robots.txt"


    # extract the forbidden routes
    response_summary = webpage_accessor.pull_summary(robots_url, ['plain_text'])

    if not 'plain_text' in response_summary:
        logger.error("No Robots.txt Found")
        return []

    robots_string = response_summary['plain_text']

    if robots_string is not None:
        for line in robots_string.split("\n"):
            if line.startswith('Disallow'):
                forbidden = line.split(':')[1].strip()

                if forbidden[0] == '/':
                    forbidden = forbidden[1:]

                if site_url[-1] == '/':
                    site_url = site_url[:-1]

                # add site prefix
                forbidden_urls.append(site_url + '/' + forbidden)

    if len(forbidden_urls) == 0:
        logger.error("No Forbbiden URLs found in Robots.txt")

    return forbidden_urls


"""
"""
"""
#
#   Read robots.txt file and return list of normalized dissalowed urls
#
import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url(robots_url)
rp.read()

print(rp.can_fetch('*', url))
class Robot_Parser():
    
    def __init__(self):
        
    
# find forbidden urls
self.forbidden_urls = []

# get the robots.txt url for the seed url
robots_url = self.seed_url + "robots.txt"

# extract the forbidden routes
response_summary = url_accessor.get_response_summary(robots_url, self.url_resolver)

robots_string = self.file_parser.extract_plain_text(response_summary['binary_response_content'],
                                                    response_summary['content_type'])
if robots_string is not None:
    for line in robots_string.split("\n"):
        if line.startswith('Disallow'):
            forbidden = line.split(':')[1].strip()

            if forbidden[0] == '/':
                forbidden = forbidden[1:]

            seed_url = self.seed_url
            if self.seed_url[-1] == '/':
                seed_url = self.seed_url[:-1]

            # add site prefix
            self.forbidden_urls.append(seed_url + '/' + forbidden)
"""