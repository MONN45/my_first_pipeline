
import requests
from http_utils import get_with_retry

url  = "https://jsonplaceholder.typicode.com/posts"


def get_posts( page_size =25 ,max_post = 100):
    '''Fetch every post one page at atime and store them in the list all_posts'''
    try:
        start  = 0
        all_posts = []
        
        for page_number in range(start, max_post+1):
            params = {"_start" :start ,"_limit" : page_size}

            page = get_with_retry(url, params=params)
           

            #page = response.json()

            #print(len(page))
            # print(page)
            if page is None:
                print(f"Failed to fetch page {page_number}. Stopping further requests.")
                break

            print("*****************")
            all_posts.extend(page)

            if len(page) < page_size:
                return all_posts

            start += page_size

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching posts: {e}")
        return

if __name__ == "__main__":

    posts = get_posts()
    if posts:
        print(f"Total posts fetched: {len(posts)}")
        print(f"First post: {posts[0]}")
