import requests
import sys

for small in sys.stdin:
    wordlist = small.strip()
    if not wordlist:
        continue
    print(wordlist)
    response = requests.get(url=f"http://94.237.57.211:40253/{small}")
    
    try:
        if response.status_code != 404:
            content_type = response.headers.get("Content-Type" or "").lower()
            print(response)    
            print("Content-Type", content_type)
            print(" Length :", len(response.content))
            
            if "json" in content_type:
                try :
                    print(response.json())
                except ValueError:
                    print(response.text)  
            else:
                print(response.text)     
    
    except Exception as e:
        print(wordlist, "request error",e)
        



