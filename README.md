# terminal-bad-apple
I made a terminal representation of the song Bad Apple! This was a short project but it was really cool. I'm uploading this on GitHub so other people can view it and enjoy it!

# Setup
To install the dependencies, run: `pip install -r requirements.txt`

# Running
To run the actual thing, use `python3 play.py`
Note: you do need python 3 for this

If you want the audio (not frame dependent and can lose sync if the animation gets slow at some point), uncomment line 17 in `play.py`

# How?????
Basically, I converted the downloaded video (with `youtube-dl`) into individual frames (with `ffmpeg`) and converted those frames to ASCII art (which I *totally* didn't use any tutorial for (sarcasm)). I then played those frames in my terminal to create the animation!


# Play any other video
You download the video with `youtube-dl`, parse it into its individual frames with `ffmpeg`, then run `python3 converter.py`. This will render the images into ASCII art frames. Then, when it's done, run `python3 play.py` to view it. If you have audio and want to play it, download it separately and then edit line 17 on `play.py` to say `playsound('./YOUR_AUDIO_FILE_NAME+EXTENSION', block=False)`


Hope you enjoy this!
