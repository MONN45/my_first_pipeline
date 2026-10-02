# Make PAI call serive temperory failure

import random
import time

import requests

Retryable_status_codes = {429,500, 502, 503, 504}

def get_with_retry(url ,params = None, max_attempts =4):
    ''''Geta URL and return the josn response , stop om perenantly retryable status codes or max attempts reached
    '''

    for attempt in range(1, max_attempts + 1):
        try :
            response = requests.get(url, params=params, timeout=10)

        except requests.exceptions.RequestException as error:
            reason =f"Network errror: {error}"

        else:
            if response.status_code in Retryable_status_codes:
                reason = f"Retryable status code: {response.status_code}"

            if response.status_code < 400:
                return response.json()
            reason = f"HTTP error: {response.status_code}"

        if attempt < max_attempts:
            wait_time = 2 ** attempt + random.uniform(0, 1)
            print(f"Attempt {attempt} failed: {reason}. Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)
    