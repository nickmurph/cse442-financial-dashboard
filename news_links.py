from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key= '692f7d1a9a4743918f99bc95c73a28ed')

class news_articles:
    def __init__(self, title, url):
        self.title = title
        self.url = url

# headlines = newsapi.get_everything(q = 'apple',
#                                         sources = 'bloomberg',
#                                         language = 'en',
#                                         sort_by = 'relevancy',
#                                         page = 1)

# results = []
# desc = []
# articles = headlines['articles']
# for ar in articles:
#     results.append(ar["title"])
#     desc.append(ar["description"])

# for i in range(len(results)):
#     print(i + 1, results[i])
#     print(desc[i])

def get_news(topic):
    news = newsapi.get_everything(q = topic, sources= 'bloomberg,fortune,the-wall-street-journal,techcrunch,the-verge,cbs-news,abc-news,financial-post,cnbc,wired,business-insider,bbc-news,associated-press, australian-financial-review, hacker-news ', sort_by="relevancy", language='en', page = 1)
    news_list = []
    articles = news['articles']
    for ar in articles:
        news_list.append(news_articles(ar['title'],ar['url']))
    return news_list

# list = get_news('apple')
# for i in range(len(list)):
#     print (i + 1, list[i].title)
#     print (list[i].url, '\n')