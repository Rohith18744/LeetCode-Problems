class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        smallest,biggest=0,len(people)-1
        while biggest>=smallest:
            if people[biggest]+people[smallest]<=limit:
                smallest+=1
                biggest-=1
            else:
                biggest-=1
            boats+=1
        return boats