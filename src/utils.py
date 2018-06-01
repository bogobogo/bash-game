def removeNewLine(s):
    if repr(s)[-3:-1] == '\\n':
        return repr(s)[1:-3]
    return str(s)





