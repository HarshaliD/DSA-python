#Solution 1

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = {}

        for word in strs:
            sortedWord = tuple(sorted(word))

            if sortedWord in dict1:
                dict1[sortedWord].append(word)
            else:
                dict1[sortedWord] = [word]

        output = []

        for key,val in dict1.items():
            output.append(val)

        return output



#Solution 2

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = {}

        for word in strs:
            sortedWord = tuple(sorted(word))

            if sortedWord in dict1:
                dict1[sortedWord].append(word)
            else:
                dict1[sortedWord] = [word]

        output = []

        return list(dict1.values())

