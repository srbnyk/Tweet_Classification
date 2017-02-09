import os
import codecs
import re
#l = ["sport","technology","law","politics","health"]
#l = ['education','travel','nature','fashion','lifestyle','entertainment']
l = ['sport','technology','law','politics','health', 'education','travel','nature','fashion','entertainment']
dir = 'Tweet_Data'
if not os.path.exists(dir):
    os.makedirs(dir)

for item in l:
    old_dir = 'Tweets_Old'+'\\'+item
    new_dir = dir+"\\"+item
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    read_f = old_dir + "\\" + item + '0101' + ".txt"
    print (read_f)
    f1 = codecs.open(read_f, encoding='utf-8', mode='r')
    ct=0
    for line in f1:
        if line.isspace():
            continue
        temp = '#'+item
        line = re.sub(temp,'',line)
        file_name = new_dir+"\\"+str(ct)+".txt"
        f2=codecs.open(file_name,encoding='utf-8',mode='w')
        f2.write(line)
        f2.close()
        ct += 1