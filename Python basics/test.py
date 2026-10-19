# aaaabbcaa

string = "aaaabbcab"
count = 1
answer = ""
for i in range(1, len(string)):
    if string[i] == string[i - 1]:
        count += 1
    else:
        answer += string[i- 1] + str(count)
        count = 1
        
    
answer += string[-1] + str(count)    
print(answer)

