for srcpointi in range(1):
    for dstpointi in range(1):
        filepathy="/home/stack/code/pythontest/datafortrain/datafortrain(0-18).txt"
        filepathx="/home/stack/code/pythontest/answer(0-18).txt"
        
        print(str(srcpointi)+"to"+str(dstpointi))
        lines = open(filepathx).readlines()
        fp = open(filepathx,'w')
        for s in lines:
            fp.write( s.replace(',',' '))
        fp.close()

        lines = open(filepathx).readlines()
        fp = open(filepathx,'w')
        for s in lines:
            fp.write(s.replace('[',""))
        fp.close()

        lines = open(filepathx).readlines()
        fp = open(filepathx,'w')
        for s in lines:
            fp.write(s.replace(']',""))
        fp.close()



        lines = open(filepathy).readlines()
        fp = open(filepathy,'w')
        for s in lines:
            fp.write( s.replace(',',' '))
        fp.close()

        lines = open(filepathy).readlines()
        fp = open(filepathy,'w')
        for s in lines:
            fp.write(s.replace('[',""))
        fp.close()

        lines = open(filepathy).readlines()
        fp = open(filepathy,'w')
        for s in lines:
            fp.write(s.replace(']',""))
        fp.close()


print("done!!!")
