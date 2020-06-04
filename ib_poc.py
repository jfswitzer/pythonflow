import pythonflow as pf
import random as rand
from pythonflow.ib_util import autogen_problem

#~~~ Helpers ~~~#
def nrand():
    return rand.randint(0, 5000)

def ib_server(graph, inputs):
    """ Takes as input an execution graph and the high-level inputs to the graph, performs the specified computation, returns the result """
    print(graph)
    #evaluate the graph
    print("evaluating graph")
    print(graph("end"))

#~~~ Test code ~~~#    

def example_client():
    with pf.Graph() as graph:
        #a = pf.placeholder(name='x')
        #b = pf.placeholder(name='y')
        a = pf.constant(2)
        b = pf.constant(4)
        c = b - a
        d = pf.constant(4)
        e = d - c
        e.name = "end"
        #print(graph.operations)
        for op in graph.operations:
            print(op)
        ib_server(graph, {})

def main():
    example_client()

    print("testing")

    autogen_problem()
    
if __name__ == "__main__":
    main()
   
