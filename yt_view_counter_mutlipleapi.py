import os
import google_auth_oauthlib.flow #pip install google-auth-oauthlib
import googleapiclient.discovery #pip install google-api-python-client
import googleapiclient.errors
import pprint
from time import sleep

#initialize permissions
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def create_api_list(infile):
    api_list = [];
    with open(infile, "r") as reader:
        for line in reader:
            api_list.append(line.strip('\n').strip('\r'));
    return api_list;

#to displau data
pp = pprint.PrettyPrinter(indent=2)
def main():
    #setup
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"

    api_list = create_api_list("api_files.txt");
    print(api_list);
    youtube = [];
    for client_secrets_file in api_list:
        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube.append(googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials))

    count = 0;
    curr_api = 0;
    while(True): 
        curr_api = curr_api + 1 if curr_api < len(api_list)-1 else 0;

        # Request (This is what asks Youtube API for the video data)
        try:
            request = youtube[curr_api].videos().list(
                part="snippet,statistics",
                id="X4xtZv5nFIk"
            )
            response = request.execute()

            data = response["items"][0];
            vid_snippet = data["snippet"];

            title = vid_snippet["title"];

            views = str(data["statistics"]["viewCount"]);
            
            print("");
            print("Title of Video: " + title);
            print("Number of Views: " + views);

            change = (views not in title);

            if(change):
                title_upd = "How This Video Has " + format(int(views), ",d") + " Views, Explained";
                vid_snippet["title"] = title_upd;

                request = youtube[curr_api].videos().update(
                    part="snippet",
                    body={
                        "id": "X4xtZv5nFIk",
                        "snippet": vid_snippet
                    }
                )
                response = request.execute()
                
                print("Worked!" + str(count));
                sleep(475 / len(api_list));
            count += 1;
            
            
        except:
            print("Error, trying again");

        count += 1;
        sleep(44 / len(api_list));
        
        
#run program
if __name__ == "__main__":
    main()