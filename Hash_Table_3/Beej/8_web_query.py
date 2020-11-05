import urllib.request
import datetime

# Getting information from a url
# resp = urllib.request.urlopen("https://example.com/")
# data = resp.read()

# print(data)

# print(data.decode())

# Example
# edge cases if empty pass
# did it cache or not
# http can set time for cache but need to look it up
# alternative - time stamp

#create cacheentry class that records timestamp to avoid issues with tuples
class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()

cache = {}
CACHE_TIMEOUT_SECS = 10

while True:
    url = input("Enter a URL: ")

    if url == '':
        continue

    cur_time = datetime.datetime.now().timestamp()
    print(cur_time)

    if url not in cache or cur_time - cache[url].timestamp > CACHE_TIMEOUT_SECS:
        resp = urllib.request.urlopen(url)
        data = resp.read()
        cache[url] = CacheEntry(data)
        resp.close()
        print("CACHE MISS") # notifies you if this is not in cache
    else:
        print("CACHE HIT") # notifies you if website is already cached

    # print(cache[url].timestamp)
    print(cache[url].data[:75])
