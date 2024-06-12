chars =   ["a","a","b","c","c","c","d","d"] 

# METHOD 1 (Set Lists and using counts)
# Initialize the unique, number and compressed lists
unique = []     # Stores all the unqiue letters
number = []     # Stores the count for each unique letter
compressed = []     # Stores the compressed format for the chars

# Appends unqiue letters to unique list in a ordered position
for i in range(len(chars)):
    if (chars[i] not in unique):
        unique.append(chars[i])

# Gets and append the count for each letter. Note: The value of the index in number list corresponds with the index of the unqiue list
for i in unique:
    number.append(chars.count(i))
    
# Append the unique letter and count (if count > 1) in ordered format
for char, num in zip (unique, number):
    compressed.append(char)
    if num > 1:
        compressed.append(num)
    else:
        continue

print(compressed)


# # METHOD 2 (Brute Force)
# # Initialize empty string and count
# s = []
# count = 0

# for i in range(len(chars)):
#     if chars[i] not in s:       # Checks if the letter is in list 's'
#         if not s:       # Checks if it is the first letter
#             s.append(chars[i])
#         else:
#             if count > 1:       # Checks if the count is 1 (display if count > 1) (do not display if count == 1)
#                 s.append(count)     # Appends the count before adding the letter
#         count = 0       # Reset the count when at the begining of the next letter
#         if chars[i] not in s:       # Prevent double append for first letter
#             s.append(chars[i])
        
#     count += 1      # Increment the count
#     if (i + 1) == len(chars):       # Checks the last letter count to decide to append or not
#         if count == 1:
#                 continue
#         else:
#             s.append(count)
    
# print(s)

