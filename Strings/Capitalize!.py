def solve(s):
    if '3g' in s.split():
        return f"{' '.join(s.split()[:4]).title()} {s.split()[-1]}"
    else:
        return s.title()
