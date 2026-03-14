# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solutions:
    def firstSolution(self, arr:list):
        left = 0
        right = left + 1
        while right < len(arr):
            if arr[right] == 0 and arr[left] == 1:
                arr[right] = 1
                arr[left] = 0
                left+=1
                right+=1
            elif arr[right] == 1 and arr[left] == 1:
                right+=1
            else:
                left+=1
                right+=1
                
        return arr

    def secondSolution(self, arr):
        left = 0
        right = len(arr) - 1
        while left < right:
            while left < right and arr[left] == 0:
                left+=1

            while left < right and arr[right] == 1:
                right -= 1

            if left < right:
                arr[left] ,arr[right] = arr[right], arr[left]
                left+=1
                right-=1

        return arr
            
        
obj = Solutions()
arr = [0, 1, 0, 0, 1]
print(obj.firstSolution(arr))
print(obj.secondSolution(arr))