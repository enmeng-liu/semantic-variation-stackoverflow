from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
import nltk

text = '<p>I want to use a <code>Track-Bar</code> to change a <code>Form</code>\'s opacity.</p><p>This is my code:</p><pre class="lang-cs prettyprint-override"><code>decimal trans = trackBar1.Value / 5000;this.Opacity = trans;</code></pre><p>When I build the application, it gives the following error:</p><blockquote><pre class="lang-none prettyprint-override"><code>Cannot implicitly convert type decimal to double</code></pre></blockquote><p>I have tried using <code>trans</code> and <code>double</code>, but then the<code>Control</code> doesn\'t work. This code worked fine in a past VB.NET project.</p>'

csv_path = "/data/StackOverflow/Communityposts/data/Posts.csv"
# corpus_path = "data/"
corpus_path = "/data/StackOverflow/Communityposts/data/annual/"
bunch_size = 10000

def remove_codes_and_html_tags(raw_text):
    if len(raw_text) == 0:
        return ""
    soup = BeautifulSoup(raw_text, features="lxml")
    for s in soup(['code', 'pre', 'script', 'style', 'blockquote']):
        s.extract()
    return soup.get_text()

def corpus_file_name(creation_date):
    date = datetime.fromisoformat(creation_date)
    return os.path.join(corpus_path, "all-{}.txt".format(date.year))

cnt = 0
with open(csv_path, mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
        creation_date = line["CreationDate"]
        body = line["Body"]
        title = line["Title"]
        sentences = nltk.sent_tokenize(remove_codes_and_html_tags(body))
        if len(title) > 0:
            sentences.append(remove_codes_and_html_tags(title))
        with open(corpus_file_name(creation_date), mode='w') as txt_file:
            txt_file.writelines(sentences)
    
        cnt += 1
        if (cnt % bunch_size == 0):
            print(cnt, "row")
        # if cnt >= 100:
        #     break