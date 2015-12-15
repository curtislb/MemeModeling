import argparse, os, sys
from Entry import Entry
import collections, operator

def count_base_urls(file):
    lines = []
    base_urls = collections.defaultdict(int)
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if (line):
                lines.append(line)
            else:
                entry = Entry(lines)
                lines = []
                # update map
                base_urls[entry.get_base_url()] += 1
                
    return base_urls




def main(argv):
   parser = argparse.ArgumentParser(description='Read in memetracker data, make models')
   parser.add_argument('-i','--input', help='Input file name',required=True)
   args = parser.parse_args()

   base_urls = count_base_urls(args.input)
   #sample thing
   print 'base urls:'
   sorted_base_urls = sorted(base_urls.items(), key=operator.itemgetter(1), reverse=True)
   for url, count in sorted_base_urls:
    print '{:<50} {:5}'.format(url, count)



if __name__ == '__main__':
   main(sys.argv[1:])