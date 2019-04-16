from bs4 import BeautifulSoup, Comment

TAGS_BLACKLIST = ['noscript', 'script', 'style',
                  'input', 'textarea', 'iframe', 'footer', 'form']


def extract(to_remove):
    for element in to_remove:
        element.extract()


def remove_tags(soup):
    for tag_name in TAGS_BLACKLIST:
        tag_elements = soup.findAll(tag_name)
        extract(tag_elements)


def remove_comments(soup):
    comment_elements = soup.findAll(
        text=lambda text: isinstance(text, Comment))
    extract(comment_elements)


def get_text(html):
    soup = BeautifulSoup(html, 'lxml')
    remove_tags(soup)
    remove_comments(soup)
    text = soup.get_text(" ")
    return " ".join(text.split())
