# File: TDD test

def make_snippet(string):
    if len(string.split()) > 5:
        return ' '.join(string.replace(",", "").split()[:5]) + "..."
    else:
        return string.replace(",", "")

