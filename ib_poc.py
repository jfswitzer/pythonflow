import pythonflow as pf
import random as rand

#~~~ Helpers ~~~#
def nrand():
    return rand.randint(0, 5000)

#~~~ IB implementation ~~~#

#map a 3 digit int representing the op to the result
SAVED_RESULTS = {}

def autogen():
    n = rand.randint(0, 9)
    m = rand.randint(0, 9)
    op = rand.randint(0, 3)
    #filter out divide by zeroes
    if ((op == 3) & (m == 0)):
        return autogen()
    return 100*n + 10*op + m


def ib_server(graph, inputs):
    """ Takes as input an execution graph and the high-level inputs to the graph, performs the specified computation, returns the result """
    print(graph)

#~~~ Test code ~~~#    

def example_client():
    with pf.Graph() as graph:
        #a = pf.placeholder(name='x')
        #b = pf.placeholder(name='y')
        a = pf.constant(2)
        b = pf.constant(4)
        c = a + b
        c.name = "addition_"+str(nrand())
        #print(graph.operations)
        for op in graph.operations:
            print(op)
        ib_server(graph, {})

def main():
    example_client()
    
if __name__ == "__main__":
    main()
   
