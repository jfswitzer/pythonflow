import pythonflow as pf
from pythonflow.ib_util import autogen

def ib_server(graph, inputs):
    """ Takes as input an execution graph and the high-level inputs to the graph, performs the specified computation, returns the result """
    #Evaluate the graph
    print("Evaluating graph")
    print(graph("end"))

#~~~ Test code ~~~#    

def example_client():
    with pf.Graph() as graph:
        a = pf.constant(2)
        b = pf.constant(4)
        c = b - a
        d = pf.constant(4)
        e = d - c
        e.name = "end"
        ib_server(graph, {})

def main():
    # autogenerate a bunch of problems
    autogen(1000)
    example_client()
    
if __name__ == "__main__":
    main()
   
