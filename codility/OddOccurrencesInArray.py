
def solution(A):
   if len(A) == 1:
       return A[0]

   elif len(A) == 3:
       if A[0] == A[2]:
           return A[1]
       else:
           return A[2]
   else:
       while A:
           pair1, pair2 = A.pop(0), A.pop(1)
           if pair1 == pair2:
               continue
           else:
               return pair2

print(solution([9, 3, 9, 3, 9, 7, 9]))
#print(solution([1,2,1]))
#print(solution([1,2,3]))
