import spacy
import spacy_cleaner
from spacy_cleaner.processing import removers, replacers, mutators

# Load model
nlp = spacy.load("en_core_web_sm")
# nlp = spacy.load("fr_core_news_sm")

# Treat text
text = "Hello World"
doc = nlp(text)

# Remove stopwords
stopwords = nlp.Defaults.stop_words