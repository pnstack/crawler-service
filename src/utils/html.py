from bs4 import BeautifulSoup
import htmlmin

def clean_and_minify_html(html_string):
    # create BeautifulSoup object and parse HTML
    soup = BeautifulSoup(html_string, 'html.parser')

    # remove class attribute from all tags
    for tag in soup.find_all(True):
        tag.attrs = {attr: value for attr, value in tag.attrs.items() if attr != 'class'}

    # minify HTML using htmlmin library
    minified_html = htmlmin.minify(str(soup), remove_comments=True, remove_empty_space=True)

    return minified_html