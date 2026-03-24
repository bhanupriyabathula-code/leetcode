from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))  # (current_word, steps)
        
        while queue:
            word, steps = queue.popleft()
            
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + ch + word[i+1:]
                    
                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove(newWord)  # mark visited
        
        return 0
