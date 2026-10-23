import pymupdf, sys, os
src=r"C:\Users\varun\OneDrive\Desktop\Learning M Varun\2. Product Maangment\Imp PM documents\Final Doc including all"
out=r"C:\Users\varun\Documents\ClaudeProjects\Product-Management-Master-Handbook\_source"
for f in os.listdir(src):
    if f.endswith(".pdf"):
        d=pymupdf.open(os.path.join(src,f))
        imgs=sum(len(p.get_images()) for p in d)
        print(f, "pages",len(d),"images",imgs, "toc",len(d.get_toc()))
        with open(os.path.join(out,f[:-4]+".txt"),"w",encoding="utf-8") as o:
            for i,p in enumerate(d,1):
                o.write(f"\n=== PAGE {i} ===\n"+p.get_text())
        with open(os.path.join(out,f[:-4]+".toc.txt"),"w",encoding="utf-8") as o:
            for t in d.get_toc(): o.write(repr(t)+"\n")
