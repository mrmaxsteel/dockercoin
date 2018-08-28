# dockercoin

## Architecture
Dockercoin is comprised of the following components:
* Nodes
### Nodes
A node is a dockercoin peer that will actively mine dockercoins, has a personal dockercoin wallet, and holds a copy of the dockercoin blockchain.
#### Node Messages
* *getaddr* - when a node receives a getaddr message, it first figures out how many addresses it has that have a timestamp in the last 3 hours. Then it sends 3 of those addresses (randomly sampled), back to the node making the request via an *addr* message
* *addr* - a list of 3 or less node addresses (for bootstrapping)

