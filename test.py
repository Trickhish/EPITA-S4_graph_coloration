import testcolor
import login_coloration

fl = dir(login_coloration)
fl = [(e, getattr(login_coloration, e)) for e in fl if e[0]!="_" and callable(getattr(login_coloration, e))]

tests_number = 20
compact = True

for (fn, f) in fl:
    if not compact:
        print("")
    print(f"Testing {fn} ({tests_number}avg.) : ", end=("" if compact else "\n"))
    dtl=[]
    for i in range(tests_number):
        (dt, mdn, r)=testcolor.run_verif_coloration(f, "files")
        dtl.append(dt)
        #print(f"    {dt}")
    dt = sum(dtl)/len(dtl)
    dr = [e[0] for e in r]

    if compact:
        print(f"{round(dt, 3)}μs")
    
    print(f"    {dr}")

    sc=len(r)
    for e in r:
        if e[1]!="":
            sc-=1
    sc=round(sc/len(r)*100)
    if sc==100:
        if not compact:
            print("    100%")
    else:
        print("    "+str(sc)+"%"+('cf'.join( [str(e) for e in r] )))
    if not compact:
        print(f"    {fn} Took {dt}μs in average")

print("")
