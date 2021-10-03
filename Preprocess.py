import json
import spacy
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

print("Preprocessing the input file ...")
def preprocess_raw(raw_text : str) :
  nlp = spacy.load('en', parser = False)
  json_dict_outer =  {}
  json_dict =  {}
  json_dict_outer['id']="1"
#   nlp_spacy = spacy.load("en_core_web_sm")
  POS = {w: i for i, w in enumerate([''] + list(nlp.tagger.labels))}
  ENT = {w: i for i, w in enumerate([''] + nlp.entity.move_names)}
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


text = """
Ashwin Swarup:Alright, let's let's start then. So, welcome to the Daily call. So I wanted a basic update on where we are on ditto, so mitesh can even brought update on that.
Mitesh Gupta: Oh yeah. So deter we have finally our position was in this Marketplace and we have got our latest app available on the marketplace with the updates, about the installation steps and new screenshots. We are waiting to put a new video so that will get a new release next week. Next early. Next week, as well as we're in talk with the Eric, the representative
Mitesh Gupta:person of zendes where you can help us with the marketing of video. So we are all
Ashwin Swarup:No. Yeah I also got a video the latest video from anitage and looks good. So I send it for approval to my. So let's see if If you approves it, I will set it up on the detail. but,
Mitesh Gupta:Corporation, then we can work.
Ashwin Swarup:But on the whole, it looks good.
Mitesh Gupta:Yeah. And as well as what I have seen. I have also seen the Google analytics page for dito and I've seen around 8 to 15 requests are there. Like people have visited to our little page,
Ashwin Swarup:That's good. So I mean, the initial days two days since deployment. Let's see how it goes. All right, what's the status on Chiron?
Siddhant Bane:Yeah. So in terms of testing we have we are done with our unit tests and today we have pushed them I think with it can review them and basically approve our pull request and we will be done with that apart from that we are working on the chat server where like we discussed in yesterday's meeting, we are going to incorporate handoff feature and Also, the scalability issues that we were facing, we're going to address. From that Shashank can update.
Shashank M:Oh yeah. So from my side, I had a few Test cases remaining. And as, after that, udit also told me to make a few more code changes to the API for the document passing an intense generation. So we made a, we made the remaining changes and I've pushed the code and with the HTTP action file on the HTTP download and upload code, which I had written. So I've put the changes for that as well. So I just have to sit with Throne to make the UI changes. So yeah so after that I'm done with the unit test case now I just have a few Service Test cases remaining. So once I'm done with that, I'll push it to get
Ashwin Swarup:And the knowledge graph test cases are also done the part where we were trying to do question augmentation test cases now that that needs to still start.
Shashank M:With the knowledge craft test cases. So it's divided into two and that one is the document passing. And then the Generation. The addition of the training.
Ashwin Swarup: Yeah.
Shashank M: So So the first one, the document passing test cases are all done so the other one which was to add the generated intense and responses for that. We were facing a few issues. So with its help you were able to just you know just get the edge cases out. So if it's failing we're giving the particular the necessary output messages. So yeah, that's all done.
Ashwin Swarup: All right. Sounds good. Thanks a lot, guys.

"""


json_file= preprocess_raw(text)
with open('test_raw_newid.json', 'w') as fout:
    json.dump(preprocess_raw(text),fout)
    
    
#convert json to jsonl

with open('ExampleRawData/meeting_summarization/AMI_proprec/test/test_raw2.jsonl', 'w') as outfile:
    for entry in [json_file]:
      # print(entry)
     
        json.dump(entry, outfile)
        outfile.write('\n')
        
#gzip
import gzip
with open('ExampleRawData/meeting_summarization/AMI_proprec/test_raw2.jsonl', 'rb') as f_in, gzip.open('ExampleRawData/meeting_summarization/AMI_proprec/test/test_raw2.jsonl.gz', 'wb') as f_out:
    f_out.writelines(f_in)
    
print("Prerpocessing is Complete!")
