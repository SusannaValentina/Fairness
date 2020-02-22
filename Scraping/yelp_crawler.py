import requests
from lxml import html


def get_ranking(url):
    page_content = requests.get(url)
    tree = html.fromstring(page_content.content)

    recommended_reviews_text = "Recommended Reviews"
    reviews_list = tree.xpath('//section[div[div[h3[text()="%s"]]]]/div/div/ul/*' % recommended_reviews_text)
    print(reviews_list)

    # Index for ranking
    i = 1
    reviews_text = []
    reviews_date = []

    # TODO: in url start=x to scroll pages of the ranking
    for review in reviews_list:
        reviews_text.append((i, tree.xpath('//section[div[div[h3[text()="%s"]]]]/div/div/ul/li[%d]/div/div[last()]/div[p]/p/span' % (recommended_reviews_text, i))[0].text))
        reviews_date.append((i, tree.xpath('//section[div[div[h3[text()="%s"]]]]/div/div/ul/li[%d]/div/div[last()]/div[1]/div/div[2]/span' % (recommended_reviews_text, i))[0].text))
        i = i + 1

    print(reviews_text)
    print(reviews_date)
