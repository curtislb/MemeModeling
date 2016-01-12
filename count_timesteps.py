import dateutil.parser as dt_parser
import datetime as dt
import matplotlib.pyplot as plt
"""
takes len_time_unit in seconds, and domain_times dict.
takes start_time string, i.e. when is the beginning of the timerange we're dealing with (e.g. '2008-08-01', '2008-08-01 00:00:01')
returns 3 arrays S, I, R: S[0] is the number susceptible at timestep 0, etc.
"""

total_timesteps = 31

def count_timesteps(len_time_unit, start_time, domain_times):

    len_t = dt.timedelta(seconds=len_time_unit)
    init_t = dt_parser.parse(start_time)

    S = []
    I = []
    R = []

    # while loop to go through each timeslot
    t = 0
    while(t < total_timesteps): #stop after a year
        t_min = init_t + t * len_t
        t_max = init_t + (t+1) * len_t

        num_S = 0
        num_I = 0
        num_R = 0


        #go through dict, if t_max < infect its susceptible
        # if infect < t_max && t_max < recover, its infected
        # if recover < t_max, its recovered
        # mark breakflag as false if breakflag && recover >= t_min
        for domain in domain_times:
            infect_time, recover_time = domain_times[domain]
            infect_time = dt_parser.parse(infect_time)
            if recover_time is not None:
                recover_time = dt_parser.parse(recover_time)
            else:
                recover_time = dt_parser.parse(str(dt.MAXYEAR))


            if (t_max < infect_time):
                num_S += 1
            elif ((infect_time < t_max and t_max < recover_time) or recover_time < t_max) :
                num_I += 1
            # elif (recover_time < t_max):
            #     num_R += 1

        S.append(num_S)
        I.append(num_I)
        R.append(num_R)

        t += 1

    return S, I, R

def graph_SIR(S, I, R):
    tot = S[0] + I[0] + R[0]
    I = [i*1./tot for i in I]
    S = [s*1./tot for s in S]
    R = [r*1./tot for r in R]

    # now plot the graph of S, I, R over STEPS
    p1, = plt.plot(range(total_timesteps), I, label='infected')
    p2, = plt.plot(range(total_timesteps), S, label='susceptible')
    p3, = plt.plot(range(total_timesteps), R, label='recovered')
    plt.title('SIR values over all steps')
    plt.legend()
    axes = plt.gca()
    axes.set_xlabel('steps')
    axes.set_ylabel('values of SIR')
    plt.show()

