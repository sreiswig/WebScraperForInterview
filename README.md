# WebScraperForInterview
Requirements:
<ol>
	<li>Prompt user for one url.</li>
	<li>Scrape that url and all links found on the page for words and index them.</li>
		<ul>
			Index is defined as the number of times a word shows up on all the pages visited and the url of the pages it shows up on.
		</ul>
	<li>Prompt user for a word</li>
	<ul>
        Retreive the number of times a word shows up and at least a single url of a page it shows up on.
	</ul>
	<li> Develop as if under a time crunch think simplify </li>
	<li> No DB required should save results as JSON file </li>
	<li> Send link to the github around the start of next week </li>
</ol>

This program uses the nltk toolkit library https://www.nltk.org/ for processing of text. <br>
And BeautifulSoup4 https://www.crummy.com/software/BeautifulSoup/bs4/doc/ for parsing html.

The instructions for installing the nltk toolkit are: https://www.nltk.org/install.html <br>
NLTK requires python 3.7, 3.8, 3.9, or 3.10

The instructions for installing BeautifulSoup4 are found here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup <br>
Or just "pip install beautifulsoup4"

To use the program as a command line tool, navigate to 'As Command Line Program' and run the following command: <br>
python3 main.py

Enter the URL of the page you want to scrape and wait. <br>
A message will pop up asking if you want to query the scrape for a word, quit, or save to file. <br>

The program can also be used from the Jupyter Notebook

Work in progress: as a web application. <br>
Django webserver with a Flutter for web frontend. <br>