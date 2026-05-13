class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        container = {}
        for x in strs:
            ana = str(sorted(Counter(x).items()))
            # print("ana", ana)
            if ana in container:
                # print("container", container[ana])
                container[ana].append(x)
            else:
                container[ana] = [x]
        answer = []
        print(container)
        for x in container:
            print(container[x])
            answer.append(container[x])
        return answer