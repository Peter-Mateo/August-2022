# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def iterate(list):
    reverbed = ""
    for i in reversed(range(len(list))):
        reverbed += str(list[i])
    return int(reverbed)

def breaks(string):
    one = string[:1] 
    two = string[1::3]
    three = string[2::]
    return [int(three), int(two), int(one)]
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        list_1 = iterate(l1)
        list_2 = iterate(l2)
        combo = str(list_1 + list_2)
        return breaks(combo)

new = Solution()
print(new.addTwoNumbers([2,4,3], [5,6,4]))
