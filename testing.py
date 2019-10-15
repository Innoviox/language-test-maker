from pickle       import dump, load
from log          import log
from json.decoder import JSONDecodeError
from functools    import partial
from googletrans  import Translator
from duolingo     import Duolingo
from tqdm         import tqdm

def take_input(inmsg, valid, trans=lambda s:s):
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

try:
    word_map = load(open("word_map_save.txt", "rb"))
    log.debug("Loaded word map from file")
    words = list(filter(lambda i: i["word_string"] not in word_map, words))
except Exception as e:
    log.warning(f"No save found, reinitializing with errors: {e}")
    word_map = {}
    
log.debug(f"Loading {len(words)} new words")

for w in tqdm(words):
    word, strength = w["word_string"], w["strength"]
    try:
        word_map[word] = (t.translate(word, src=src_lang, dest=dest_lang).text, strength)
    except JSONDecodeError as e:
        log.error(f"Translate error: {e}, for word: {word}")
        log.debug(f"This could be because of quota limits. Stop running?")
        if stop_input() == "s": break
    except KeyboardInterrupt as k:
        if stop_input() == "s": break
    # log.debug(f"Translated {w} as {word_map[w]}")

log.debug("Saving word_map to file")
dump(word_map, open("word_map_save.txt", "wb"))
