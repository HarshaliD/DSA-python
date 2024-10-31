# https://practice.geeksforgeeks.org/problems/search-query-auto-complete/0?category%5B%5D=Strings&category%5B%5D=Strings&problemStatus=unsolved&difficulty%5B%5D=2&page=1&query=category%5B%5DStringsproblemStatusunsolveddifficulty%5B%5D2page1category%5B%5DStr

class AutoCompleteSystem:
    def __init__(self, sentences, times):
        # Initialize search term and dictionary
        self.search = ""
        self.dict = {}
        
        for i in range(len(sentences)):
            self.dict[sentences[i]] = times[i]
        
        # Sort the dictionary items based on frequency and lexicographical order
        self.sorted_dict = sorted(self.dict.items(), key=lambda item: (-item[1], item[0]))

    def input(self, c):
        '''
        Return the top 3 suggestions when the current character in the stream is c
        c == '#' means the current query is complete and save the entire query into historical data
        '''
        output = []


        if c == '#':

            if self.search in self.dict:
                self.dict[self.search] += 1
            else:
                self.dict[self.search] = 1
            
            self.sorted_dict = sorted(self.dict.items(), key=lambda item: (-item[1], item[0]))
            
            self.search = ""
            return output
        

        self.search += c
        count = 0
        
        for sentence, freq in self.sorted_dict:
            if sentence.startswith(self.search):
                if count < 3:
                    output.append(sentence) 
                    count += 1
                else:
                    break
        
        return output
