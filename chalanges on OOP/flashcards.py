class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+"-"+self.meaning
flash=[]
print("welcom to flashcard application")
while True:
    word=input("enter your word")
    meaning=input("enter the meaning of the word")
    flash.append(flashcard(word,meaning))
    break
print("your flashcards")
for i in flash:
    print(i)