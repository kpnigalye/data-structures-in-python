## This class does not handle collisions.

class HashTable:
    def __init__(self):
        self.SIZE = 10
        self.arr = [None for i in range(self.SIZE)]
    
    # hash function 
    # finds sum of ascii values of all characters in the key
    # return MOD of the sum to get index of the array where the value will be stored
    def get_hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)    # ord returns ascii value of the char
        return sum % self.SIZE
        
    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.arr[index] = value
    
    def __delitem__(self, key):
        index = self.get_hash(key)
        self.arr[index] = None
    
    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.arr[index]
        
# main
if __name__ == '__main__':
    data = HashTable()
    data['Dominiq'] = 30
    data['Roman'] =40
    data['HBK'] = 55

    print('Age of HBK is ', data['HBK'])
    
    del data['HBK']
    
    print('Age of HBK is ', data['HBK'])
