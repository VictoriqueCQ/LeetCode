class Solution:
    def groupAnagrams(self,strs):
        temp_dict={}
        for temp_str in strs:
            sort_str = self.HashMapFunc(temp_str)
            if sort_str in temp_dict:
                temp_dict[sort_str].append(temp_str)
            else:
                temp_dict[sort_str]=[temp_str]
        return list(temp_dict.values())


    def HashMapFunc(self, temp_str):
        return ''.join(sorted(list(temp_str)))
class Solution2:
    def groupAnagrams(self,strs):
        temp_dict={}
        for temp_str in strs:
            sort_str = self.HashMapFunc(temp_str)
            if sort_str in temp_dict:
                temp_dict[sort_str].append(temp_str)
            else:
                temp_dict[sort_str]=[temp_str]
        return list(temp_dict.values())

    def HashMapFunc(self, temp_str):
        key = [0] * 26
        for char in temp_str:
            key[ord(char) - ord('a')] += 1
        return ''.join([str(i) for i in key])