import configparser
import requests

config = configparser.ConfigParser()
config.read('twitter_api.creds')

bearer_token = config['DEFAULT']['bearer_token']


def create_url(id):
    tweet_fields = "tweet.fields=lang,author_id,created_at,attachments"
    media_fields = "media.fields=duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    ids = "ids=" + str(id)
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets?{}&expansions=attachments.media_keys&{}&{}".format(ids, tweet_fields,
                                                                                               media_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    headers = {
        "authorization": "Bearer " + bearer_token,
        "content-type": "application/json"
    }
    data = {
        "query": "from:Sector035 lang:en",
        "maxResults": "100",
        "fromDate": "201712010000",
        "toDate": "201712312359"
    }
    # You will have to change this to your dev environment label
    dev_environment_label = "dev"
    r = requests.post("https://api.twitter.com/1.1/tweets/search/fullarchive/" + dev_environment_label + ".json",
                      json=data, headers=headers)

    response = r.json()

    # What term should be searched for in the tweets
    search_term = "puzzle"
    for result in response['results']:
        if search_term in result['text']:
            url = create_url(result['id'])
            json_response = connect_to_endpoint(url)
            photo_url = json_response['includes']['media'][0]['url']
            # split the url so you only get the photo id
            photo_id = photo_url.split('media/')[1].split('.jpg')[0]
            print(photo_id)


if __name__ == "__main__":
    main()
