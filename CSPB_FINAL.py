#welcome text!
print("\n")
print("Welcome! Let's conduct a search!\n")
print("Below you will see a list of available texts, please follow the instructions given.\n")
print("Thanks  - happy searching!\n")


#text library!
avail_texts = {
    '1' : ("Annabel Lee by Edgar Allan Poe", '/Users/a/Documents/CSPB2270/annabel_lee.txt'),
    '2' : ("Covehithe by China Mieville", '/Users/a/Documents/CSPB2270/Covehithe by China Miéville.txt'),
    '3' : ("A Review of Domestic Dogs Human-Like Behaviors: Or Why Behavior Analysts Should Stop Worrying and Love Their Dogs by Monique Udel et al \n", '/Users/a/Documents/CSPB2270/dog.txt')
}

#display the text library
print("Available texts: ")
for key, (title, path) in avail_texts.items():
    print(f"({key}) {title}")

#user text selection by num!
text_choice = input("Enter the number for the text you would like to use today: ")
if text_choice not in avail_texts:
    print("That text is not in our library.")
    #exit bc invalid choice
    exit()

#pull the correct text path
title, input_txt = avail_texts[text_choice]


#ask for a word to search
target_word = input("What word would you like to search for? Enter it here: ")

#would user like the inv index printed?
print_index = input("Would you like the  index to be printed? Enter yes or no: ")

#how many context words for search??
context_words = int(input("How many context words would you like on each side of the target word? Enter a number here: "))

#FIRST - CREATE INV INDEX
def create_inv_index(input_txt):
    #init empty dictionary
    inv_index = {}

    #now open input file (in read mode!!)
    with open(input_txt, 'r') as text:
        #break file down into lines
        for line_num, line in enumerate(text, start = 1):
            #break line into words
            words = line.split()
            #for each word..
            for word in words:
                #make it lowercase and get rid of hanging punctuation
                word = word.lower().strip(",.!?")
                #if word already in index..
                if word in inv_index:
                    #append another line location to word!
                    inv_index[word].append(line_num)
                else:
                    #else just add  to index w current line num
                    inv_index[word] = [line_num]
    
                #print(f"Word '{word}' appears on line {line_num}")
    return inv_index

#call inv index func
index = create_inv_index(input_txt)

#print the inv index here if user selected yes
if print_index == 'yes':
    print("Inverted Index for text: ", index)

#(quick middle step - read text in as a single line)
    #(this eliminates line break confusion relating to context words)
def text_to_single_line(input_txt):
    #open file as in read
    with open(input_txt, 'r') as file:
        #replace a new line w a space (to make the single str text)
        text_one_line = file.read().replace('\n', ' ')
    return text_one_line

#call the single line func here
text_one_line = text_to_single_line(input_txt)

#SECOND - CONCORDANCE!!
def concord(text_one_line, target_word, context_words=3):
    #split the text into words!
    words = text_one_line.split()
    #init empty list for word locations
    word_location = []
    #make target word lowercase for easier searching
    low_target_word = target_word.lower()
    #loop to search thru words, create temp index of words..
    #..that helps us locate where a word is (to find context)
    for i, word in enumerate(words):
        #remove attached punc from word, make lowercase
        no_punc = word.strip(",.!?").lower()
         #check if word matches the input word
        if no_punc == low_target_word:
            #if match, add to word location list!!
            word_location.append(i)
    return word_location

#call concord func here
word_concord = concord(text_one_line, target_word, context_words)

#THIRD - PRINT CONCORDANCE
def print_context(words, word_location, context_words):
    #
    if not word_location:
        print(f"The word '{target_word}' does not appear in this text.")
    else:
        #loop through ea instance of target word, for ea instance..
        for index in word_location:
            #calculate starting index
            start = max(0, index - context_words)
            #calculate ending index
            end = min(len(words), index + context_words + 1)
            #pull words between start + end and put 'em all together
            #..w the target word!!
            context = ' '.join(words[start:end])
            print(f"Context for word '{words[index]}' : {context}")

#call print func here
print_context(text_one_line.split(), word_concord, context_words)