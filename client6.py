import rpyc
import sys
import random
import time
 
if len(sys.argv) < 3:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
n = int(sys.argv[2])
conn = rpyc.connect(server, 18861)
start = time.time()
 
vector = [random.randint(0, n-1) for i in range(n)]
soma = conn.root.get_sum(vector)
print("sum:  " + str(soma))


end = time.time()
print(end-start)