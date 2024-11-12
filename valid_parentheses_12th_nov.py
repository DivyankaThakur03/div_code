class Solution:
    def isValid(self, s: str) -> bool:
        dict_map = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        stack = []
        for i in s:
            if i in dict_map:
                stack.append(i)
                # print(i)
            elif i in dict_map.values():
                if not stack:
                    return False
                elif dict_map[stack[-1]] != i:
                    return False
                stack.pop()

        return not stack