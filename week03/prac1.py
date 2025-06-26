'''
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

def reverse_comments_queue(comments):
    stack = []
    reversed_comments = []
    for comment in comments:
        stack.append(comment)
    while stack:
        reversed_comments.append(stack.pop())
    return reversed_comments

def is_symmetrical_title(title):
    title1 = "".join(title.lower().split())
    left, right = 0, len(title1)-1
    while right > left:
        if title1[left] != title1[right]:
            return False
        left += 1
        right -= 1

        return True
'''



