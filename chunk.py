data = "I am a programmer"
lData = list(data)
rData = ['0'] * len(lData)
index = 0
z = []
class ToyTCPStream:
    def receive(self,chunk, data):
        global rDAta
        global z
        index = chunk - 1
        for i in range(len(data)):
            rData[chunk-1+i] = data[i]
            
        print(rData)

    def read(self, data):
      global index
      j = 0
      if rData[index]!='0':
        j = 
      for i in rData[index:]:
        if i=='0':
          return j
        else:
          j += 1
      return j


### we use a global string to get the each chunk value and append it
### whenever read is called , we print the chunk index to next '0' which defines the empyty space and return that length


obj = ToyTCPStream()

chunk = 1
bytes = ['I',' ']
obj.receive(chunk,bytes)

chunk = 3
bytes = ['a']
obj.receive(chunk,bytes)
print(obj.read([]))
print(obj.read([]))

chunk = 7
bytes = ['','p','r']
obj.receive(chunk,bytes)
print(obj.read([]))


