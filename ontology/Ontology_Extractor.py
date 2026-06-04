import spacy
from collections import Counter
from ontology.stop_phrases import STOP_PHRASES


class PhraseExtractor:

    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

    def clean_phrase(self, phrase):

        phrase = phrase.lower().strip()

        return phrase

    def is_valid_phrase(self, phrase):

        if phrase in STOP_PHRASES:
            return False

        if len(phrase) < 4:
            return False

        if phrase.isnumeric():
            return False

        return True

    def extract_phrases(self, text):

        doc = self.nlp(text)

        phrases = []

        for chunk in doc.noun_chunks:

            phrase = self.clean_phrase(chunk.text)

            if self.is_valid_phrase(phrase):

                phrases.append(phrase)

        return Counter(phrases)