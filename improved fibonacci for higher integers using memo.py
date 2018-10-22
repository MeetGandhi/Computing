known={0:0,1:1}
def fibdic(n):
    if n in known:
        return known[n]
    else:
        r=fibdic(n-1)+fibdic(n-2)
        known[n]=r
        return r
