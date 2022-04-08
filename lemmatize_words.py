from nltk.stem import WordNetLemmatizer
import nltk
import os
nltk.download('wordnet')
nltk.download('omw-1.4')
 
lemmatizer = WordNetLemmatizer()

def lemmatize_all_words(text):
    return ' '.join([lemmatizer.lemmatize(w) for w in text.split(' ')])

text = "look on the popular forked list and you ll probably see something that interest you i had to do this for a project before one of the major difficulty i had wa explaining what i wa trying to do to other people i spent a ton of time trying to do this in sql  but i found the pivot function woefully inadequate i do not remember the exact reason why it wa  but it is too simplistic for most application  and it isn t full implemented in m sql 2000 i wound up writing a pivot function in  net i ll post it here in hoincluding the four space in front each line from timocracy com generally when i use clickonce when i build a vb net program but it ha a few downside i ve never really used anything else  so i m not sure"


for year in range(2008, 2021):
    lines = []
    cnt = 0
    bunch_size = 100000
    with open(os.path.join("/data/StackOverflow/Communityposts/data/annual/", "all-{}-3.txt".format(year)), 'r') as f:
        for line in f:
            cnt += 1
            if cnt % bunch_size == 0:
                print(cnt, "lines.")
            lemmatized = lemmatize_all_words(line)
            if len(line) > 512:
                line = line[:512]
            if len(line) > 0:
                lines.append(line)
    with open(os.path.join("/data/StackOverflow/Communityposts/data/annual/", "all-{}-4.txt".format(year)), 'w') as f:
        f.writelines(lines)