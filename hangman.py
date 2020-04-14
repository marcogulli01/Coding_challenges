
# Challenges proposed at https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs

import numpy as np
import string
import random
import urllib.request

def pick_a_word(): # function to download the library sowpods, composed of thousands of words

	url = "http://norvig.com/ngrams/sowpods.txt"

	file = urllib.request.urlopen(url) # download the file

	words = []

	# decode the file using "UTF-8" and choose only words with more than 3 letters for a reason of game difficulty

	for line in file:
		if len(line.decode("utf-8")) > 3:
			words.append(line.decode("utf-8"))

	output_word = random.choice(words).lower() # convert to lowercase

	output_word = output_word[0:len(output_word)-1] # delete the final character, "\n"

	return output_word

# function to guess the word. It should return only the first and the last letter of the word to guess

def guess_a_letter(word):

	m = len(word) # length of the word to guess
	lett_list = ['-']*m # build a list composed of hyphens and with length equal to m 
	lett_list[0], lett_list[m-1] = word[0], word[m-1]
	# replace the first and the last hyphen with the first and the last letter

	return ''.join(map(str, lett_list)) # return the list converted into a string

# function to fill the word with the exact letters

def locate_letter(incomplete_word, complete_word, let):

	incomp_list = list(incomplete_word) 
	comp_list = list(complete_word)

# the exact letter should be appended to the incomplete word
	
	for i in range(len(comp_list)):
		if let == comp_list[i]:
			incomp_list[i] = let

	return ''.join(map(str, incomp_list) # return the incomplete word filled with the exact letters


if __name__ == '__main__':

	word_to_guess = pick_a_word()
	to_guess = guess_a_letter(word_to_guess)

	print("Welcome, you are playing hangman. The word you should guess is: ", to_guess)

	# the total number of attempts by the user should not overcome 6

	count = 0
	while count < 7:
		if to_guess != word_to_guess:
			l = str(input("Type a letter, please:")).lower() # l = letter typed by the user
			if l in word_to_guess[1:len(word_to_guess)-1]: # is l one of the letters of the word, different from the first and the last one?
				print("The word becomes", locate_letter(to_guess, word_to_guess, l))
				to_guess = locate_letter(to_guess, word_to_guess, l)
			else: # if l does not belong to the word, decrease the number of available attempts by 1
				count += 1
				print("Sorry, this letter does not belong to the word. You still have " + str(7 - count) + " attempts left.")



	if to_guess != word_to_guess: 
		print("Sorry, you lose. The word was: "+str(word_to_guess))
	else:
		print("Congratulations, you win.")






