# Youtube View Updater / Comment Updater

## How to Use

### Step 1: 
Get setup with the Youtube API: https://developers.google.com/youtube/v3/quickstart/python \
        Be sure to follow it carefully, as it won't work if you don't do every step. \
### Step 2: 
Save the Google Oauth Client File from Step 1 into a file named "secret.json" \
### Step 3: 
[Download](https://github.com/nang149/youtubeviewcounter.git) code from Github and  \
	- Replace client_secrets_file with your new "secret.json" \
 	- Replace the id's with the id of the video you want to edit \
### Step 4:
	Run the program (yt_view_counter.py for view counter, yt_comment_vid.py for comment updater) by using command
	```
	python yt_view_counter.py
	'''
### Step 5: 
The Youtube API will give you a link to get authenticated. Go to this link, and if you get "Website is not secure", just hit "Advanced" and keep going to get your authentication code.
### Step 6: It should work now!
	