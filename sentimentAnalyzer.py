# Analyzes sentiments of inputted text
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os

class sentimentAnalyzer:

    def __init__(self):
        self.client = language.LanguageServiceClient()

    def analyzeText(self,input_text):

        document = types.Document(
            content=input_text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = self.client.analyze_sentiment(document=document).document_sentiment

        return [sentiment.score, sentiment.magnitude]