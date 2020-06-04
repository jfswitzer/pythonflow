import pythonflow as pf
import random

def rand():
    return pf.constant(random.randint(0, 20))
def build():
    with pf.Graph() as graph:
        a = rand()
        b = rand()
        c = rand()
        d = rand()

        mode = rand()

        if (mode == 0):
            e0 = a + b
            e1 = b - a
            e2 = a + d
            e3 = e1 + c
            e3.name = "end"

        elif (mode == 1):
            e0 = a - b
            e1 = c + b
            e2 = d + d
            e3 = e1 + e2
            e4 = e3 + c
            e4.name = "end"

        elif (mode == 2):
            e0 = d - b
            e1 = d + a
            e2 = b + c
            e3 = e1 - e2
            e4 = e3 + a
            e4.name = "end"            
        graph("end")
def test_no_autogen():
    pf.clear_saved()    
    for _ in range(0, 10):
        build()

def test_autogen_100():
    global SAVED_VALUES
    pf.clear_saved()
    pf.autogen(100)
    pf.clear_testvals()
    for _ in range(0, 10):
        build()

def test_autogen_1000():
    pf.clear_saved()    
    pf.autogen(1000)
    pf.clear_testvals() 
    for _ in range(0, 10):
        build()

def test_autogen_10k():
    pf.clear_saved()    
    pf.autogen(10000)
    pf.clear_testvals()   
    for _ in range(0, 10):
        build()

def test_autogen_100k():
    pf.clear_saved()    
    pf.autogen(100000)
    pf.clear_testvals()    
    for _ in range(0, 10):
        build()

def test_autogen_1mil():
    pf.clear_saved()    
    pf.autogen(1000000)
    pf.clear_testvals()    
    for _ in range(0, 10):
        build()    

def main():
    pf.clear_saved()
    print(" ~~~~~~~~ TEST NO PF.AUTOGEN ~~~~~~~~ ")
    test_no_autogen()
    print("RESULT NO PF.AUTOGEN: "+pf.from_cache()+" FROM IB CACHE, "+pf.from_compute()+" COMPUTED DIRECTLY")
    
    print(" ~~~~~~~~ TEST PF.AUTOGEN 100 ~~~~~~~ ")    
    test_autogen_100()
    print("RESULT PF.AUTOGEN 100: "+pf.from_cache()+" FROM IB CACHE, "+pf.from_compute()+" COMPUTED DIRECTLY")
    
    print(" ~~~~~~~~ TEST PF.AUTOGEN 1000 ~~~~~~ ")    
    test_autogen_1000()
    print("RESULT PF.AUTOGEN 1000: "+pf.from_cache()+" FROM IB CACHE, "+pf.from_compute()+" COMPUTED DIRECTLY")
    
    print(" ~~~~~~~~ TEST PF.AUTOGEN 10k ~~~~~~~ ")    
    test_autogen_10k()
    print("RESULT PF.AUTOGEN 1OK: "+pf.from_cache()+" FROM IB CACHE, "+pf.from_compute()+" COMPUTED DIRECTLY")
    
    print(" ~~~~~~~~ TEST PF.AUTOGEN 100K ~~~~~~ ")    
    test_autogen_100k()
    print("RESULT PF.AUTOGEN 100K: "+pf.from_cache()+" FROM IB CACHE, "+pf.from_compute()+" COMPUTED DIRECTLY")
    
    print(" ~~~~~~~~ TEST PF.AUTOGEN 1MIL ~~~~~~ ")    
    test_autogen_1mil()
    print("RESULT PF.AUTOGEN 1MIL: "+pf.from_cache()+" FROM IB CACHE, "+pf.from_compute()+" COMPUTED DIRECTLY")     

if __name__ == "__main__":
    main()
   
