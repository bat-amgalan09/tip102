def is_valid_post_format(posts):
    stack = []
    hashm = {"}":"{", ")":"(","]":"["}
    for char in posts:
        if char in hashm.values():
            stack.append(char)
        elif char in hashm:
            if not stack or stack[-1] != hashm[char]:
               return False
            stack.pop()
        else:
           return False
    return not stack
        
  
           


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))