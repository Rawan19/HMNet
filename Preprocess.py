import json
import spacy
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

def preprocess_raw(raw_text : str) :
  # nlp = spacy.load('en', parser = False)
  json_dict_outer =  {}
  json_dict =  {}
  json_dict_outer['id']="1"
  nlp_spacy = spacy.load("en_core_web_sm")
  POS = {w: i for i, w in enumerate([''] + list(nlp_spacy.tagger.labels))}
  ENT = {w: i for i, w in enumerate([''] + nlp_spacy.entity.move_names)}
  name_role_dict = {'Ashwin Swarup' : 'PM' , 'Siddhant Bane' : 'ID' , 'Shashank M' :'UI' , 'Mitesh Gupta' :'ME'}

  list_dicts = [] 
  turns = text.split('\n')
  for turn in turns : 
    
    json_dict =  {}
    if len(turn) < 1 : continue 
    name = turn.split(":", 1)[0]
    role_name = name_role_dict[name] 
    json_dict['speaker'] = name
    json_dict['role'] = role_name

    word_text = turn.split(":", 1)[1]
    tokenized_text = word_tokenize(word_text)
    json_dict['utt'] = {}
    output = {'word': [], 'pos_id': [],'ent_id': []}
    output['word'] = tokenized_text

    for token in nlp_spacy(word_text):
      pos = token.tag_
      output['pos_id'].append(POS[pos] if pos in POS else 0)
      ent = 'O' if token.ent_iob_ == 'O' else (token.ent_iob_ + '-' + token.ent_type_)
      output['ent_id'].append(ENT[ent] if ent in ENT else 0)

    json_dict['utt'] = output
    list_dicts.append(json_dict)
    json_dict_outer['meeting'] = list_dicts
    json_dict_outer['summary']=[""]
  return json_dict_outer




json_file= preprocess_raw(text)
with open('test_raw_newid.json', 'w') as fout:
    json.dump(preprocess_raw(text),fout)
    
    
#convert json to jsonl
with open('test_raw_newid.jsonl', 'w') as outfile:
    for entry in [json_file]:
      # print(entry)
     
        json.dump(entry, outfile)
        outfile.write('\n')
        
#gzip
import gzip
with open('ExampleRawData/meeting_summarization/AMI_proprec/test/test_raw2.jsonl', 'rb') as f_in, gzip.open('ExampleRawData/meeting_summarization/AMI_proprec/test/test_raw2.jsonl.gz', 'wb') as f_out:
    f_out.writelines(f_in)
