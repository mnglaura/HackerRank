s1 = "zzzzz"
s2 = "zzzzzzz"
k =4

def appendAndDelete(s, t, k):
    counter = 0

    if len(s) == len(t) and k == 0:
            return "Yes,here"

    else:
        len1 = len(s)
        len2 = len(t)

        for i in range(len1):
            j = i
            if j < len2:
                if s[i] == t[j]:
                    counter +=1
                else:
                    break
        print(counter) 
        if len1 < len2 and counter == len1:
            needed_op = len2 - counter
            if counter < len2-1:
                if s2[counter+1] == s2[counter] and k >= needed_op:
                    return "Yes"
                else:
                    return"No"
            if k == needed_op or k % 2 == 1:
                return "Yes, this"
            else:
                return "No"

        needed_op = (len1+len2)-2*counter

        if k >= needed_op:
            return "Yes"
        else:
            return "No"

print(appendAndDelete(s1, s2, k))