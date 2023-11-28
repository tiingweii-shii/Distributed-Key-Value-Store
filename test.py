#!/usr/bin/env python

import getpass, os, argparse, atexit
from run import Simulation

LEADERBOARD_OUTPUT = '/course/cs3700f20/stats/project6/'

# Constants for tuning the difficulty of the tests
PACKETS_LOW = 500.0
PACKETS_MID = 800.0
PACKETS_HIGH = 1000.0
REPLICAS = 5.0
MAYFAIL_LOW = 0.01
MAYFAIL_HIGH = 0.1
LATENCY_LOW = 0.05 # In fractions of a second
LATENCY_MID = 0.09 
LATENCY_HIGH = 0.5

parser = argparse.ArgumentParser()
parser.add_argument("--config-directory",
                    dest='config_dir',
                    default='',
                    help='A subdirectory containing test configs (Default: use the current directory)')
parser.add_argument("--silence",
                    dest='silence',
                    action='store_true',
                    help='Pipe stdout and stderr of replicas to /dev/null (Default: False)')
args = parser.parse_args()

sim = None

# Attempt to kill child processes regardless of how Python shuts down (e.g. via an exception or ctrl-C)
@atexit.register
def kill_simulation():
    if sim:
        try: sim.shutdown()
        except: pass

def run_test(filename, description, log=None):
    global sim
        
    sim = Simulation(os.path.join(args.config_dir, filename), args.silence)
    sim.run()
    sim.shutdown()
    stats = sim.stats    

    passed = sim.correctness_check()

    if passed:
        perf = sim.performance_tests()

        if log:
            log.write('%s %i %i %i %i %i %i %f %f\n' % (filename, stats.total_msgs, 
                                                        stats.failed_get, stats.unanswered_get,
                                                        stats.failed_put, stats.unanswered_put,
                                                        stats.duplicates,
                                                        stats.mean_latency, stats.median_latency))  

        print '\t%-60s\t[PASS]\tPerformance Tiers:' % (description), 
        for t in perf:
            print ' %i' % (t)
        print ''
    else:
        print '\t%-60s\t[FAIL]' % (description)

    return passed

trials = []

print 'Basic tests:'
trials.append(run_test('simple-1.json', 'No drops, no failures, 80% read'))
trials.append(run_test('simple-2.json', 'No drops, no failures, 20% read'))

print 'Unreliable network tests:'
trials.append(run_test('unreliable-1.json', '5% drops, no failures, 20% read'))
trials.append(run_test('unreliable-2.json', '10% drops, no failures, 20% read'))
trials.append(run_test('unreliable-3.json', '15% drops, no failures, 20% read'))

print 'Crash failure tests:'
trials.append(run_test('crash-1.json', 'No drops, 1 replica failure, 20% read'))
trials.append(run_test('crash-2.json', 'No drops, 2 replica failures, 20% read'))
trials.append(run_test('crash-3.json', 'No drops, 1 leader failure, 20% read'))
trials.append(run_test('crash-4.json', 'No drops, 2 leader failures, 20% read'))

print 'Partition tests:'
trials.append(run_test('partition-1.json', 'No drops, 1 easy partition, 20% read'))
trials.append(run_test('partition-2.json', 'No drops, 2 easy partitions, 20% read'))
trials.append(run_test('partition-3.json', 'No drops, 1 hard partition, 20% read'))
trials.append(run_test('partition-4.json', 'No drops, 2 hard partitions, 20% read'))

ldr = open(LEADERBOARD_OUTPUT + getpass.getuser(), 'w')

print 'Advanced tests:'
trials.append(run_test('advanced-1.json', '10% drops, 2 hard partitions and 1 leader failures, 20% read', ldr))
trials.append(run_test('advanced-2.json', '15% drops, 2 leader failures, 20% read', ldr))
trials.append(run_test('advanced-3.json', '50% drops, 1 leader failure, 20% read', ldr))
trials.append(run_test('advanced-4.json', '10% drops, 3 hard partions and 1 leader kill, 20% read', ldr))

print 'Passed', len(filter(None, trials)), 'out of', len(trials), 'tests'
