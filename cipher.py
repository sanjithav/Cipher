"""Encodes and decodes"""
# Name 1: Sanjitha Venkata
# EID 1: sv28325


# Name 2: Swati Misra
# EID 2: SM83264


#  Input: string is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of string
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(string, key):
    """Takes in a string and key to return a single string encoded with the rail fence algorithm"""
    grid = []
    for i in range(key):
        grid.append(["-"] * len(string))


    row = 0
    movement = 1
    #traverses diagonally, fills in with letters of string
    for col in range(len(string)):
        grid[row][col] = string[0]
        string = string[1:]
        row += movement
        if row in (key - 1, 0): #if row == key-1 or row == 0
            movement *= -1


    railfenceword = ""
    #reads row by row (across) and adds letter to string if its not a -
    len_grid = len(grid)
    for row in range(len_grid):
        for i in range(len(grid[row])):
            if grid[row][i][0] != "-" or grid[row][i].isspace():
                railfenceword += grid[row][i]


    return railfenceword


#  Input: string is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of string
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(string, key):
    """Takes in a string of characters and key to return a single
    string decoded with rail fence algorithm"""
    grid=[]
    word = string
    for i in range(key):
        key1 = [""] * len(string)
        grid.append(key1)


    #traverse diagonally and add dashes as markings
    row = 0
    movement = 1
    #traverses diagonally, fills in with letters of string
    for col in range(len(string)):
        grid[row][col] = "-"
        row += movement
        if row in (key - 1, 0): # row == key-1 or row == 0
            movement *= -1


    #traverse straight through grid, and offload string in place of dashes
    for row in range(key):
        for i in range(len(word)): #len_grid
            if grid[row][i] == "-":
                grid[row][i] = string[0]
                string=string[1:]


    #read diagonally and add to output
    row1 = 0
    movement1 = 1
    output = ""
    #traverses diagonally, fills in with letters of string
    for col in range(len(word)):
        output+=grid[row1][col]
        row1 += movement1
        if row1 in (key - 1, 0): # row == key-1 or row == 0
            movement1 *= -1


    return output


    # i = []
    # j = []


    # while len(i) < len(string):
    #     for x in range(key):
    #         if len(i) < len(string):
    #             i.append(x)
    #     for y in range(key-2, -1, -1):
    #         if len(i) < len(string):
    #             i.append(y)
    #     for z in range(1, key):
    #         if len(i) < len(string):
    #             i.append(z)
    #     for y in range(key-2, -1, -1):
    #         if len(i) < len(string):
    #             i.append(y)
    #     for z in range(1, key):
    #         if len(i) < len(string):
    #             i.append(z)
    #     for zz in range(1, key-1):
    #         if len(i) < len(string):
    #             i.append(zz)


    # for a in range(len(string)):
    #     j.append(a)
    # indices=[]
    # counter = 0
    # while string:
    #     indices  = [index for (index, item) in enumerate(i) if item == counter]
    #     len_indices = len(indices)


    #     for c in range(len_indices):
    #         grid[i[counter]][indices[c]] = string[0]
    #         string=string[1:]
    #     counter+=1


    # row1 = 0
    # movement = 1
    # output=""


    # for col1 in range(len(i)):
    #     output+=grid[row1][col1]
    #     row1 += movement
    #     if row1 == key-1 or row1 == 0:
    #         movement *= -1




    # return output


#  Input: string is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(string):
    """makes string valid"""
    word = ""
    string = string.lower()


    for char in string:
        if char.isalpha():
            word += char


    return word


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p, s):
    """encodes accoording to vigenere"""
    result= chr(((ord(p)-97)+(ord(s)-97))%26+97)
    return result


#  Input: p is a character in the pass phrase and s is a character
#         in the cipher text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p, s):
    """decodes according to vigenere"""
    result = ""
    i = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
         'o','p','q','r','s','t','u','v','w','x','y','z']
    len_i=len(i)
    for j in range(len_i):
        if encode_character(s, i[j]) == p:
            result += i[j]
    return result


#  Input: string is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(string, phrase):
    """encodes with vigenere cipher"""
    phr=""


    string=filter_string(string)
    len_phrase=len(phrase)
    while len(phr) < len(string):
        for i in range(len_phrase):
            if len(phr) < len(string):
                phr += phrase[i]


    output=""
    len_phr=len(phr)
    for j in range(len_phr):
        output+=encode_character(string[j], phr[j])


    return output


#  Input: string is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(string, phrase):
    """Decodes with Vigenere algorithm"""
    string = filter_string(string)
    phr=""
    len_phrase=len(phrase)
    while len(phr) < len(string):
        for i in range(len_phrase):
            if len(phr) < len(string):
                phr += phrase[i]


    output=""
    len_phr=len(phr)
    for j in range(len_phr):
        output+=decode_character(string[j], phr[j])


    return output




def main():
    """Runs main"""
    print("Rail Fence Cipher")
    print()


    # read the plain text from stdin
    plaintext= input()
    print("Plain Text:",plaintext)


    # read the key from stdin
    key = int(input())
    print("Key:", key)


    # encode and print the encoded text using rail fence cipher
    print("Encoded Text:",rail_fence_encode(plaintext, key))
    print()


    # read encoded text from stdin
    encoded_text = input()
    print("Encoded Text:",encoded_text)


    # read the key from stdin
    key2 = int(input())
    print("Enter Key:",key2)


    # decode and print the plain text using rail fence cipher
    print("Decoded Text:",rail_fence_decode(encoded_text, key2))
    print()


    print("Vigenere Cipher")
    print()
    # read the plain text from stdin
    plaintext1= input()
    print("Plain Text:", plaintext1)
    # read the pass phrase from stdin
    pass_phrase= input()
    print("Pass Phrase:", pass_phrase)
    # encode and print the encoded text using Vigenere cipher
    print("Encoded Text:",vigenere_encode(plaintext1, pass_phrase))
    print()
    # read the encoded text from stdin
    encoded_text1 = input()
    print("Encoded Text:", encoded_text1)
    # read the pass phrase from stdin
    pass_phrase1= input()
    print("Pass Phrase:" , pass_phrase1)
    # decode and print the plain text using Vigenere cipher
    print("Decoded Text:",vigenere_decode(encoded_text1, pass_phrase1))




# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
