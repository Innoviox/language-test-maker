from pickle          import dump, load
from json.decoder    import JSONDecodeError
from functools       import partial
from time            import sleep
from urllib.parse    import quote
from collections     import defaultdict
from os.path         import exists
from os              import mkdir
from random          import sample
from googletrans     import Translator
from duolingo        import Duolingo
from tqdm            import tqdm
from spacy.tokenizer import Tokenizer
from spacy.lang.en   import English
from selenium        import webdriver
from gtts            import gTTS
from playsound       import playsound
from unidecode       import unidecode
from log             import log

AUDIO_PATH = "audio/{}/{}.mp3"

def take_input(inmsg, valid, trans=lambda s:s[0].lower()):
    while True:
        s = input(inmsg)
        if s:
            s = trans(s)
            if (not valid) or s in valid:
                return s

stop_input = partial(take_input, "[s]top (any key to continue): ", [], lambda s: s[0].lower())

t = Translator()
try:
    d = load(open("duolingo_save.txt", "rb"))
    log.debug("Loading duo from file")
except Exception as e:
    log.warning(f"No save found, reinitializing with errors: {e}")
    
    u, p = open("duolingo_info.txt")
    d = Duolingo(u.strip(), password=p.strip())
    
    log.debug("Saving Duo to file")
    dump(d, open("duolingo_save.txt", "wb"))

info = d.get_user_info()
_src_lang, dest_lang = info["learning_language_string"], info["ui_language"]
src_lang = d.get_language_details(_src_lang)['language'] # _src_lang is full name, convert to abbreviation

log.debug("Loading words")
words = d.get_vocabulary(language_abbr=src_lang)
words = words["vocab_overview"]

def duolingo_translate(word, sl=src_lang, tl=dest_lang): # All translate methods must accept word, sl (source lang), and tl (trans/dest lang)
    # note that target/src are switched for some reason in the duo API
    w = d.get_translations([quote(word)], target=sl, source=tl)
    if w[word]:
        return w[word][0]
    wt = word.title()
    w = d.get_translations([quote(wt)], target=sl, source=tl) # fix for german nouns
    if w[wt]:
        return w[wt][0]
        # log.error(f"Translate error: {w}, {word}")

translate = google_translate = lambda word, sl=src_lang, tl=dest_lang: t.translate(word, src=sl, dest=tl).text
translate = duolingo_translate

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('./chromedriver', options=options)

def headless_translate(word, sl=src_lang, tl=dest_lang):
    driver.get(f"https://translate.google.com/#view=home&op=translate&sl={sl}&tl={tl}&text={quote(word)}")
    
    s = ""
    while not s:
        sleep(0.2)
        try:
            s = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span")
        except:
            pass
    return s.text

try:
    word_map = load(open("word_map_save.txt", "rb"))
    log.debug("Loaded word map from file")
    words = list(filter(lambda i: all(i["word_string"] not in j for j in word_map.values()), words))
except Exception as e:
    log.warning(f"No save found, reinitializing with errors: {e}")
    word_map = defaultdict(dict)

def load_words():
    for w in tqdm(words):
        word, strength = w["word_string"], w["strength"]
        try:
            tw = translate(word)
            if tw:
                word_map[w["pos"]][word] = (tw, strength, w["skill"])
            else:
                log.error(f"No translation found for {word}, trying headless")
                tw = driver_translate(word)
                word_map[w["pos"]][word] = (tw, strength, w["skill"])
            sleep(0.2)
        except JSONDecodeError as e:
            log.error(f"Translate error: {e}, for word: {word}")
            log.debug(f"This could be because of quota limits. Stop running?")
            s = take_input("[s]top, [c]hange to duolingo-translator: ", "sc")
            if s == "s": break
            else:
                translate = duolingo_translate
            # if stop_input() == "s": break
        except KeyboardInterrupt as k:
            if stop_input() == "s": break
        except Exception as e:
            log.error(f"Critical error: {e}")
            break

if words:
    log.debug(f"Loading {len(words)} new words")
    load_words()
    
    log.debug("Saving word_map to file")
    dump(word_map, open("word_map_save.txt", "wb"))

log.debug("Initializing tokenizer")
nlp = English()
tokenizer = Tokenizer(nlp.vocab)

def _ensure_audio_file(word, lang=src_lang):
    f = AUDIO_PATH.format(lang, unidecode(word))
    if not exists(f):
        if not exists(f"audio/{lang}/"): mkdir(f"audio/{lang}/")
        with open(f, "wb") as file:
            gTTS(word, lang=lang).write_to_fp(file)
    return f

def sentence_to_audio(sent, lang=src_lang, _i=0):
    for token in tokenizer(sent): # tqdm(tokenizer(sent)):
        playsound(_ensure_audio_file(str(token), lang=lang))

def gen_words(types=list(word_map.keys()), n=10):
    all_words = {}
    for t in types:
        all_words.update(word_map[t])
    return sample(all_words.items(), n)
        
# sentence_to_audio("Ich bin ein Mann")
translate_sentence = headless_translate # Wrapper method
