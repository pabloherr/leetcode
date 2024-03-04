
def isNStraightHand(hand: list[int], groupSize: int):
        hand = sorted(hand)
        print(hand)
        while len(hand) != 0:
            a = 0
            b = 0
            l = []
            if len(hand) < groupSize:
                return False
            while a != groupSize:
                print(b)
                if hand[b] in l:
                    b +=1

                l.append(hand[b])
                del hand[b]
                print(l)
                print(hand)
                a +=1
            
            for i in range(len(l)-1):
                if l[i]!=l[i+1]-1:
                    return False


            if len(l)!=groupSize:
                return False
        return True
print(isNStraightHand([1,1,2,2,3,3],2))