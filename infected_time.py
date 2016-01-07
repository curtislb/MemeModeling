import argparse, sys
import numpy as np

from Entry import Entry, base_url


def get_infected_times(filename, meme):
    lines = []
    domain_times = {}
    entries = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if (line):
                lines.append(line)
            else:
                entry = Entry(lines)
                lines = []
                
                for quote in entry.quotes:
                    if meme in quote:
                        entry_domain = entry.get_base_url()
                        if entry_domain not in domain_times:
                            domain_times[entry_domain] = [entry.timestamp, None]

                        for link in entry.links:
                            link_domain = base_url(link)
                            if link_domain in domain_times:
                                domain_times[link_domain][1] = entry.timestamp

    return domain_times


def main(argv):
    parser = argparse.ArgumentParser(
        description='Find first and last infected times of memetracker domains'
    )
    parser.add_argument('-i','--input', help='Input file name', required=True)
    parser.add_argument('-m', '--meme', help='Meme string', required=True)
    args = parser.parse_args()

    domain_times = get_infected_times(args.input, args.meme)
    for domain in domain_times:
        infect_time, recover_time = domain_times[domain]
        print '{:<50} {:<25} {:<25}'.format(domain, infect_time, recover_time)


if __name__ == '__main__':
    main(sys.argv[1:])