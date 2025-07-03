def palindormo(s):
    s = s.replace(" ", "").lower()

    if len(s) <= 1:
        return True
    elif s(0) == s(-1):
        return palindormo(s[1:-1])
    else:
        return False
    
print (palindormo("anna"))
