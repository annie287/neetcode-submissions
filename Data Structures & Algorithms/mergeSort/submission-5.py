# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # merge sort

        def merge(pairs, s, m, e):
            # declare two pointers
            i, j = s, m + 1
            temp = []
            while i <= m and j <= e:
                if pairs[i].key <= pairs[j].key:
                    temp.append(pairs[i])
                    i += 1
                else:
                    temp.append(pairs[j])
                    j += 1
            
            while i <= m:
                temp.append(pairs[i])
                i += 1
            while j <= e:
                temp.append(pairs[j])
                j += 1
            
            for n in range(len(temp)):
                pairs[s + n] = temp[n]


        def merge_sort(pairs, s, e):
            if e - s <= 0:
                return pairs
            
            m = (s + e) // 2
            merge_sort(pairs, s, m)
            merge_sort(pairs, m + 1, e)

            merge(pairs, s, m, e)
            return pairs

        return merge_sort(pairs, 0, len(pairs) - 1)
        