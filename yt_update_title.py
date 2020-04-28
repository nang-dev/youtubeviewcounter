import os
import google_auth_oauthlib.flow #pip install google-auth-oauthlib
import googleapiclient.discovery #pip install google-api-python-client
import googleapiclient.errors
import pprint

#initialize permissions
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

#to displau data
pp = pprint.PrettyPrinter(indent=4)

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

    # Request (This is what asks Youtube API for the comment data)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId="5qYZC56dneU"
    )
    response = request.execute();

    comment_data = response["items"][0];
    comment_snippet = comment_data["snippet"]["topLevelComment"]["snippet"];

    comment_text = comment_snippet["textOriginal"];
    comment_username = comment_snippet["authorDisplayName"];

    safe = predict(comment_text);
        if not safe:
            continue; # Don't update title if comment is not safe

    # Request (This is what asks Youtube API for the video data)
    request = youtube.videos().list(
        part="snippet,statistics",
        id="5qYZC56dneU"
    )
    response = request.execute();
    data = response["items"][0];
    vid_snippet = data["snippet"];
    curr_title = vid_snippet["title"];

    #Update title
    title_upd = "Your Comment: \"" + comment_text + "\" -"  + comment_username;

    if(curr_title != title_upd):
        vid_snippet["title"] = title_upd; #Max 300 Characters

        request = youtube.videos().update(
            part="snippet",
            body={
                "id": "5qYZC56dneU",
                "snippet": vid_snippet
            }
        )
        response = request.execute();


#run program
if __name__ == "__main__":
    main()

        
