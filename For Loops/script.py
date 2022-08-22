class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Declaring the String
        so_far = ''
        # For loop to start 
        for letter in s:
            # Check if the letter is in the string 
            if letter in so_far:
                finish = len(so_far)
                so_far = ''
            # Add the letter to the new 
            else:
                so_far += letter
        print(finish)
        return finish
                
        # Create a for loop that loops through each letter in so_far to check against the current letter 
        
        """
        :type s: str
        :rtype: int
        """
test = Solution()
test.lengthOfLongestSubstring('abcabcbb')