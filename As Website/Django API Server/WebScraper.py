import requests
import string
import json
import logging

import nltk
from nltk import word_tokenize
from bs4 import BeautifulSoup


class WebScraper():
    """
    A class to scrape a set of websites and return a dictionary of words and their frequency

    '''
    Attributes:
    -----------
    __results: dict
        A dictionary of words and their frequency, stores the results of the last scrape
    __logger: logging.Logger
        A logger to log errors and debug information

    Methods:
    --------
    scrape_url(url, curr_depth=0, max_depth=2):
        Scrapes a url and all of its links up to a certain depth, results are stored in the __results attribute
    extract_words(text):
        Cleans and extracts words from a string of text
    is_hyphenated_word(word):
        Helper function that checks if a hyphenated word is valid
    save(filename="result.json", destination="filesystem"):
        Saves the results of the last scrape to a file as a json object
    clear_results():
        Clears the results of the last scrape
    query_results(word):
        Returns the results of the last scrape for a given word
    """
    __results = dict()
    __logger = logging.getLogger('webscraper_logger')
    
    def __init__(self):
        fh = logging.FileHandler('webscraper.log')
        self.__logger.addHandler(fh)
        self.__logger.propagate = False
        
    def scrape_url(self, url):
        try:
            self.__results = dict()
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            links = []
            for link in soup.find_all('a'):
                links.append(link.get('href'))
            words = self.extract_words(soup.get_text())
            
            for word in words:
                self.__results[word] = self.__results.get(word)
                if (self.__results.get(word) == None):
                    self.__results[word] = {"count": 1, "urls": [url]}
                else:
                    self.__results[word]["count"] += 1
                    if (url not in self.__results[word]["urls"]):
                        self.__results[word]["urls"].append(url)
            
            for link in links:
                self.__scrape_worker(link)
            
        except ValueError as e:
            self.__logger.error(e)
    
    def __scrape_worker(self, url):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            words = self.extract_words(soup.get_text())
            for word in words:
                self.__results[word] = self.__results.get(word)
                if (self.__results.get(word) == None):
                    self.__results[word] = {"count": 1, "urls": [url]}
                else:
                    self.__results[word]["count"] += 1
                    if (url not in self.__results[word]["urls"]):
                        self.__results[word]["urls"].append(url)
        
        except ValueError as e:
            self.__logger.error(e)
                
    def extract_words(self, text):
        words = []
        
        for word in word_tokenize(text):
            if (word not in string.punctuation):
                if (self.is_hyphenated_word(word) or word.isalpha()):
                    words.append(word.lower())
        
        return words
    
    def is_hyphenated_word(self, word):
        is_word = True
        splits = word.split("-")
        for split in splits:
            if (not split.isalpha()):
                is_word = False
        return is_word
    
    def save(self, filename="result.json", destination="filesystem"):
        if (destination == "filesystem"):
            with open(filename, "w") as outfile:
                json.dump(self.__results, outfile)
        
    def clear_results(self):
        self.__results = dict()
    
    def query_results(self, word):
        return self.__results.get(word.lower(), "Word was not found in scrape: " + word)

    def query_results_file(self, word):
        try:
            with open("result.json", "r") as infile:
                results = json.load(infile)
                infile.close()
            return results.get(word.lower(), "Word was not found in scrape: " + word)
        except ValueError as e:
            self.__logger.error(e)
            return "An Error Occurred while querying the results file"