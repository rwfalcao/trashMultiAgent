from osbrain import run_agent
from osbrain import run_nameserver


def reply(agent, message):
    return 'agent '+ str(agent.name) +' Received ' + str(message)

class binAgent():
    def __init__(alias):
        this.agent = run_agent(alias)
        this.weight = 50

class mainStationAgent():
    pass

if __name__ == '__main__':

    ns = run_nameserver()
    alice = run_agent('Alice')
    bob = run_agent('Bob')

    addr = alice.bind('REP', alias='main', handler=reply)
    bob.connect(addr, alias='main')

    for i in range(10):
        test = dict()
        test['pos'+str(i)] = i 
        bob.send('main', test)
        reply = bob.recv('main')
        print(reply)

    ns.shutdown()
