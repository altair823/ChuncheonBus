import requests


# Web scraper class that scraping the html string from given URL.
class Scraper:

    def __init__(self, url_string=None):

        # URL for scraping information.
        self.url = url_string

        try:
            # URL connection.
            self.conn = requests.get(self.url, verify=False, timeout=10)
            if self.conn.status_code != 200:
                raise requests.exceptions.ConnectionError
        except requests.exceptions.ConnectionError:
            print("There is no connection for url. Cannot retrieve the html string.")
            self.conn = None
        except requests.exceptions.MissingSchema:
            print("Invalid URL! Please check URL string")
            self.conn = None

        # html string that contains information.
        try:
            self.htmlString = self.conn.text
        except AttributeError:
            print("Cannot retrieve html string from URL!")
            raise requests.exceptions.InvalidURL

    # Get the html string of connected url page and return it.
    # If there is no connection for url, print message and return None.
    def get_html_string(self):
        return self.htmlString

    # Get response header.
    def get_header(self):
        return self.conn.headers


if __name__ == "__main__":
    print("This is not a valid executable.")
