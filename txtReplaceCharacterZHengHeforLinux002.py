
def txtreplacechar(src1,src2,srcstep,dst1,dst2,dststep):
    for i in range(src1,src2+1,srcstep):
        for j in range(dst1,dst2+1,dststep):

            filepath1="/home/stack/code/pythontest/answer("+str(i)+"-"+str(j)+").txt"
            filepath2="/home/stack/code/pythontest/datafortrain/datafortrain(" + str(i) + "-" + str(j) + ").txt"


            lines = open(filepath1).readlines()
            fp = open(filepath1,'w')
            for s in lines:
                #print(s[0])
                fp.write( s.replace('[',''))
            fp.close()


            lines = open(filepath1).readlines()
            fp = open(filepath1,'w')
            for s in lines:
                fp.write(s.replace(']',""))
            fp.close()


            lines = open(filepath1).readlines()
            fp = open(filepath1,'w')
            for s in lines:
                fp.write(s.replace(','," "))
            fp.close()

            lines = open(filepath2).readlines()
            fp = open(filepath2,'w')
            for s in lines:
                #print(s[0])
                fp.write( s.replace('[',''))
            fp.close()


            lines = open(filepath2).readlines()
            fp = open(filepath2,'w')
            for s in lines:
                fp.write(s.replace(']',""))
            fp.close()


            lines = open(filepath2).readlines()
            fp = open(filepath2,'w')
            for s in lines:
                fp.write(s.replace(','," "))
            fp.close()

    print("done!!!  "+str(src1)+"-"+str(src2)+" --> "+str(dst1)+"-"+str(dst2))

#txtreplacechar(0,4,2,18,28,2)
#txtreplacechar(0,4,2,40,50,2)
#txtreplacechar(6,10,2,62,72,2)
txtreplacechar(6,10,2,84,94,2)
txtreplacechar(18,20,1,40,50,2)
txtreplacechar(18,20,1,26,33,1)

print("all done!!!")
