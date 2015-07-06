# plus.py (by Wesley Chun under CC-SA3.0 license)
import sys
import math

if len(sys.argv) < 3:
    sys.exit('Usage: %s nodeid m '% sys.argv[0])

nid = int(sys.argv[1])
m = int(sys.argv[2])

for i  in range(m):
    print "45+2^",i,"=>",nid+2**i,"=>",(nid+2**i) % 2**m 

