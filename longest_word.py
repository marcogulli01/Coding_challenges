
# Solution of the challenge LongestWord proposed on Coderbyte at https://coderbyte.com/challenges

"""
After converting the input to a list, we should remove all the characters which are not letters. Therefore,
the words are stored into a list. Then, after storing each word length into a list, we should get the index of the
first word with maximal length and print it.
"""

def LongestWord(sen):
  sent = list(sen.split(' '))

  words = []
  for item in sent:
    word = str()
    for i in range(len(item)):
        if item[i].isalpha():
          word += item[i]

    words.append(word)

#    print(words)

  lens = []
  for word in words:
    lens.append(len(word))

  m = next(lens.index(x) for x in lens if x == max(lens))

  return sent[m]

# keep this function call here
print(LongestWord(input()))
