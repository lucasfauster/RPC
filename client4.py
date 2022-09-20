import rpyc
import sys
import random
 
if len(sys.argv) < 3:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
n = int(sys.argv[2])
conn = rpyc.connect(server,8000)
 
vector = [random.randint(0, n-1) for i in range(n)]
print("sum:  " + str(conn.root.sum_vector(vector)))

