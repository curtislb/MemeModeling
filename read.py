import argparse, os, sys
from Entry import Entry
import pdb

def open_and_test(file):
    lines = []
    entries = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if (line):
                lines.append(line)
            else:
                entry = Entry(lines)
                entries.append(entry)
                lines = []

    return entries




def main(argv):
   parser = argparse.ArgumentParser(description='Read in memetracker data, make models')
   parser.add_argument('-i','--input', help='Input file name',required=True)
   args = parser.parse_args()

   entries = open_and_test(args.input)
   #sample thing
   print "base urls:"
   for entry in entries:
    print '\t'+entry.get_base_url()



if __name__ == "__main__":
   main(sys.argv[1:])