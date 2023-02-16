
from __future__ import print_function
import time
from aylien_news_api.rest import ApiException
from pprint import pprint
from aylien_news_api import ApiClient, DefaultApi

# set up the API client
configuration = aylien_news_api.Configuration()
configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '10c284c4'
configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '217ae7d0e71bcbbb6f10d0aa495cca0a'

client = ApiClient(configuration)
api_instance = DefaultApi(client)

def get_articles():
    try:
        # call Aylien API
        stories = api_instance.list_stories(
            title="(Artificial AND Intelligence)",
            language=["en"],
            published_at_start="NOW-1DAY"
        )
        # print titles of returned articles
        for story in stories.stories:
            print(story.title)
    except ApiException as e:
        print(f"Error: {str(e)}")

get_articles()


# from __future__ import print_function
# import time
# import aylien_news_api
# from aylien_news_api.rest import ApiException
# from pprint import pprint

# configuration = aylien_news_api.Configuration()
# configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '10c284c4'
# configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '217ae7d0e71bcbbb6f10d0aa495cca0a'

# client = aylien_news_api.ApiClient(configuration)
# api_instance = aylien_news_api.DefaultApi(client)


# def get_articles():
#     try:
#         # set query parameters
#         query = {
#             "language": ["en"],
#             "title": "artificial AND intelligence"
#         }
#         # call Aylien API
#         stories = client.list_stories(**query)["stories"]
#         # print titles of returned articles
#         for story in stories:
#             print(story["title"])
#     except Exception as e:
#         print(f"Error: {str(e)}")

# get_articles()

# try:
#     filters = {
#         'title': "artificial AND intelligence",
#         'published_at_start': 'NOW-1DAY',
#         'published_at_end': 'NOW',
#         'language': ['en'],
#         'not_language': 'es',
#     }
#     api_response = api_instance.list_stories(**filters)
#     for story in api_response.stories:
#         print(story.title)
# except ApiException as e:
#     print("Exception when calling DefaultApi->list_stories: %s\n" % e)
