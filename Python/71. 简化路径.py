class Solution:
    def simplifyPath(self, path: str) -> str:
        r = []
        for s in path.split('/'):
            r = {'':r, '.':r, '..':r[:-1]}.get(s, r + [s])
        return '/' + '/'.join(r)

class Solution2:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for item in path:
            if item == "..":
                if stack : stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)
