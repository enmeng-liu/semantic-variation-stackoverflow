from get_word_embedding import get_word_embedding
import pickle, os

def collect_word_usages_yearly(word, year, corpus_file_path, bunch_size=100000, model="jeniya/BERTOverflow"):
    usages = []
    cnt = 0
    with open(corpus_file_path, 'r') as f:
        for line in f:
            cnt += 1
            if bunch_size > 0 and cnt % bunch_size == 0:
                print(str(cnt) + " lines.")
            if len(line) > 512:
                line = line[:512]
            if ' ' + word + ' ' in ' ' + line + ' ':
                w = get_word_embedding(word, line)
                usages.append(w)
    return usages



corpus_path = "/data/StackOverflow/Communityposts/data/annual/"
fork_yearly = {}
for year in range(2009, 2022):
    corpus_file_path = os.path.join(corpus_path, "all-{}-3.txt".format(year))
    usages = collect_word_usages_yearly(word='fork', year=year, corpus_file_path=corpus_file_path, bunch_size=100000)
    with open('./data/fork-so-{}.pkl'.format(year), 'wb') as f:
        pickle.dump(usages, f)
        print(str(year) + " completed.")
    fork_yearly[year] = usages
with open('./data/fork-so.pkl', 'wb') as f:
    pickle.dump(fork_yearly, f)
    