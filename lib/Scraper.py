import requests

# Web scraper class that scraping the html string from given URL.
class Scraper:

    def __init__(self, urlString):

        # URL for scraping information.
        self.url = urlString

        # URL connection
        self.conn = None

        # html string that contains information.
        self.htmlString = None

    # Get the http(https) connection from given url string.
    def getConnection(self):
        try:
            self.conn = requests.get(self.url)
        except requests.exceptions.ConnectionError:
            print("There is no page in " + self.url)

    # Get the html string of connected url page and return it.
    # If there is no connection for url, print message and return None.
    # So, getConnection function has to be called first before this function called.
    def getHtmlString(self):
        try:
            self.htmlString = self.conn.text
        except AttributeError:
            print("There is no connection for url. Cannot retrieve the html string.")
        else:
            return self.htmlString


if __name__ == "__main__":
    print("This is not a valid executable.")
