# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(pairs, s, m, e):
            merged = []
            # initialise the two pointers
            i, j = s, m + 1

            while i <= m and j <= e:
                if pairs[i].key <= pairs[j].key:
                    merged.append(pairs[i])
                    i += 1
                else:
                    merged.append(pairs[j])
                    j += 1
            
            if i > m:
                while j <= e:
                    merged.append(pairs[j])
                    j += 1
            else:
                while i <= m:
                    merged.append(pairs[i])
                    i += 1

            for i in range(s, e + 1):
                pairs[i] = merged[i - s]

        def merge_sort(pairs: List[Pair], s: int, e: int):
            if e - s + 1 <= 1:
                return pairs
            
            m = (s + e) // 2
            merge_sort(pairs, s, m)
            merge_sort(pairs, m + 1, e)

            merge(pairs, s, m, e)

            return pairs
        
        return merge_sort(pairs, 0, len(pairs) - 1)
        