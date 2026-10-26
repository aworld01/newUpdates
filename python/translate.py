# Stored translations (you can expand this)
#sentence_map = {
#    "I have a cat": "मेरे पास एक बिल्ली है",
#    "I have a dog": "मेरे पास एक कुत्ता है"
#}

# Word-level translations
#word_map = {
#    "I": "मैं",
#    "have": "पास",
#    "a": "एक",
#    "cat": "बिल्ली",
#    "dog": "कुत्ता",
#    "car": "गाड़ी"
#}

#def translate(sentence):
#    # 1. Check full-sentence translation
#    if sentence in sentence_map:
#        return sentence_map[sentence]

#    # 2. Word-by-word fallback
#    words = sentence.split()
#    translated_words = []

#    for w in words:
#        if w in word_map:
#            translated_words.append(word_map[w])
#        else:
#            translated_words.append(w)  # keep unknown word as-is

#    # 3. Reconstruct Hindi structure (simple example)
#    # English: I have a X
#    # Hindi: मेरे पास एक X है
#    if words[:3] == ["I", "have", "a"]:
#        obj = translated_words[3]
#        return f"मेरे पास एक {obj} है"

#    # Default fallback
#    return " ".join(translated_words)


# TESTS
#print(translate("I have a cat"))  # full translation
#print(translate("I have a new car"))  # partial translation






# Full sentence translations
sentence_map = {
    "I have a cat": "मेरे पास एक बिल्ली है"    
}

# Word-level translations
word_map = {
    "I": "मैं",
    "have": "पास",
    "a": "एक",
    "new": "नया",
    "very": "बहुत",
    "old": "पुरानी",
    "red": "लाल",
    "cat": "बिल्ली",
    "dog": "कुत्ता"
}

def translate(sentence):
    # 1. Full sentence match
    if sentence in sentence_map:
        return sentence_map[sentence]

    words = sentence.split()

    # 2. Pattern: I have a <object phrase>
    if len(words) >= 4 and words[:3] == ["I", "have", "a"]:
        object_words = words[3:]  # everything after "a"

        translated_obj = []
        for w in object_words:
            translated_obj.append(word_map.get(w, w))  # fallback to original

        object_phrase = " ".join(translated_obj)
        return f"मेरे पास एक {object_phrase} है"

    # 3. Default fallback (word-by-word)
    translated = [word_map.get(w, w) for w in words]
    return " ".join(translated)
    
    
print(translate("I have a cat"))
print(translate("I have a dog"))
print(translate("I have a new car"))
print(translate("I have a very old red car"))

print(translate("My name is Abdul Zoha"))