"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#define a list called some_words and the string ("what", "does", "this", "line", "do", "?")is in the list
some_words = ["what", "does", "this", "line", "do", "?"]

#I think this will print each word in this list 
for word in some_words:
    print(word) #it printed "what does this line do ?" in seperate line

#I am not sure what this will print
for x in some_words: #x is temporary variable that holds each value of the list just like "word"
    print(x) #it printed "what does this line do ?"" in seperate line

#I think this will print the entire list with the bracket [] and comma,
print(some_words) #it printed "['what', 'does', 'this', 'line', 'do', '?']"

#if the length of the list (how many member in the list) is larger than 3 (in this list is 6)
if len(some_words) > 3:
    #I think this will print the word "some_words contains more than 3 words
    print("some_words contains more than 3 words") #it printed "some_words contains more than 3 words"


#define the function called usefulFunction with no input
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #I think this will print system, node, release, version, machine, and processor of this code
    print(platform.uname()) #it printed "uname_result(system='Windows', node='DESKTOP-MGHQ3DG', release='11', version='10.0.22631', machine='AMD64')"


#I think this will run usefulFunction 
usefulFunction()
