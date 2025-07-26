from z3 import *

def evaluate_constraints(banks):
    results = []

    for bank in banks:
        s = Solver()
        L = Real('L')
        O = Real('O')
        s.add(L == bank['L'])
        s.add(O == bank['O'])
        s.add(L >= 0.25 * O)
        status = s.check()
        results.append((bank['id'], str(status)))
    
    return results

