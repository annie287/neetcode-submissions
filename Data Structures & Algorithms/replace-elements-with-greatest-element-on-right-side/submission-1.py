class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        output = [0]*length
        right_max = arr[length-1]
        output[length-1] = -1

        for i in range(length - 1, 0, -1):
            right_max = max(right_max,arr[i])
            output[i-1] = right_max
        return output