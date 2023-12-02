class Solution:

    def doExist(self, word, matris_dict):
        for key,le in enumerate(word):
            if key == 0:
                

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        matris_dict = dict()


        m = len(board) # satır sayısı 4

        n = len(board[0]) # sütun sayısı 5
                # a = i, j (0, 1)


        for i in range(m):
            for j in range(n):
                upper_num= i-1 if i-1>=0 else None
                bottom_num= i+1 if i+1<m else None

                left_num= j-1 if j-1>=0 else None
                right_num= j+1 if j+1<n else None

                # upper_num = upper_num, j
                # upper_num = bottom_num, j
                # left_num = i, left_num
                # right_num = i, right_num
                coordinates = [(upper_num, j), (bottom_num, j), (i, left_num), (i, right_num)]

                matris_dict[i, j] = {board[x][y]:(x, y) for x,y in coordinates if x!=None and y!=None}
                print(i, j, matris_dict)

        result = []
        for word in words:
            if self.doExist(self, word):
                result.append(word, matris_dict)
        return result