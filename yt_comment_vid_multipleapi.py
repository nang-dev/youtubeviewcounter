import os
import google_auth_oauthlib.flow #pip install google-auth-oauthlib
import googleapiclient.discovery #pip install google-api-python-client
import googleapiclient.errors
import pprint
from time import sleep
from profanity_check import predict, predict_prob

#initialize permissions
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

#to displau data
pp = pprint.PrettyPrinter(indent=1)

def create_api_list(infile):
    api_list = [];
    with open(infile, "r") as reader:
        for line in reader:
            api_list.append(line.strip('\n'));
    return api_list;

def main():
    #setup
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"

    api_list = create_api_list("api_files.txt");

    youtube = [];
    for client_secrets_file in api_list:
        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube.append(googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials));

    count = 0;
    curr_api = 0;
    while(True):
        # Request (This is what asks Youtube API for the video data)
        request = youtube[curr_api].commentThreads().list(
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
        comment_username = comment_username[:min(len(comment_username), 20)];
        max_length = 100 - (buffer + len(comment_username));
        comment_text = comment_text[:min(len(comment_text), max_length)];
        
        inappro = predict([comment_text]);
        if inappro:
            continue; # Don't update title if comment is inappropriate 

        #Update title
        title_upd = "Your Comment: " + comment_text + " -"  + comment_username + str(count);
        try:
            # Request (This is what asks Youtube API for the video data)
            request = youtube[curr_api].videos().list(
                part="snippet,statistics",
                id="5qYZC56dneU"
            )
            response = request.execute()
            data = response["items"][0];
            vid_snippet = data["snippet"];
            curr_title = vid_snippet["title"];

            if(curr_title != title_upd):
                vid_snippet["title"] = title_upd; #Max 300 Characters

                request = youtube[curr_api].videos().update(
                    part="snippet",
                    body={
                        "id": "5qYZC56dneU",
                        "snippet": vid_snippet
                    }
                )
                response = request.execute()

            print("Worked!" + str(count));
            sleep(int(501 / len(api_list)));
        except:
            print("except" + str(count));

        curr_api = curr_api + 1 if curr_api < len(api_list)-1 else 0;
        count += 1;
        

#run program
if __name__ == "__main__":
    main()