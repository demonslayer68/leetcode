"""
Important thing in this problem is how to create the hashmap.
initially, I created a map for every word. But that is n**2
better is to create a map for every pattern. that is n * length of word ** 2( << n )
It is length ** 2 because string splicing also takes O(m)

Also, look at the solution for bi-drectional BFS. it significantly reduces space and time

"""

from collections import deque
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        newq = deque()
        visited = {}
        visited_pattern = {}
        length = 1
        patterns = defaultdict(list)
        L = len(wordList[0])  # since all words are of same length

        # for each word, add it to the list of patterns it is part of
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)

        # normal BFS. generate each pattern for a word, then do BFS using all words for that pattern
        while q:
            word = q.popleft()
            # print(word)
            visited[word] = 1
            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1:]
                if pattern not in visited_pattern:
                    visited_pattern[pattern] = 1
                else:
                    continue
                # print(pattern, patterns[pattern])
                for elem in patterns[pattern]:
                    if elem == endWord:
                        return length + 1
                    elif elem not in visited:
                        newq.append(elem)

            if not q:
                q = newq
                newq = deque()
                length += 1

        return 0
