import rpyc
from rpyc.utils.server import ThreadedServer
 
 
class MyService(rpyc.Service):
   def on_connect(self, conn):
       # código que é executado quando uma conexão é iniciada, caso seja necessário
       pass
  
   def on_disconnect(self, conn):
       # código que é executado quando uma conexão é finalizada, caso seja necessário
       pass
 
   @staticmethod
   def exposed_sum_vector(vector):
       return sum(vector)
  
#Para iniciar o servidor
if __name__ == "__main__":
   t = ThreadedServer(MyService, port=8000)
   t.start()

