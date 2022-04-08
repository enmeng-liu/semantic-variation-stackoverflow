import re
import os

corpus_path = "/data/StackOverflow/Communityposts/data/annual/"
bunch_size = 1000000

text = '''And as expected, the stuff echoed from inside the threads seems weird, however if you store the results, and sort them by the time they were executed, you can see it acts as expected.I have found similar code here (http://sahatyalkabov.com/jsrecipes/#!/backend/who-is-online-with-socketio) and yes, this is the correct way to use sockets.It fires so many requests because every time a user connects and every time a user disconnects a message is fired (including when you reload.when you reload it fires twice, 1 for getting out and 1 for getting back on the site).I'm having trouble figuring out why my "Remove" button is not working as intended.I'm working on a webpage.Long story short, the main page contains a table whose rows are added via user input, some SQL database queries, and Flask.I want to be able to remove rows w/o refreshing the page, so I got some help constructing an AJAX call to do just that.This is the portion meant to handle that action'''


def remove_url(text):
    return re.sub(r'\w*:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)


# year = 2021
cnt = 0
for year in range(2008, 2021):
    write_lines = []
    with open(os.path.join(corpus_path, "all-{}.txt".format(year)), mode='r') as f:
        for line in f:
            if len(line) > 0 and line != '\n':
                line = remove_url(line).lower()
                if len(line) > 0:
                    write_lines.append(line)
            cnt += 1
            if cnt % bunch_size == 0:
                print(cnt, " lines")
    with open(os.path.join(corpus_path, "all-{}-2.txt".format(year)), mode='a') as f2:
        f2.writelines(write_lines)
    print(str(year) + "finished.")