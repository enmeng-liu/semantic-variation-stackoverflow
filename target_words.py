import pickle, os

freq_path = "/data/StackOverflow/Communityposts/data/annual/frequency"
output_file = "/data/StackOverflow/Communityposts/data/annual/frequency/target-words-truncated.pkl"

def get_most_frequent_words(year, count=5000):
    with open(os.path.join(freq_path, "freq-{}-truncated.pkl".format(year)), 'rb') as f:
        freq_dict = pickle.load(f)
    sorted_freq = {k: v for k, v in sorted(freq_dict.items(), key=lambda item: -item[1])}
    return list(sorted_freq.keys())[:count]

target_words = set()
for year in range(2010, 2021):
    year_words = get_most_frequent_words(year)
    if len(target_words) == 0:
        target_words = set(year_words)
    else:
        target_words = target_words.intersection(year_words)
    print(str(year) +" completed.")

target_words_list = list(target_words)
print(target_words_list[:100])
print("size={}".format(len(target_words_list)))
with open(output_file, 'wb') as f:
    pickle.dump(target_words_list, f)


    