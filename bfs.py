graph = { 'You':['mani','surat','vino','prakash','karup','Ram'],'mani':['Ross','seeni','periya'],'surat':['Ramana','Rohit'],'vino':['Rocky','Vallur','gowtham'],'Ram':['vignesh','Ajeeth'],'prakash':['Arun','Kabbali'],'karup':['Dinesh','Raja']}
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
#BFS
queue = Queue()
searched=[]
parents={}

queue.enqueue('You')
end = 'Ramana'


while queue.size() != 0:

      person = queue.dequeue()

      if  person not in searched :

          if person == end:
             path =Queue()
             path.enqueue(person)
             nx = parents[person]
             while nx is not None:
                 path.enqueue(nx)
                 try:
                     nx = parents[nx]
                 except:
                     nx = None
             for _ in range(path.size()-1):
                 print(path.dequeue(),end="-->")
             print(path.dequeue())    
             break
          else:
              try:
                  nx = graph[person]
                  for n in nx:
                      queue.enqueue(n)
                      parents[n] = person
                      searched.append(person)
              except:
                  pass
