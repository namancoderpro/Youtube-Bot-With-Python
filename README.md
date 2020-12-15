# Youtube Bot With Python
A Youtube Bot built with Python (Selenium), it automates the Login, Watch, Like, and subscribe processes. 

![](https://i.ibb.co/ZhYWcK3/Pink-and-Purple-Sporty-Gradient-Fitness-You-Tube-Thumbnail.png)
```
usage: youtubeBot.py [-h] --accounts ACCOUNTS [--videos VIDEOS] [--channels CHANNELS] [--like [LIKE]]

                     --subscribe [SUBSCRIBE]] [--watch [WATCH]

A Youtube Bot Built With Python | It does: Watching, Liking videos & Subscribing to channnels.

optional arguments:

  -h, --help            show this help message and exit
  
  --accounts ACCOUNTS   A txt file that holds the gmail accont(s) | [xxxx@gmail.com:password]
  
  --videos VIDEOS       A txt file that holds a list of Youtube videos. | [link|length]
  
  --channels CHANNELS   A txt file that holds a list of channel(s) links.
  
  --like [LIKE]         To like the videos in the list.
  
  --subscribe [SUBSCRIBE]    To subscribe to the channels in the list.
                        
  --watch [WATCH]       To watch the videos in the list.
```
---
### Examples:

- To only subscribe to a list of Youtube channels: *python youtubeBot.py --accounts accounts.txt --channels channels.txt --subscribe *

- To only watch video: *python youtubeBot.py --accounts accounts.txt --videos videos.txt --watch*

- To only watch & like the video: *python youtubeBot.py --accounts accounts.txt --videos videos.txt --watch --like*

- To subscribe to a list of Youtube channels & watch and like a list of videos: *python youtubeBot.py --accounts accounts.txt --channels channels.txt --subscribe  --videos videos.txt --watch --like*

## Tutorial On Youtube:
[Watch Here]()
