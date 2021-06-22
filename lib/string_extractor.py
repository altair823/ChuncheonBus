# Higher level abstract module that handling html string.
# Extract meaningful strings from html string that scraped by scraper module.

def get_extractor(html_string):
    return StringExtractor(html_string)


class StringExtractor:

    def __init__(self, html_string):
        self.total_html_string = html_string
        self.target = None

    def set_target(self, target_string):
        if target_string == "":
            print("Target string for finding is empty!")
            print("Please check the string to find.")
            exit(1)
            # In temporary, absence of target string cause abort program.
            # But for making flexible program, there should be re-inputting the target.
        self.target = target_string

    def find_string(self):
        found_line_set = set()
        found_index = 0
        while found_index < len(self.total_html_string):
            found_index = self.total_html_string.find(self.target, found_index)
            while self.total_html_string[found_index] != "\n":
                found_index -= 1
            found_index += 1
            found_line_set.add(found_index)
            print(found_index)
            found_index += len(self.target)

        return found_line_set
