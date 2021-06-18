class Codec:
    def compress(dself,data):
        s = ""
        i = 0
        n = len(data)
        while i<n:
            count = 1
            while i<N-1 and data[i]==data[i+1]:
                count += 1
                i += 1 
            if count ==1:
                s += str(data[i])
            else:
                s += str(data[i]) + '{' + str(count) + '}'
            i += 1 
        return s

    def decompress(self,data):
        z = ""
        i = 0
        while i < len(data):
            if z[i] == "{":
                z += str(z[i-1]) * (int(z[i+1])-1)
                i += 3 
            else:
                z += str(z[i])

        return z



### approach is to make the count of the chacater and append it after that character in between flower brackets 
### to decompresss we whenever we find that we multiple the character before bracket with that count in brackets



obj = Codec()


data1 = obj.compress("aaabbbccda")
print(obj.decompress(data1))

data2 = obj.compress("1223334444")
print(obj.decompress(data2))

data3 = obj.compress("##122aaaabbbbbb$$$$bbbbbbcc")
print(obj.decompress(data3))
