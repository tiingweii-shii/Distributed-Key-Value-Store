## Approach
We generally followed the given outline in terms of order.
Other functionality was filled in between and in parallel with these.
1. Create a general structure for the program.
2. Implement basic message handling.
3. Set up a basic version of the election system.
4. Hack together a basic version of AppendEntries.

## Challenges
We had issues with git merges due to our layouts diverging.

## Testing
We ran tests on a Khoury system as changes were made. 
Our environments don't have the socket tech, so we couldn't test locally.

## Sources
- https://docs.python.org/3.6/library/json.html - json reference
- https://docs.python.org/3.6/library/socket.html - socket reference
- https://docs.python.org/3.6/library/stdtypes.html#typesmapping - dictionary reference
- https://docs.python.org/3.6/library/random.html - randomness reference
- https://raft.github.io/raft.pdf - protocol design
- https://stackoverflow.com/questions/21831046/pycharm-indentation-spaces - indentation issue
- https://stackoverflow.com/questions/35407770/ - git issue
- piazza #332, #610, #634 - assignment clarification