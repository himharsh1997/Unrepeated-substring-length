# Print Your code here
class Solution:
    def __init__(self):
        self.crossedChrDict = {}
        self.maxLengthStr = 0
        self.index = 0
        self.currentStrLength = 0

    def lengthOfLongestSubstring(self, s):
        while self.index != len(s):
            self.chrRepeatCheck(s)
            self.chrNonRepeatCheck(s)
            self.index = self.index + 1
        self.setMaxLengthStr(self.currentStrLength)
        return self.maxLengthStr

    def chrRepeatHandler(self, s):
        if(self.crossedChrDict.get(s[self.index]) != None):
            self.setMaxLengthStr(self.currentStrLength)
            self.index = self.crossedChrDict.get(s[self.index]) + 1
            self.crossedChrDict = {}
            self.currentStrLength = 0

    def chrNonRepeatHandler(self, s):
        if(self.crossedChrDict.get(s[self.index]) == None):
            self.crossedChrDict[s[self.index]] = self.index
            self.currentStrLength = self.currentStrLength + 1

    def setMaxLengthStr(self, currentStrLength):
        if(self.maxLengthStr < self.currentStrLength):
            self.maxLengthStr = self.currentStrLength


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
