# Higher level abstract module that handling html string.
# Extract meaningful strings from html string that scraped by scraper module.

# Factory that construct StringExtractor.
def get_extractor(html_string=None):
    return StringExtractor(html_string)


class StringExtractor:

    # Constructor
    def __init__(self, html_string=None):
        if html_string is None:
            raise AttributeError("There is no html String!")
        self.total_html_string = html_string
        self.target_start = None
        self.target_end = None

    # Set target starting string.
    def set_start_target(self, target_string):
        if target_string == "":
            print("Target string for finding is empty!")
            print("Please check the string to find.")
            exit(1)
            # In temporary, absence of target string cause abort program.
            # But for making flexible program, there should be re-inputting the target.
        self.target_start = target_string

    # Set target ending string.
    def set_end_target(self, target_string):
        if target_string == "":
            print("Target string for finding is empty!")
            print("Please check the string to find.")
            exit(1)
        self.target_end = target_string

    # Find index of target string in html string.
    # And store all found index to found_line_set, return it.
    def find_string(self):
        found_line_set = list()
        index = 0
        while True:
            index = self.total_html_string.find(self.target_start, index)
            if index == -1:
                break
            index += len(self.target_start)
            first_index = index
            index = self.total_html_string.find(self.target_end, index)
            last_index = index
            found_line_set.append((first_index, last_index))
            print(index)
            index = last_index+1

        return found_line_set
