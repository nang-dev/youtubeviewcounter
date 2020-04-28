import os
import google_auth_oauthlib.flow #pip install google-auth-oauthlib
import googleapiclient.discovery #pip install google-api-python-client
import googleapiclient.errors
import pprint
from time import sleep

#initialize permissions
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

#to displau data
pp = pprint.PrettyPrinter(indent=1)

def main():
    #setup
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secret1.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    count = 0;
    while(True):
        # Request (This is what asks Youtube API for the comment data)
        request = youtube.commentThreads().list(
            part="snippet",
            videoId="X4xtZv5nFIk"
        )
        response = request.execute()

        comment_data = response["items"][0];
        comment_snippet = comment_data["snippet"]["topLevelComment"]["snippet"];

        comment_text = comment_snippet["textOriginal"];
        comment_username = comment_snippet["authorDisplayName"];

        #Make sure it's under 300 characters and format
        buffer = 25; #length of the hard-coded text i.e. "Most Recent Comment"
        comment_username = comment_username[:min(len(comment_username), 30)];
        max_length = 100 - (buffer + len(comment_username));
        comment_text = comment_text[:min(len(comment_text), max_length)];

        #Update title
        title_upd = "Your Comment: \"" + comment_username + "\" -"  + comment_text;

        # Request (This is what asks Youtube API for the video data)
        request = youtube.videos().list(
            part="snippet,statistics",
            id="5qYZC56dneU"
        )
        response = request.execute()
        data = response["items"][0];
        vid_snippet = data["snippet"];
        curr_title = vid_snippet["title"];

        if(curr_title != title_upd):
            vid_snippet["title"] = title_upd; #Max 300 Characters

            request = youtube.videos().update(
                part="snippet",
                body={
                    "id": "5qYZC56dneU",
                    "snippet": vid_snippet
                }
            )
            response = request.execute()

            print("Worked!" + str(count));

        count += 1;
        sleep(5);

#run program
if __name__ == "__main__":
    main()