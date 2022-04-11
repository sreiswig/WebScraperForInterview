from WebScraper import WebScraper

ws = WebScraper()
url = input("Enter a URL: ")
ws.scrape_url(url=url)
is_working = True
while is_working:
    user_input = input("Commands: query , exit, help, save \n")
    if user_input == "query":
        query = input("Enter a query: ")
        print(ws.query_results(query))
    elif user_input == "exit":
        is_working = False
    elif user_input == "help":
        print("query: Query the web scrape for a chosen word \n Returns count of the word and the urls associated with it")
        print("exit: exits the program")
        print("help: prints this message")
        print("save: saves the current web scrape to a file as json")
    elif user_input == "save":
        file = input("Enter a file name or nothing for results.json: ")
        if file == "":
            ws.save()
        else:
            ws.save(file)

print("Exiting... bye!")
