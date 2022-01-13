import functools
import time



def request(func):
    """
        The request decorator avoid code duplication and force each request to be 
        executed after 1 sec. 
        Every failed requests will return None
    """
    @functools.wraps(func)
    def wrapper_request(*args, **kwargs):
        # wait 
        time.sleep(1.5)

        value = func(*args, **kwargs)
        response, endpoint = value["response"], value["endpoint"]
        content = response.json() 

        if response.status_code != 200:
            msg = content["status"]["message"]
            print(f"WARNING : request {endpoint} failed with status {response.status_code}")
            print(f"WARNING : request failed because : {msg}")
            return None
        return content

    return wrapper_request
