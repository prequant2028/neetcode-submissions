class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        frq=[0]*2
        for i in range(len(students)):
            frq[students[i]]+=1
        for sandwich in sandwiches:
            if frq[sandwich]>0:
                frq[sandwich]-=1
            else:
                break
        return frq[0]+frq[1]