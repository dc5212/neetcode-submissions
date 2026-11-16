class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        top,bots=0,rows-1
        while top<=bots:
            row=(top+bots)//2
            if target>matrix[row][-1]:
                top+=1
            elif target<matrix[row][0]:
                bots-=1
            else:
                break
        if not (top<=bots):
            return False
        row=(top+bots)//2
        l=0
        r=cols-1
        while l<=r:
                mid=(l+r)//2
                if target>matrix[row][mid]:
                    l=mid+1
                elif target<matrix[row][mid]:
                    r=mid-1
                else:
                    return True
        return False
        