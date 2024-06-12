class Solution:
    def decode(self, encoded, first):
        n = len(encoded) + 1
        arr = [0] * n
        arr[0] = first
        
        for i in range(1, n):
            arr[i] = encoded[i - 1] ^ arr[i - 1]
        
        return arr

