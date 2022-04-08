import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
import pickle, os
# MODEL_NAME = 'jeniya/BERTOverflow'
MODEL_NAME = "bert-base-uncased"
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME, output_hidden_states=True)
model = model.to(DEVICE)
corpus_path = "/data/StackOverflow/Communityposts/data/annual/"

def assign_GPU(Tokenizer_output):
    tokens_tensor = Tokenizer_output['input_ids'].to(DEVICE)
    token_type_ids = Tokenizer_output['token_type_ids'].to(DEVICE)
    attention_mask = Tokenizer_output['attention_mask'].to(DEVICE)
    output = {'input_ids' : tokens_tensor, 
        'token_type_ids' : token_type_ids, 
        'attention_mask' : attention_mask}
    return output

def get_sent_embeddings(sent, encoded):
    input = assign_GPU(encoded)
    with torch.no_grad():
        output = model(**input)
    states = output.hidden_states
    output = torch.stack([states[i] for i in [-4, -3, -2, -1]]).sum(0).squeeze()
    return output

import os
year = 2011
with open(os.path.join(corpus_path, 'frequency', 'common-words-brown.pkl'), 'rb') as f:
    words = pickle.load(f)
corpus_file_path = os.path.join(corpus_path, "all-{}-truncated.txt".format(year))
w2u = {w: [] for w in words} # word -> usages
cnt = 0
bunch_size = 10000

with open(corpus_file_path, 'r') as f:
    for line in f:
        if len(line) > 512:
            line = line[:512]
        encoded = tokenizer.encode_plus(line, return_tensors="pt")
        sent_embeddings = get_sent_embeddings(line, encoded)
        line_words = line.split(' ')
        for word in words:
          if word in line_words:
            idx = line_words.index(word)
            token_ids_word = np.where(np.array(encoded.word_ids()) == idx)
            word_embedding = sent_embeddings[token_ids_word].mean(dim=0)
            w2u[word].append(word_embedding.numpy())
        
        cnt += 1
        if cnt % bunch_size == 0:
            print(cnt, "lines.")
    
    # with open(os.path.join(corpus_path, 'embeddings', 'common-words-{}-truncated-base.pkl'.format(year)), 'wb') as f:
    #     pickle.dump(w2u, f)

torch.save(w2u, os.path.join(corpus_path, 'embeddings','common-words-embeddings-{}-truncated-base-brown.pt'.format(year)))
print(year, "completed.")