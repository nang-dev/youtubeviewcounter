import os
import google_auth_oauthlib.flow #pip install --user google-auth-oauthlib
import googleapiclient.discovery #pip install --user google-api-python-client
import googleapiclient.errors
import pprint

#initialize permissions
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

#to displau data
pp = pprint.PrettyPrinter(indent=4)


def main():
    #setup
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_883634937018-euknjgkgq1vk98mtr0djoqgk359oivvp.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # Request (This is what asks Youtube API for the video data)
    request = youtube.videos().list(
        part="snippet,statistics",
        id="5qYZC56dneU"
    )
    response = request.execute()

    data = response["items"][0];
    vid_snippet = data["snippet"];

    title = vid_snippet["title"];

    views = str(data["statistics"]["viewCount"]);

#run program
if __name__ == "__main__":
    main()