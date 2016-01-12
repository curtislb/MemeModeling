import argparse, sys
import cPickle as pickle
from datetime import datetime, timedelta


def compute_gamma(filename, delta_secs):
    with open(filename, 'rb') as f:
        domain_times = pickle.load(f)
        total_time = 0
        domain_count = 0
        format_str = '%Y-%m-%d %H:%M:%S'
        for domain in domain_times:
            infect_time, recover_time = domain_times[domain]
            if recover_time is None:
                ## count all infected domains as max_period
                #total_time += (31 * 24 * 3600) / delta_secs
                #domain_count += 1

                ## count all infected domains as 0
                #domain_count += 1

                # only count recovered domains
                continue

            else:
                infect_dt = datetime.strptime(infect_time, format_str)
                recover_dt = datetime.strptime(recover_time, format_str)
                time_delta = recover_dt - infect_dt
                total_time += float(time_delta.total_seconds()) / delta_secs
                domain_count += 1

        mean_period = float(total_time) / domain_count
        return 1.0 / mean_period


def main(argv):
    print compute_gamma('domain_times.pickle', 3600 * 24)


if __name__ == '__main__':
    main(sys.argv[1:])
