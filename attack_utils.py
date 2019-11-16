
import nltk
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def get_tokens(sent):
    """
    return words tokens
    """
    return nltk.word_tokenize(sent)
    
def get_synonymes(word):
  
  '''
  using sysset from wordnet to get all possible synonyms
  '''
  
  def get_word(word_with_type):
    #get_synonymes('weak') -> returns all synonyms,all synonyms in dict with type of word
    """ 
    the function takes a string like "dog.n.01" and return dog,n so we know what
    type of word we have like is it verb for v adj for a and n for noun
    """
    word_new = word_with_type.split('.')[0]
    word_new = word_new.replace('_'," ")
    return (word_new,word_with_type.split('.')[1])
  
  synsets = wordnet.synsets(word)
  syn = [x.name() for x in synsets]
  for x in synsets:
    syn+=list(i.name() for i in x.hypernyms())
  syn = set(get_word(s) for s in syn)
  sss = set()
  for s in syn:
    a,b = s
    if a == word:
      continue
    sss.add(a)
  syn_dict = {}
  for w,t in syn:
    if t not in syn_dict:
      syn_dict[t]=set()
    if w == word:
      continue
    syn_dict[t].add(w)
  return sss,syn_dict

