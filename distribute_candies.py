def distributeCandies(candies: int, num_people: int) -> list[int]:
    people = [0]*num_people
    i = 0
    j = 0
    while candies != 0:
        if j >= len(people):
            j = 0
        i +=1
        if candies <= i:
            people[j] = people[j]+candies
            return people
        else:
            people[j] = people[j]+i
        candies -=i
        j +=1
print(distributeCandies(7,4))

#def distributeCandies(self, candies: int, num_people: int) -> List[int]:
#    ans = [0] * num_people
#    k = 0
#    while candies > 0:
#        if candies >= (k+1):
#            candies -= (k+1)
#            ans[k % num_people] += k + 1
#        else:
#            ans[k % num_people] += candies
#            candies = 0
#        k += 1
#    return ans