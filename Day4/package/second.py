def frequency(st,ch):
    return st.count(ch)

#frequency('ruthu','u')
def is_palindrome(st):
    if len(st)==1:
        return -1
    else:
        if st==st[::-1]:
            return True
        else:
            return False
#is_palindrom(12)

def reverse(it):
    return reversed(it)
