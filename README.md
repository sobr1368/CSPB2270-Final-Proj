# CSPB2270-Final-Proj
Inverted Index and Concordance Generator for Text Analysis

PROJECT GOAL
------------
To facilitate more efficient analysis of lengthy transcripts of Native American languages through the use of inverted indexes 
and a concordance generator. The user would be able to upload a text file of any size and quickly search for a word or phrase. 
The program would then return an index of where the word or phrase can be found in the text, and the sample of text in which the input 
occurs. Concordance generation will allow the linguistic researcher to see the context for the input and allow for faster pattern-recognition 
which can help to accurately place the word or phrase’s usage in the language. This would also help to build a linguistic database that 
can be continuously added to and easily used. 
 

  METHODOLOGY 
  -----------
 I will be implementing this code using Python, a common language used in linguistic research and one that I 
 would like to get more experience with - particularly with code that uses some elementary Natural Language Processing (NLP). 
 
- Data input: I will be sourcing some large transcripts of text that the user can then use to search for particular words or 
    phrases, while also creating a way for the user to upload their own text file that they would like to explore.

- Concordance generator: In linguistics, concordance is used to show context to a given word or phrase. If a researcher 
  wants to understand what a word means, they need to see it in a variety of different usages. Each example shows how the 
   word can be used differently (or not!). This is a valuable tool in spotting patterns for words.
 
- Inverted Index: I will be using an inverted index, which functions differently from a regular index by directing 
  the user to the specific line, page, and document that the word can be found on. Inverted indexes are commonly 
 used in search engines and map the input variable directly to their location.
 
- Hash-Map Dictionary: A dictionary will be created using a hashmap for the code to store and quickly search for 
the input word or phrase. Hashmaps are extremely efficient and have a computational complexity of constant time, or O(1).

- Interface Design:I would like to explore some interface design but am a bit intimidated by that idea - I’m aiming to 
create something simple that will allow for easier and more streamlined interaction with the code.
 

 EXPECTED OUTCOME 
------------------
Linguistic researchers will be able to more efficiently analyze bodies of text or datasets, perform quick searches on words or phrases, and easily see context for a word or phrase. Across very large bodies of text or many data sources, this can lend a significant uptick in speed of research. This program would also allow for easier analysis of semantic or lexical patterns, allowing researchers to easily see common contexts for a word as well as explore things like common prefixes or suffixes



 INVERTED INDEXES: DETAILED 
-----------------------
Inverted indexes are a reverse mapping of words to their location in text, typically implemented using a hashmap 
or (dictionary in Python). Here, the target word is the key, and the list of locations of that word is the value. The inverted index supports efficient searching by avoiding the need to iterate over the entire text, which is especially useful in the concordance generator.
To create an inverted index, the text needs to be broken down into words, and then the locations of every word stored. In this code, the words are all converted to lowercase prior to being added to the hashmap/dictionary so that there is less room for error or confusion through the addition of uppercase letters.


 RUNNING THE CODE 
 -----------------
1. You have been added as a member to this private repository, I think that means you can download the files and then run them locally through a terminal...GitHub is still so difficult for me and I tried to find more detailed descriptions for what to do but they all seemed a bit unclear to me. Crossing my fingers and letting jesus take the wheel a litte bit at this point!

2. Now that you are running the code through the terminal, the UI should make it easy! Simply follow the instructions as
   they are given. Those will be:
       a. Select a text from the displayed library
       b. Enter a target word for the code to search for
       c. Decide whether you would like the inverted index to be displayed or not
       d. Determine how many words of context you would like to see and input that number
   
4. The output of this will be the inverted index (if selected to display), each occurence of the input target word surrounded by however many context words were specificed by the user.


 SOME CLOSING THOUGHTS 
 --------------------
1. This code converts all words to lower case in order to check if the word has already been logged into the inverted index. This is fine for researching familiar words in a familiar language, but may present issues in unfamiliar languages. What if the word containing a capital letter distinguishes it from a different word that is all lower case and the researcher doesn't know that yet? An example off the top of my head, what if you were researching the word  “hunter”. In the English language, this word could be used to describe someone who hunts, but if capitalized it can become a proper noun and someone’s name. This may cause issues in research.

2. I would like this code to be functional for other languages (specifically transcripts of Native American languages), but I think that would complicate the search quite a bit as Native American languages were oral, and transcriptions often use phonological symbols to signify letters or sounds, which I would need to account for in my search. I ran out of time to work around a new alphabet in this code, but I think it is something I will continue to play around with over the summer.

3. Coding this project was both easier and harder than I exptected. Python is certainly a lot more beginner-friendly than C++, but my lack of practice with it did really slow me down. I enjoyed googling how to approach this and learning about all of the cool things python just /knows/ how to do without me writing any extra code. It also slowed things down significantly. I think that having to take what I've learned and apply it to another language was a really good way for me to cement some of the theory and concepts in my head, and I would ultimately like to take this post-bacc program into a career that has me working with NLP and language research regularly, so I am glad that I used Python and stretched that muscle a little after such a long break from CSPB1300. I'm proud of this project, but I do wish I had been able to go a little further with it than I did here. It is certainly still very elementary and I'm not sure if it falls under "impressive" quite yet, even for my level of learning. However, it is definitely something that I can continue to come back to, modify, and expand on as I continue my classes. It really felt cool to apply some of what we've done to a specific project that I am passionate about and see it in the context of my own learning goals. 













