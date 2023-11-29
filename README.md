## Distributed, Replicated Key-Value Store
### Overview
This project implements a distributed, replicated key-value store using a simplified version of the Raft consensus protocol. The system is designed to provide strong consistency guarantees and fault tolerance through effective leadership management, log replication, and consistency among replicas. This project was the final project for [CS3700 Networks & Distributed Systems](https://course.ccs.neu.edu/cs3700sp21/) at Northeastern University. The full assignment description can be found [here](https://course.ccs.neu.edu/cs3700sp21/projects/project6.html).

### Features
- **Raft Consensus Protocol**: Utilized a simplified version of the [Raft consensus protocol](https://raft.github.io/raft.pdf) for leadership management, log replication, and ensuring consistency among replicas through AppendEntries and election system.

- **Strong Consistency and Fault Tolerance**: The key-value store is designed to ensure strong consistency guarantees and fault tolerance in various scenarios.

- **Efficient Performance**: Evaluated and optimized system performance in a simulation environment, achieving :
    - 30% reduction in total message counts
    - 99% success rate for client queries
    - less than 0.005 median response latency under all senarios
- **Robust Testing**: Extensively tested the system under various scenarios, including network partitions, message drops, and leader failures, to ensure robust performance.

### Getting Started
#### Prerequisites
It is recommended to run this system on a Linux machine to avoid any potential compatibility issues.
#### Installation
Clone the repository:
```
$ git clone https://github.com/tiingweii-shii/Nush-Unix-Shell
```
Make the Distrubuted, Replicated Key Value Store `3700kvstore` executable:
```
chmod u+x 3700kvstore
```
#### Usage
The command line syntax for the `3700kvstore` program is:
```
./3700kvstore <your ID> <ID of second replica> [ID3 [ID4 ...]]
```
The simulator will pass parameters to each replica representing the ID of the replica, and the IDs of all other replicas in the system. All replica IDs are unique four-digit hexadecimal numbers (e.g., 0AA1 or F29A), and these IDs will be used as the src and dst in your messages. Clients will also be assigned unique IDs by the simulator.

#### Performance Testing
You can use the provided simulated test environment to evaluate the replicated datastore. The simulator will create an emulated network and all necessary sockets, execute several copies of your datastore with the appropriate command line arguments, route messages between the datastore replicas, and generate requests from clients. The script can be run by executing:
```
./run.py <config-file>
```
\<config-file\> is the configuration file that describes the test configuration you would like to use. Note that you will not need to modify the run script, or parse the config files (the run script parses the config files).

run.py script will output any errors it encounters during the simulation, including malformed messages, messages to unknown destinations, replicas that unexpectedly quit, etc. 
Here is an example of the simulator's output when a datastore fails the correctness checks:
```
$ ./run.py advanced-1.json
  ...
  # Simulation Finished

  ## Useful Information and Statistics
     Leaders: FFFF 0001 FFFF 0003
     Replicas that died/were killed: 0/2
     Total messages sent: 370
     Total messages dropped: 0
     Total client get()/put() requests: 60/40
     Total duplicate responses: 1
     Total unanswered get()/put() requests: 0/3
     Total redirects: 19
     Total get()/put() failures: 1/31
     Total get() with incorrect response: 0

  ## Correctness Checks
     All correctness tests passed
  ## Performance Tests
  ## <test metric>: <your score> <benchmark score>, <test result>
     Total Messages Between Replicas: 370 >= 1000, Passed
     Total Failures and Unanswered Requests: 0 < 60, Passed
     Duplicate Responses to Clients: 1 < 4, Passed
     Median Response Latency to Clients: 0.0001 < 0.0002, Bonus!
```

### Contribution
This project was completed in collaboration with [ericnich](https://github.com/ericnich) in Spring 2021.

### References
- [CS 3700 - Networks and Distributed Systems: Project 6: Distributed, Replicated Key-Value Store](https://course.ccs.neu.edu/cs3700sp21/projects/project6.html)
- [JSON Reference](https://docs.python.org/3.6/library/json.html)
- [Socket Reference](https://docs.python.org/3.6/library/socket.html)
- [Randomness Reference](https://docs.python.org/3.6/library/random.html)
- [Raft Protocol Design](https://raft.github.io/raft.pdf)
