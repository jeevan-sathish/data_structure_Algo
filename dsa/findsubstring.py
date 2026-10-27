
string = "hello"
sentence = "this is hellow"

def find_substring(string, sentence):
  i=0
  j=0
  while (i<len(sentence)):
    if(sentence[i]== string[j]):
      j+=1
      

      if(j==len(string)):
        return True

    else:
      j = 0

    i+=1
    
  return False
 
  
print(find_substring(string, sentence))
