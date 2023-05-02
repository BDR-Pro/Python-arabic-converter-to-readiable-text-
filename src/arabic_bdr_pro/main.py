from bidi.algorithm import get_display # to display the arabic text
import arabic_reshaper # to display the arabic text

class arabic():
    def arabic(self,text): #function to get the arabic title
        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)           # correct its direction

    def print(self,text):
        print(self.arabic(text)) #function to print the arabic title