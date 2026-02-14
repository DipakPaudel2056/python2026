# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# # When studying DNA, it is useful to identify repeated sequences within the DNA.

# # Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

# # Example 1:

# # Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# # Output: ["AAAAACCCCC","CCCCCAAAAA"]
# # Example 2:

# # Input: s = "AAAAAAAAAAAAA"
# # Output: ["AAAAAAAAAA"]


def repeatedDNA(s):
    # create a dictionary
    # iterate for that sliding window and check if it is in the dictionary
    # if it is there increase the count if it is not there add that to dictionary
    left_index = 0
    res = []
    n = len(s)
    count = {}
    for right in range(9,n):
        curr = s[left_index:right+1]
        if curr not in count:
            count[curr] = 1
        else:
            if count[curr] == 1:
                res.append(curr[:]) #add the shallow copy of the current in the dictionary
                count[curr] += 1
        left_index += 1
    return res

s="AABBCCDD"
print(s[:])
print(repeatedDNA("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    