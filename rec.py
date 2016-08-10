def b():
    return '''%s\n\ndef a():
    return r\"""%s\"""\nprint b()'''%(a(),a())


def a():
    return r"""def b():
    return '''%s\n\ndef a():
    return r\"""%s\"""\nprint b()'''%(a(),a())
"""
print b()
