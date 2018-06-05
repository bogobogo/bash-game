def removeNewLine(s):
    if s.endswith("\n"):
        return s[:-1]
    return s