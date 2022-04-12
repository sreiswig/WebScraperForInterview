from WebScraper import WebScraper

def web_scraper_worker(url):
    scraper = WebScraper()
    try:
        scraper.scrape_url(url)
        scraper.save()
        return True
    except Exception as e:
        return False

def word_query_worker(word):
    scraper = WebScraper()
    try:
        return scraper.query_results_file(word)
    except Exception as e:
        return "An error occurred: " + str(e)