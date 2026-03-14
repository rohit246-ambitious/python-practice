class Solutions:
    def firstSolution(self, arr:list):
        left = 0
        right = left +1
        lenArr = len(arr)
        while right < len(arr):
            if arr[left] != arr[right]:
                left +=1
                right +=1
            elif arr[left] == arr[right]:
                arr.pop(right)
        return arr
        
    def secondSolution(self, arr: list):
        if not arr:
            return arr

        left = 0                          # left = last unique position

        for right in range(1, len(arr)):
            if arr[right] != arr[left]:   # found new unique element
                left += 1
                arr[left] = arr[right]    # overwrite duplicate position

        return arr[:left + 1]     
    

obj = Solutions()
arr = [0, 0, 1, 1,2,3,3,4,5,5]
print(obj.firstSolution(arr))
print(obj.secondSolution(arr))