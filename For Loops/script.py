class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Declaring the String
        so_far = ''
        # For loop to start 
        for letter in s:
            # Skip the first letter
            if so_far == '':
                so_far += letter
            # Check if the letter is in the string 
            if letter in so_far:
                print(so_far)
                return len(so_far)
            # Add the letter to the new 
            else:
                print(so_far)
                so_far += letter
                
                
        # Create a for loop that loops through each letter in so_far to check against the current letter 
        
        """
        :type s: str
        :rtype: int
        """
test = Solution()
test.lengthOfLongestSubstring('"abcabcbb"')