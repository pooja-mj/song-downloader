from youtube_search import YoutubeSearch

search_key = input("Enter the search term: ")

results = YoutubeSearch(search_key, max_results=1).to_json()

print(results)