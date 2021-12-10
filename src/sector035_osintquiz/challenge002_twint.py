import hashlib
import twint

c = twint.Config()
c.Search = "puzzle"
c.Username = "sector035"
c.Since = "2017-12-01"
c.Until = "2017-12-31"
c.Images = True
c.Pandas = True

tweet = twint.run.Search(c)
Tweets_df = twint.storage.panda.Tweets_df
photo_url = Tweets_df['photos'].to_string(index=False).replace('[','').replace(']','')
photo_id = ".".join(photo_url.split('/media/')[-1].split('.')[0:-1])
hash_object = hashlib.md5(photo_id.encode()).hexdigest()
print(hash_object)
