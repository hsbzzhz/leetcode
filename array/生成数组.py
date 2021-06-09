class Search(object):
    def creat_array(self, index, base: list):
        #  1, 3, 5, 7, 9, 15, 21, 27, | 45, 63
        """
        [[3, 9, 27, ]
        [5, 15, 45, ]
        [7, 21, 63 ...]]
        """
        if index == 1:
            return 1
        # using Two - dimensional array to store the result
        matrix = [[each] for each in base]
        # the length of loop, each time will append one num at end the sub-array, and it starts with 3 not 1, so minus 1
        k = (index - 1) // len(matrix)
        while k > 0:
            for i in range(len(matrix)):
                matrix[i].append(matrix[i][-1] * 3)
                # will consist as below
                # matrix[0].append(matrix[0][-1]*3)
                # matrix[1].append(matrix[1][-1]*3)
                # matrix[2].append(matrix[2][-1]*3)
            k -= 1

        # to identify the result without using travel
        col = (index - 1) // len(matrix)
        row = (index - 1) % len(matrix) - 1
        return matrix[row][col]


res = Search().creat_array(5, base=[3, 5, 7])
print(res)
