def minLen(words):
    minLen = len(words[0])
    for i in range(1, len(words)):
        if len(words[i]) < minLen:
            minLen = len(words[i])
    return minLen

def longestCommonPrefix(words):
    if not words:
        return ""

    minLength = minLen(words)
    prefix = ""

    for j in range(minLength):
        letter = words[0][j]
        for i in range(1, len(words)):
            if words[i][j] != letter:
                return prefix
        prefix += letter

    return prefix  

print(longestCommonPrefix(["flower", "flow", "flight"]))  
print(longestCommonPrefix(["dog", "racecar", "car"]))   


