

import json


def creattraindata(src1,src2,srcbujin,dst1,dst2,dstbujin):
    # linkspair = list()
    with open("/home/stack/code/pythontest/linkpairofpath.json", encoding="utf-8") as f2:
        linkspair=json.load(f2)
        f2.close()
    for i in range(src1,src2+1,srcbujin):
        for j in range(dst1,dst2+1,dstbujin):
            link184ge = list()
            with open("/home/stack/code/pythontest/data184X("+str(i)+"-"+str(j)+").json", encoding="utf-8") as f3:
                while True:
                    line = f3.readline()
                    if not line:
                        break
                    link184ge.append(json.loads(line))
                f3.close()

            for k in range(len(link184ge)):
                writetotxt = list()
                for m in range(len(linkspair[str(i)+"->"+str(j)])):
                    srcnode = linkspair[str(i)+"->"+str(j)][m][0]
                    dstnode = linkspair[str(i)+"->"+str(j)][m][1]
                    writetotxt.append(link184ge[k][str(srcnode)+"->"+str(dstnode)])
                f4 = open("/home/stack/code/pythontest/datafortrain/datafortrain(" + str(i) + "-" + str(j) + ").txt", "a")
                f4.write(str(writetotxt) + "\n")
                f4.close()

            # for k in range(len(link184ge)-390,len(link184ge)):
            #     writetotxt = list()
            #     for m in range(len(linkspair[str(i)+"->"+str(j)])):
            #         srcnode = linkspair[str(i)+"->"+str(j)][m][0]
            #         dstnode = linkspair[str(i)+"->"+str(j)][m][1]
            #         writetotxt.append(link184ge[k][str(srcnode)+"->"+str(dstnode)])
            #     f4 = open("/home/stack/code/pythontest/datafortest/datafortest(" + str(i) + "-" + str(j) + ").txt", "a")
            #     f4.write(str(writetotxt) + "\n")
            #     f4.close()
                
    print("train and test data of "+str(src1)+"-"+str(src2)+"-->"+str(dst1)+"-"+str(dst2)+" have done!!!")


#creattraindata(0,4,2,18,28,2)
#creattraindata(0,4,2,40,50,2)
#creattraindata(6,10,2,62,72,2)
creattraindata(6,10,2,84,94,2)
creattraindata(18,20,1,40,50,2)
creattraindata(18,20,1,26,33,1)

print("all done!!!")
