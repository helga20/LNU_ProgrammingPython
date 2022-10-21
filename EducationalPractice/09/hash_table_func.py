class HashTable:
    def __init__(self):
            self.size = 10
            self.data = [None] * self.size
		
    def getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
		
    def addKV(self, key, value):
        key_hash = self.getHash(key)
        key_value = [key, value]		
        if self.data[key_hash] is None:
            self.data[key_hash] = list([key_value])
            return True
        else:
            for pair in self.data[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.data[key_hash].append(key_value)
            return True
			
    def getKey(self, key):
        key_hash = self.getHash(key)
        if self.data[key_hash] is not None:
            for pair in self.data[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
			
    def deleteKey(self, key):
        key_hash = self.getHash(key)	
        if self.data[key_hash] is None:
            return False
        for i in range (0, len(self.data[key_hash])):
            if self.data[key_hash][i][0] == key:
                self.data[key_hash].pop(i)
                return True
        return False
			
    def printTable(self):
        print('Телефонний довідник:')
        for item in self.data:
            if item is not None:
                print(str(item))
