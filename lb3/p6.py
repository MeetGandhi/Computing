tscore=input("input testscore out of 50=")
lscore=input("input labscore out of 50=")
if tscore>50 or lscore>50:
    print "incorrect marks"
else:
    toscore=tscore+lscore
    if toscore>=90:
        if lscore>tscore:
            print "grade=A+"
        else:
            print "grade=A"
    elif toscore>=70:
        if lscore>tscore:
            print "grade=B+"
        else:
            print "grade=B"
    elif toscore>=50:
        if lscore>tscore:
            print "grade=C+"
        else:
            print "grade=C"
    else:
        if lscore>tscore:
            print "grade=D+"
        else:
            print "grade=D"
