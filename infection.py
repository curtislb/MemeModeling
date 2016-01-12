import numpy as np
import pdb
import argparse, sys
import matplotlib.pyplot as plt

"""
to run: python infection.py -h
"""
DEFAULT_EPS = 1 #there is no eps?? 0.2 spreads it well tho
DEFAULT_BETA = 3.60000
DEFAULT_GAMMA = 2.03283970531
DEFAULT_STEPS = 31

EPS = 0.0
BETA = 0.0
GAMMA = 0.0
STEPS = 0

INITIAL_I = 0.01
INITIAL_S = 0.99
INITIAL_R = 1 - INITIAL_I - INITIAL_S

def next_S(S, I):
    next = S[-1] - EPS * BETA * S[-1] * I[-1]
    S = np.concatenate((S, np.array([next])))
    return S

def next_I(I, S):
    next = I[-1] + EPS * BETA * S[-1] * I[-1] - EPS * GAMMA * I[-1]
    I = np.concatenate((I, np.array([next])))
    return I

def next_R(R, I):
    next = R[-1] + EPS * GAMMA * I[-1]
    R = np.concatenate((R, np.array([next])))
    return R

def run_sim(I, S, R):
    cur_step = 0
    while(cur_step < STEPS-1 or I[-1] > 1):
        cur_step += 1
        S = next_S(S, I)
        I = next_I(I, S)
        R = next_R(R, I)

    return I,S,R

def graph(I, S, R):
    # now plot the graph of S, I, R over STEPS
    p1, = plt.plot(range(STEPS), I, label='infected')
    p2, = plt.plot(range(STEPS), S, label='susceptible')
    p3, = plt.plot(range(STEPS), R, label='recovered')
    plt.title('SIR values over all steps')
    plt.legend()
    axes = plt.gca()
    axes.set_xlabel('steps')
    axes.set_ylabel('values of SIR')
    plt.show()

def main(argv):
    # arg stuff
    parser = argparse.ArgumentParser(description='Read in constants (optional), run SIR')
    parser.add_argument('--epsilon', type=float, default=DEFAULT_EPS, help='epsilon value for SIR',required=False)
    parser.add_argument('--beta', type=float, default=DEFAULT_BETA, help='beta value for SIR',required=False)
    parser.add_argument('--gamma', type=float, default=DEFAULT_GAMMA, help='gamma value for SIR',required=False)
    parser.add_argument('--steps', type=int, default=DEFAULT_STEPS, help='number of steps to run SIR',required=False)
    parsed_args = parser.parse_args()

    if '--epsilon' not in argv:
        print "Using default value for epsilon..."
    if '--beta' not in argv:
        print "Using default value for beta..."
    if '--gamma' not in argv:
        print "Using default value for gamma..."
    if '--steps' not in argv:
        print "Using default value for steps..."

    global EPS, BETA, GAMMA, STEPS
    EPS = parsed_args.epsilon
    BETA = parsed_args.beta
    GAMMA = parsed_args.gamma
    STEPS = parsed_args.steps

    # set up S,I,R and initial values
    I = np.array([])
    S = np.array([])
    R = np.array([])
    I = np.concatenate((I, np.array([INITIAL_I])))
    S = np.concatenate((S, np.array([INITIAL_S])))
    R = np.concatenate((R, np.array([INITIAL_R])))
    # now run
    print "Running SIR for", STEPS, "steps..."
    I, S, R = run_sim(I, S, R)
    #now graph
    print "Generating graph of S,I,R over time..."
    graph(I, S, R)


if __name__ == '__main__':
   main(sys.argv[1:])
