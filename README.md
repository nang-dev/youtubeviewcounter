# Youtube View Updater / Comment Updater
Using the Youtube API and Python to update view count on Youtube video to: \
Achieve the "This Video Has X Views" Title \
Enable video's title to be the most recent comment \
and More!

## How to Use

### Step 1: 
Get setup with the Youtube API: https://developers.google.com/youtube/v3/quickstart/python \
Be sure to follow it carefully, as it won't work if you don't do this part right. 
### Step 2: 
Save the Google Oauth Client File from Step 1 into a file named "secret.json" 
### Step 3: 
[Download](https://github.com/nathan-149/youtubeviewcounter.git) code from Github and in the program you want to run (yt_view_counter.py for view counter, yt_comment_vid.py for comment updater) \
* Replace client_secrets_file with your new "secret.json" 
* Replace the id's with the id of the video you want to edit 

### Step 4: Setup
Setup pip on Windows: https://www.liquidweb.com/kb/install-pip-windows/  \
In terminal / command line, run the program with
```
pip install google-auth-oauthlib
pip install google-api-python-client
```

### Step 5: Run
In terminal / command line, run the program with
```
python yt_view_counter.py
```
### Step 6: 
The Youtube API will give you a link to get authenticated. Go to this link, and if you get "Website is not secure", just hit "Advanced" and keep going to get your authentication code.
### Step 7: It should work now!
	
