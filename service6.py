import rpyc
import time
from rpyc.utils.server import ThreadedServer
 
class MyService(rpyc.Service):
   def on_connect(self, conn):
       # código que é executado quando uma conexão é iniciada, caso seja necessário
       pass
  
   def on_disconnect(self, conn):
       # código que é executado quando uma conexão é finalizada, caso seja necessário
       pass
 
   def exposed_get_sum(self, vector):
        start = time.time()
        total = sum(vector)
        end = time.time()
        print(end - start)
        return total
  
#Para iniciar o servidor
if __name__ == "__main__":
   t = ThreadedServer(MyService, port=18861, protocol_config = {"sync_request_timeout" : None})
   t.start()
   
