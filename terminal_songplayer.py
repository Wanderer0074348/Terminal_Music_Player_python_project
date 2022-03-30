import os
from venv import create
from youtube_search import YoutubeSearch
import time


def song_from_internet(give_search_results=False, number_of_outputs=2):
    user_searches = input("enter your song: \n")
    results = YoutubeSearch(
        user_searches, max_results=number_of_outputs).to_dict()
    if give_search_results is False:
        print("--------------------------------------------------------------------")
        print("your song will start now!!, hit ctrl+c to stop the song from playing")
        print("--------------------------------------------------------------------")
        os.system(
            f"mpv https://youtube.com{results[0]['url_suffix']} --no-video")
    else:
        for i in range(len(results)):
            print(f"{i+1}. {results[i]['title']}")
            time.sleep(0.5)
        enter_which_audio = int(input("which audio would you like to play?"))
        if enter_which_audio <= number_of_outputs+1:
            os.system(
                f"mpv https://youtube.com{results[enter_which_audio-1]['url_suffix']} --no-video")
        else:
            print("We only searched what you asked for, please stay within search limits")


def play_one_song(song):
    print("--------------------------------------------------------------------")
    print("your song will start now!!, hit ctrl+c to stop the song from playing")
    print("--------------------------------------------------------------------")
    os.system(f"mpv {song}")


def play_mulitple_songs_from_the_internet():
    want_to_see_results = bool(input(
        "Do you want to see the search results from the internet? type anything for <yes> and hit enter for <no>: "))
    number_of_results = int(input(
        "How many results do you want to see?: ")) if want_to_see_results is True else 1+1
    

    def create_playlist():
        buffer_list = []
        while True:
            user_searches = input("enter your song: \n")    
            results = YoutubeSearch(user_searches, max_results=number_of_results).to_dict() 
            for i in range(len(results)):
                print(f"{i+1}. {results[i]['title']}")
                time.sleep(0.5)
            enter_which_audio = int(input("which audio would you like to insert? "))
            buffer_list.append(
                f"https://youtube.com{results[enter_which_audio-1]['url_suffix']}")
            print(buffer_list)
            more_songs = int(
                input("More song to input? type 1 for yes, type 2 for no: "))
            if more_songs == 1:
                continue
            else:
                break
        with open("playlistFolder/Playlist.txt", "a+") as playlist:
            for i in buffer_list:
                playlist.write("%s\n" % i)
        return buffer_list

    def play_the_song(textfile):
        os.system(f"mpv --playlist='playlistFolder/Playlist.txt' --no-video")

    play_the_song(create_playlist())


def main():
    while True:
        print("--------------------------------------------------------------------")
        userinp = int(input('''What would you like to do now?:
_____________
|          
|->  1. Play one song
|->  2. Play multiple songs
|->  3. Play from the internet
|->  4. Exit \n
--------------------------------------------------------------------
enter here: '''))
        if userinp == 1:
            song_path = input("please enter correct song path: ")
            play_one_song(song_path)
        elif userinp == 2:
            play_mulitple_songs_from_the_internet()
        elif userinp == 3:
            want_to_see_results = bool(input(
                "Do you want to see the search results from the internet? type anything for <yes> and hit enter for <no>: "))
            number_of_results = int(input(
                "How many results do you want to see?: ")) if want_to_see_results is True else 1+1
            song_from_internet(want_to_see_results, number_of_results)
        else:
            break


main()
