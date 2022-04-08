from collections import Counter
import os
import pickle

corpus_path = "/data/StackOverflow/Communityposts/data/annual/"
output_path = "/data/StackOverflow/Communityposts/data/annual/frequency"



def count_word(file_name):
    with open(file_name) as f:
            return Counter(f.read().split())

def count_word_of_year(year):
    file_name = os.path.join(corpus_path, "all-{}-truncated.txt".format(year))
    freq_dict = count_word(file_name)
    return freq_dict


for year in range(2010, 2021):
    freq_dict = count_word_of_year(year)
    output_file = os.path.join(output_path, "freq-{}-truncated.pkl".format(year))
    with open(output_file, 'wb') as f:
        pickle.dump(freq_dict, f)
    print(year, "completed.")