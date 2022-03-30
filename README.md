# Terminal Music Player 
This is a terminal python project to learn the basics of os.sys calls and also work with other apps like mpv and packages like youtube dl and youtube search.

# This project works on 
This project currently only works on linux.
This has not been tested on MacOS. since it is a plain python file, it should run with mpv

It uses mpv as the media player

Ability to run it on windows(using some other media player more natively supported) will be added in the near future after all wishful upgrades are in place.

<hr>

# Dependencies
### 1. [mpv](https://mpv.io/)
#### Arch Linux
```sh
sudo pacman -Syu mpv
```
#### Ubuntu/Debian
```sh
sudo apt install mpv
```

### 2. [Youtubedl](https://github.com/ytdl-org/youtube-dl)
```sh
pip3 install youtube-dl
```

### 3. [Youtube_search](https://pypi.org/project/youtube-search/)
```sh
pip3 install youtube_search
```
<hr>

## Current Things that work
1. playing a local mp3 song (one song only)
2. playing a song by pulling it from youtube (one song only)
3. playing a playlist generated from youtube searches, very feature-less at the moment, will update more

<hr>

##  Working on
1. Playing multiple local files in one folder
2. Making a good looking TUI
3. Adding lyrics for songs 
4. Playing a youtube playlist ----> (adding new features)
5. PLaying a user created playlist
6. Adding Keybind configuration for users ease
7. Adding mobile support
8. Adding muliplayer/ listen with friends mode

## NOTE
**please** note that this is a project to practice what i've learnt in python. You could just use mpv from the command-line directly instead of running this py file. **THIS IS A JUST A PRACTICE PROJECT**
