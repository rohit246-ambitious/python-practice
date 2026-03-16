# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solutions:
    def squaringSortedArr(self, arr:list):
        posiArr = []
        negiArr = []
        
        for number in arr:
            if number< 0 :
                negiArr.append(number)
            else :
                posiArr.append(number)
          
        if len(posiArr) != 0:        
            posiArr = [x*x for x in posiArr]
        if len(negiArr) != 0:     
            negiArr = [x*x for x in negiArr]
        
        posArrLen = len(posiArr)
        negArrLen = len(negiArr)
        
        if negArrLen == 0:
            return posiArr
            
        if posArrLen == 0:
            return negiArr[::-1]
        negiArr =  negiArr[::-1] 
        flagId = 0
        totalResArrLen = posArrLen + negArrLen
        left = 0
        right = 0
        resultArr = []
        while flagId < totalResArrLen:
            if left < negArrLen:
                if negiArr[left] < posiArr[right]:
                    resultArr.append(negiArr[left])
                    left+=1
                    flagId+=1
                    continue
                else:
                    resultArr.append(posiArr[right])
                    right+=1
                    flagId+=1
                    continue
            
            if right < posArrLen:
                resultArr.append(posiArr[right])
                flagId+=1
        
        return resultArr

    def squaringSortedArrTwo(self, arr:list):
        arr = [x*x for x in arr]
        n = len(arr)
        result = [0] * n 
        left = 0
        right = n-1
        pos = n - 1
        while left <= right and pos >= 0:
            if arr[left] > arr[right]:
                result[pos] = arr[left]
                left+=1
            else:
                result[pos] = arr[right]
                right-=1
            pos-=1
        
        return result
        
obj = Solutions()
arr = [-8,-6,-4,-1,0,3,10]
print(obj.squaringSortedArr(arr))
print(obj.squaringSortedArrTwo(arr))