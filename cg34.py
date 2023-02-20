l = [':slight_smile:', ':disappointed:', ':loud_laugh:', ':open_mouth:' , ':stuck_out_tongue:']
m = [':)',':(','XD',':o',':p']
s = input()
for i in range(len(l)):
    s = s.replace(l[i], m[i])

print(s)