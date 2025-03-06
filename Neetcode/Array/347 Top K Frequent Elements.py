class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        sorted_freq = sorted(freq.items(),key = lambda x : x[1],reverse=True)

        output = []

        count = 0

        for num in sorted_freq:
            if(count<k):
                output.append(num[0])
                count+=1
            else:
                break

        return output 
            
