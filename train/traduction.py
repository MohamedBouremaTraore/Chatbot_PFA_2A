import googletrans
from googletrans  import Translator
translator = Translator()

def trad_input(text) :
    result = translator.translate(text,src='fr',dest='en')
    return result.pronunciation

def trad_output(text) :
    ans = ""
    text = text.split(".")
    for t in text :
        if t :
             res = translator.translate(t,src='en',dest='fr')
             ans = ans + str(res.pronunciation)
    return ans

#print(trad_output("Hello .how is it .going"))