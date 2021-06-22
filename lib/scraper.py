import requests


# Web scraper class that scraping the html string from given URL.
class Scraper:

    def __init__(self, url_string):

        if url_string == "":
            raise #raise exception

        # URL for scraping information.
        self.url = url_string

        try:
            # URL connection
            self.conn = requests.get(self.url)
        except AttributeError:
            print("There is no connection for url. Cannot retrieve the html string.")
            self.conn = None

        # html string that contains information.
        self.htmlString = self.conn.text

    # Get the http(https) connection from given url string.
    def _get_connection(self):
        try:
            return requests.get(self.url)
        except requests.exceptions.ConnectionError:
            print("There is no page in " + self.url)

    # Get the html string of connected url page and return it.
    # If there is no connection for url, print message and return None.
    def get_html_string(self):
        return self.htmlString

    # Get response header.
    def get_header(self):
        return self.conn.headers

if __name__ == "__main__":
    print("This is not a valid executable.")
