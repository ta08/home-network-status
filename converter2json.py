import re
import sys
import json
from datetime import datetime
import pytz

import requests

if __name__ == '__main__':
    
    if(len(sys.argv) == 1):
        print('set index name')
        exit;
    
    index_name = sys.argv[1].strip()
    url = "http://127.0.0.1:9200/{}/ping".format(index_name)
    
    
    for txt in iter(sys.stdin.readline, ""):
        payload = {}
        
        now_timestamp = datetime.now().timestamp()
        tz = pytz.timezone("Japan")
        created_time = datetime.fromtimestamp(now_timestamp, tz).isoformat()
        
        payload['createdAt'] = created_time
        
        time_matcher = re.search("time=(\d+(\.\d*)?|\.\d+)", txt)        
        if time_matcher:    
            payload['pingTime'] =  float(time_matcher.group(1))
            payload['canConnect2Endpoint'] = 1
            #print("time=", time_matcher.group(1),txt )
        elif "timeout" in txt:
            payload['canConnect2Endpoint'] = 0
            #print('ooooops', txt)            
        #print('dump json')
        else:
            continue
        
        with requests.post(
                url,
                json.dumps(payload, separators=(',', ':')), 
                headers = {'Content-Type': 'application/json'}) as response:
        
            print(response.status_code, payload)
        
        
        
        #sys.stdout.flush()
    
    print('ennnnnnd')

