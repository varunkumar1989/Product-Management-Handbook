import re,difflib
b=r"C:\Users\varun\Documents\ClaudeProjects\Product-Management-Master-Handbook\_source"
def words(f):
    t=open(f"{b}\\{f}.txt",encoding="utf-8").read()
    t=re.sub(r"=== PAGE \d+ ===|Page \d+|Companion page \d+|Extra topics page \d+","",t)
    return re.sub(r"\s+"," ",t).split(" ")
e=words("Expanded_PM_AI_and_Tools_Study_Guide"); v=words("Complete_Visual_PM_AI_and_Tools_Study_Guide")
print(len(e),len(v))
sm=difflib.SequenceMatcher(None,v,e,autojunk=False)
ins=dele=0
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag!="equal":
        if tag in("insert","replace"): ins+=j2-j1
        if tag in("delete","replace"): dele+=i2-i1
print("words only in Expanded:",ins,"| words only in Visual:",dele)
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag in("delete","replace") and i2-i1>8: print("VISUAL-ONLY:"," ".join(v[i1:i2])[:300])
