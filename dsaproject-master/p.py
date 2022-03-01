from tkinter import *
from PIL import Image, ImageTk
import palin
import PatternMatching
import Anagram
root = Tk()

root.title("Projectt")
image = ImageTk.PhotoImage(Image.open("stringg.png"))
image1 = Label(image=image)
image1.pack()


def open():
    top = Toplevel()
    anagram = Button(top, text="ANAGRAMS", font=100, bg="#E3DFD7", padx=50, pady=20, command=anagrams)
    anagram.pack()

    palin = Button(top, text="PALINDROME", font=100, bg="#C1EDEF", padx=50, pady=20, command=palindrome)
    palin.pack()

    sub = Button(top, text="SUBSEQUENCE STRINGS", font=100, bg="#C9D2D1", padx=50, pady=20, command=anagrams)
    sub.pack()

    pattern = Button(top, text="PATTERN SEARCHING", bg="#958D85", font=100, padx=50, pady=20, command=patterns)
    pattern.pack()

    def help():
        mylabel = Label(top, text ="\n \nHere manipulation of strings is done using various operations.\n \n \n An anagram is a word that is produced by rearranging the letters of the word itself. \nLet's take a look at the word ELBOW. We can say that BELOW is anagram of ELBOW, since BELOW uses all the original letters of ELBOW exactly once. \nNot only from one word, an anagram can also be created from, and can create, two or more words: SCHOOL MASTER is an anagram of THE CLASSROOM, or FOURTH OF JULY is an anagram of JOYFUL FOURTH.\n \n \n A palindrome is a string, or sequence of characters, that has the exact same spelling both forward and backward.\n NOON, MADAM, RADAR, and ROTATOR are some examples of the palindrome. \nSimilar to the anagram, we can also construct a palindrome from more than one word; for instance, A NUT FOR A JAR OF TUNA, or NO LEMON NO MELON. \n \n \n Subsequence string is a string derived from another string by deleting some characters without changing the order of the remaining characters.\n \n \n Pattern searching is an algorithm to find out the location of a string in another string. This process is usually used in a word processor to find a word position in a document.",font= 20).pack()

    help = Button(top, text="HELP", bg= "#DED4D8", font=100, padx=50, pady=20, command=help)
    help.pack()




def anagrams():
    top = Toplevel()
    entries = [Entry(top) for _ in range(2)]
    for entry in entries:
        entry.pack()
    submmit = Button(top, text="clickToSubmit", font=100, bg="#E3DFD7", padx=50, pady=20, command=lambda:click(entries)).pack()

    def click(enteries):
        l1 = enteries[0].get()
        l2 = enteries[1].get()
        Text = ""
        isAnagram = Anagram.anagramCode(l1, l2)
        if isAnagram:
            Text = "Anagram"
        else:
            Text = "Not anagram"
        label = Label(top, text=Text).pack()

def patterns():
    def click(enteries):
        text=enteries[0].get()
        pattern=enteries[1].get()
        output=PatternMatching.KMPSearch(pattern,text)
        if len(output) == 0:
           label= Label(top, text="No matches found").pack()
           #Modified from previous version
        else:
            textWidg = Text(top)
            textWidg.insert(INSERT,text)
            textWidg.pack()
            for label in output:
                i=0
                textWidg.tag_add(str(i),"1."+str(label),"1."+str(label+len(pattern)))
                i=i+1
            for label in output:
                i=0
                textWidg.tag_config(str(i), background="black", foreground="green")
                i=i+1
    top=Toplevel()
    entries = [Entry(top) for _ in range(2)]
    for entry in entries:
        entry.pack()
    submmit = Button(top, text="clickToSubmit", font=100, bg="#E3DFD7", padx=50, pady=20,
                     command=lambda: click(entries)).pack()
def palindrome():
    top=Toplevel()
    enteries=Entry(top)
    enteries.pack()
    submit = Button(top, text="clickToSubmit", font=100, bg="#E3DFD7", padx=50, pady=20,command=lambda: click(enteries)).pack()
    def click(entery):
        text=entery.get()
        print(text)
        isPalindrome = palin.checkPalindrome(text)
        output=""
        if isPalindrome:
            output="It is palindrome"
        else:
            output="Not a palindrome"
        label = Label(top, text=output).pack()

btn=Button(root,text="PRESS TO CONTINUE",font=100,command=open).pack()
root.mainloop()