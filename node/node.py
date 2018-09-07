import datetime


class DCNode:
    """This class represents the DockerCoin Node"""
    _node_address = ''
    address_list = []

    def __init__(self, address):
        self._node_address = address
        self.add_address(address)

    def add_address(self, address):
        if True:
            self.address_list.append({ 'addr': address, 'timestamp': str(datetime.datetime.now())})

    def ping_address(self, address):
        return True
    