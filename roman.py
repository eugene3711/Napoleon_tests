test = ['MMXX','III','IV','IX', 'XI','MMMCMXCIX']

class Solution:
    def __init__(self):
        self.name = "Solution"

    def romanToInt(self, s: str) -> int:
        
        translate = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        numbersList = []

        for figure in s:
            numbersList.append(translate[figure])    

        i, arr_len = 0, len(numbersList)

        while (i < (arr_len - 1)):       
            if (numbersList[i] < numbersList[i+1]):
                numbersList[i+1] = numbersList[i+1] - numbersList[i]
                numbersList.pop(i)
                arr_len -= 1
            i += 1        

        return sum(numbersList)

sol = Solution()

for one in test:    

    print(f'{one} is {sol.romanToInt(one)}')