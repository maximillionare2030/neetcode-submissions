class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = []
        curr = 0
        for i, ch in enumerate(s):
            print(stack)
            if ch == "]":
                cnt, char = stack.pop()
                decoded_str = cnt * char
                
                # If stack is not empty, append to the parent bracket's string
                if stack:
                    stack[-1][1] += decoded_str
                # Otherwise, we are at the top level, append to result
                else:
                    res.append(decoded_str)

            elif ch =="[":
                stack.append([curr, ""])
                curr = 0
            
            elif ch in "0123456789":
                curr = curr * 10 + int(ch) # number
            
            else: # just a char
                if not stack:
                    res.append(ch)
                else:
                
                    stack[-1][1] += ch
        return "".join(res)


"""
3b
"""