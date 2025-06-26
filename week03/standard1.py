# Problem 2
# def reverse_comments_queue(comments):
#     comms = []
#     for i in range(len(comments)):
#         comms.append(comments.pop())
#     return comms

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
#U
 #I: list of words, can be multiple
 #O: reversed string
 #C: Empty = return 
 #E: 
#P: iterate through the list and append it in stack then pop it and append again

#I:
# Problem 3
# def is_symmetrical_title(title):
#     title1 = "".join(title.lower().split())
#     left = 0
#     right = len(title1)-1
#     while left < right:
#         if not title1[left].isalnum():
#             left+=1
#         if not title1[right].isalnum():
#             right-=1 
#         if title1[left] != title1[right]:
#             return False
            
#         else:
#             left += 1
#             right -= 1
#     return True
# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 
#U
 #I: list of string can have capital letters
 #O: true or false if the string is symmetrical 
 #C: use two pointer method, 
 #E: ignore space and capital letters
#P: turn all letters to lower case and remove spaces, then check if both sides are same using two pointers

#I:
#Problem 4:
# def engagement_boost(engagements):
#     squared_engagements = []
    
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i]
#         # Appends original indexes with squares
#         squared_engagements.append((squared_engagement, i))
#     # Sorts it
#     squared_engagements.sort(reverse=True)
#     # Creating empty lists
#     result = [0] * len(engagements)
#     position = len(engagements) - 1
#     # Appends to the result
#     for square, original_index in squared_engagements:
#         result[position] = square
#         position -= 1
   
#     return result
def engagement_boost(engagements):
    left = 0
    right = len(engagements)-1
    while left <= right:
        engagements[left] = engagements[left]*engagements[left]
        engagements[right] = engagements[right]*engagements[right]
        left += 1
        right -= 1
    return sorted(engagements)
        
print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
#U
 #I: 
 #O:
 #C:  
 #E: 
#P: 

#I:
