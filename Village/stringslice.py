def stringslice(a,b,c,d,s):
    astr = s[a:b+1]
    bstr = s[c:d+1]
    tempstr = astr + ' '
    return tempstr + bstr

a = 66
b = 71
c = 91
d = 95
st = "WJ77YP1qjFDR8TctrPDVGvJVNSwV3YgzhBFodZvwXWpt7z58igtNWDER9onlDHNT9CPareasbUba8VySGgkLrZxfWDLtolainUXkBZ6FY9ZfB8aqETZHOnd6B0auVthtJgaW79rBR7BY2mskL1mu0R2ik7NMDI4OIGzX0KGaZ4BnFqHPmf7s1uyvB2Rm5CKE6NALr"
print(stringslice(a,b,c,d,st))