import sqlite3
import vlc
import time
from mutagen.mp3 import MP3
path = "C:\\Users\\ww\\Desktop\\Desktop\\songs\\"

# ==================================== PlayList  ==========================================

class Playlist:
    def add_playlist(self, name, desc, tracks=0):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''INSERT INTO playlists(name,desc,tracks)VALUES(?,?,?) '''
        params = (name, desc, tracks)
        cur.execute(sql, params)
        con.commit()
        print("Playlist Added Successfully")
        con.close()

    def add_to_playlist(self, pID,sID):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''INSERT INTO playlist_song (playlistID,songID)VALUES(?,?) '''
        params = (pID,sID)
        cur.execute(sql, params)
        con.commit()

        cur1 = con.cursor()
        sql = "UPDATE  playlists set tracks = tracks +1 where ID="+pID
        cur1.execute(sql)
        con.commit()
        print("Song Added to Playlist  Successfully")
        con.close()

    def remove_from_playlist(self, pID,sID):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''DELETE from playlist_song where songID='''+str(sID)
        cur.execute(sql)
        con.commit()

        cur1 = con.cursor()
        sql = "UPDATE  playlists set tracks = tracks -1 where ID=" + pID
        cur1.execute(sql)
        con.commit()

        print("Song removed from Playlist  Successfully")
        con.close()


    def delete_laylist(self, id):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''DELETE from playlists where ID=''' + str(id)
        cur.execute(sql)
        cur1 = con.cursor()
        sql1 = '''DELETE from playlist_song where playlistID=''' + str(id)
        cur1.execute(sql1)
        con.commit()
        print("Playlist deleted Successfully")
        con.close()

    def view_playlist(self,pID):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()

        cur1 = con.cursor()
        res1 = cur1.execute('select name ,desc from playlists where ID = ?', (pID,))
        if res1!="":
            # to print name and desc of the playlist
            for x in res1:
                print(x[0],"\n",x[1],"\n")

        songsID = cur.execute('select songID from playlist_song where playlistID = ?', (pID,))
        #list_song.playlistID=?', (pID,))

        # to print all songs in the playlist
        #res = cur.execute("SELECT songs.name ,songs.length FROM songs INNER JOIN playlist_song ON songs.ID = playlist_song.playlistID WHERE playlistID = " + str(pID))
        cur2 = con.cursor()
        for row in songsID:
            res = cur2.execute('SELECT name , length FROM songs where ID ='+str(row[0]))
            for r in res:
                print(r[0],"\t\t Duration :",r[1],"\n")
        con.close()

    def all_playlist(self):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = ''' select ID ,name ,tracks from playlists'''
        cur.execute(sql)
        print("--------------------  All PlayLists  ----------------------")
        for row in cur:
            print(row[0], ".", row[1], "\t\t\tTracks:", row[2])
        print()
        con.close()

#  ===================================   Song    ======================================

class Song:
    def add_Song(self,name, band, artists, releaseDate, genres, lyrics, length):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = ''' INSERT INTO songs(name,band,artists,releaseDate,genres,lyrics,length) 
        VALUES(?,?,?,?,?,?,?) '''
        params = (name, band, artists, releaseDate, genres, lyrics, length)
        cur.execute(sql, params)
        con.commit()
        print("Song Added Successfully")
        con.close()

    def get_song(self,id):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''select name from songs where ID=''' + str(id)
        result = cur.execute(sql)
        n=""
        for row in result:
            n = row[0]
        con.close()
        return n

    def view_song(self,id):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''select* from songs where ID=''' + str(id)
        cur.execute(sql)
        print()
        for row in cur:
            print("ID   : ",row[0])
            print("name : ", row[1])
            print("Band : ", row[2])
            print("Artists : " ,row[3])
            print("Release Date :", row[4])
            print("Genres  :", row[5])
            print("Lyrics  :",row[6])
            print("Length  : ",row[7])
        con.close()

    def delete_song(self, id):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''DELETE from song where ID=''' + str(id)
        cur.execute(sql)
        con.commit()
        print("Song deleted Successfully")
        con.close()

    def play_song(self, path1):
        sound_file = vlc.MediaPlayer(path1)
        sound_file.play()
        time.sleep(30)
        sound_file.stop()

    def get_duration(selt , path2):
        audio = MP3(path2)
        time = audio.info.length
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        duration = str(int(minutes)) + ":" + str(int(seconds))
        return duration

# =================================  Album =====================================================

class Album:

    def add_album(self,title , band_name, tracks=0):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''INSERT INTO albums(title ,band_name ,tracks)VALUES(?,?,?) '''
        params = (title, band_name, tracks)
        cur.execute(sql, params)
        con.commit()
        print("Album Added Successfully")
        con.close()

    def delete_album(self, id):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''DELETE from albums where ID=''' + str(id)
        cur.execute(sql)
        con.commit()
        print("Album deleted Successfully")
        con.close()

    def all_album(self):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = ''' select ID ,title ,band_name ,tracks from albums'''
        cur.execute(sql)
        print("ID   title    \t\t\tBand\t\tTracks")
        for row in cur:
            print(row[0],"\t",row[1],  "\t\t",row[2] ,"\t\tTracks:", row[3])
        print()
        con.close()

    def add_to_album(self, aID,sID):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''INSERT INTO album_song (albumID,songID)VALUES(?,?) '''
        params = (aID,sID)
        cur.execute(sql, params)
        con.commit()

        cur1 = con.cursor()
        sql = "UPDATE  albums set tracks = tracks +1 where ID="+aID
        cur1.execute(sql)
        con.commit()
        print("Song Added to Album  Successfully")
        con.close()

    def remove_from_albumt(self, pID,sID):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = '''DELETE from album_song where songID='''+str(sID)
        cur.execute(sql)
        con.commit()

        cur1 = con.cursor()
        sql = "UPDATE  albums set tracks = tracks -1 where ID=" + pID
        cur1.execute(sql)
        con.commit()

        print("Song Added to Album  Successfully")
        con.close()

    def view_album(self,aID):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()

        cur1 = con.cursor()
        res1 = cur1.execute('select title , band_name from albums where ID = ?', (aID,))
        if res1!="":
            # to print title and band of the album
            print("-------------- << Album's Songs>>  ---------------")
            for x in res1:
                print(x[0],"\n",x[1])

        songsID = cur.execute('select songID from album_song where albumID = ?', (aID,))
        # to print all songs in the playlist
        cur2 = con.cursor()
        for row in songsID:
            res = cur2.execute('SELECT name , length FROM songs where ID ='+str(row[0]))
            for r in res:
                print(r[0],"\t\t Duration :",r[1])
        con.close()

    def play_album_songs(self, id):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = ''' select songID from album_song where albumID=''' +str(id)
        songIDs = cur.execute(sql)
        for ID in songIDs:
            s_name = s.get_song(ID[0])
            print("------- " + s_name + " is playing -----------")
            p = path + s_name + ".mp3"
            s.play_song(p)
        con.close()

#  ============================== Artist ===================================

class Artist:
    def show_artist(self):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = ''' select ID , name from artists'''
        cur.execute(sql)
        print("---------------------- List of Albums --------------------------\n")
        for row in cur:
            print(row[0],row[1])
        con.commit()
        con.close()

    def add_artist(self, name , DOB=""):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = ''' INSERT INTO artists(name,DOB)  VALUES(?,?) '''
        params = (name, DOB)
        cur.execute(sql, params)
        con.commit()
        print("Artist Added Successfully")
        con.close()

    def delete_artist(self, id):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = ''' DELETE from artists where ID ='''+ str(id)
        cur.execute(sql)
        con.commit()
        print("Artist deleted Successfully")
        con.close()
    def play_artist_song(self,artist):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        result1 = cur.execute('SELECT name FROM songs WHERE artists = ?', (artist,))
        if result1 != "":
            print("---- << Songs of " +artist + " >>  ------")
        for row in result1:
            print("\n------------- << " + row[0] + " >> is playing -------------------\n")
            pa = path + row[0] + ".mp3"
            s.play_song(pa)
        con.close()

    def all_artist(self):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = ''' select ID ,name from artists'''
        cur.execute(sql)
        print("--------------------  All Artists  ------------------")
        print("ID   Name")
        for row in cur:
            print(row[0],"\t",row[1])
        print()
        con.close()


class Library:
    def play_playlist_songs(self,id):
        con = sqlite3.connect('musicly.db')
        songIDs = con.cursor()
        song = con.cursor()
        sql = ''' select songID from playlist_song where playlistID=''' + str(id)
        songIDs.execute(sql)

        for ID in songIDs:
            name = s.get_song(ID[0])
            print("------- " + name + " is playing -----------")
            p = path + name + ".mp3"
            s.play_song(p)
        con.close()

    def play_band_song(self,band):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        result = cur.execute('SELECT name FROM songs WHERE band = ?', (band,))
        if result!="":
            print("----------- << Songs of " + band + " >>  -------------")
        for row in result:
            p = path + row[0] + ".mp3"
            print("---------- << " + row[0] + " >> is playing ------------\n")
            s.play_song(p)
        con.close()

    def play_song(self,id):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        sql = ''' select name from songs where ID=''' + str(id)
        cur.execute(sql)
        for row in cur:
            p = path + row[0] + ".mp3"
            print("------------- << " + row[0] + " >> is playing -------------------\n")
            s.play_song(p)
        con.close()

    def play_all_song(self):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        result1 = cur.execute('SELECT name FROM songs')
        if result1 != "":
            print("-------------- << Play All Songs >>  -------------------")
        for row in result1:
            print("------------- << " + row[0] + " >> is playing -------------------\n")
            pa = path + row[0] + ".mp3"
            s.play_song(pa)
        con.close()

    def view_all_song(self):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        result1 = cur.execute('SELECT* FROM songs')
        if result1 != "":
            print("-------------- << All Songs >>  -------------------")
            print("ID   name        Band       Artists      Genres     Length")

        for row in result1:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[5],"\t",row[7])
        con.close()

    def add_song(self):
        name = input("Enter name of the song :")
        band = input("Enter band name :")
        artist = input("Enter artist name :")
        rDate = input("Enter release Date :")
        genres = input("Enter category of the song :")
        lyrics = input("Enter lyrics :")
        p1 = path + name + ".mp3"
        leng = s.get_duration(p1)
        s.add_Song(name,band,artist,rDate,genres,lyrics,leng)
        # if artist is new then add it to the list
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        result = cur.execute('SELECT * FROM artists WHERE name = ?', (artist,))
        print(result)
        for row in result:
            if row[1] != artist:
                ar.add_artist(artist, "")
            else:
                print("Artist is exist")
        con.commit()
        con.close()

    def add_song_to_playlist(self,pID , sID ):
        con = sqlite3.connect('musicly.db')
        cur = con.cursor()
        res1 = cur.execute('SELECT ID , tracks FROM playlists WHERE name = ?', (pID,))
        res2 = cur.execute('SELECT ID FROM songs WHERE name = ?', (sID,))
        con.close()
        if res1 != "" and res2 != "":
            p.add_to_playlist(pID,sID)


# ==============================   Musicly   ======================================================

class Musicly:
    def playlist(self):
        while True:
            print("-------------------- << PlayList >>   ----------------------\n")
            p.all_playlist()
            print("1.View playlist \n2.Add Playlist \n3.Delete Playlist")
            print("4.Play PlayList's Songs \n5.Add Song to Playlist")
            print("6.Remove Song From Playlist \n7.Back to Home")
            n = int(input())
            if n == 1:
                pID = input("Enter ID of the playlist : ")
                p.view_playlist(pID)
            elif n == 2:
                name = input("Enter name of the playlist : ")
                desc = input("Enter description of the playlist : ")
                p.add_playlist(name,desc)
            elif n == 3:
                id = int(input("Enter ID of the playlist to delete : "))
                p.delete_laylist(id)
            elif n == 4:
                id = input("Enter plyList ID : ")
                l.play_playlist_songs(id)
            elif n == 5:
                pID = input("Enter ID of the playlist : ")
                sID = input("Enter ID of the song : ")
                l.add_song_to_playlist(pID , sID)
            elif n == 6:
                pID = input("Enter ID of the playlist : ")
                sID = input("Enter ID of the song : ")
                p.remove_from_playlist(pID, sID)
            elif n == 7:
                m.home()
            else:
                print("wrong choice")

    def artist(self):
        while True:
            print(" -------------------  << Artist >> --------------------- ")
            ar.all_artist()
            print("1.View Artist \n2.Add Artist \n3.Delete Artist \n4.Play Artist's Songs \n5.Back to Home")
            n = int(input())
            if n == 1:
                ar.show_artist()
            elif n == 2:
                name = input("Enter name of the artist : ")
                dob = input("Enter DOB of the artist DD-MM-YY : ")
                ar.add_artist(name,dob)
            elif n == 3:
                id = int(input("Enter ID of the artist to delete : "))
                ar.delete_artist(id)
            elif n == 4:
                art = input("Enter artist name: ")
                ar.play_artist_song(art)
            elif n==5:
                m.home()
            else:
                print("wrong choice")

    def album(self):
        while True:
            print("-------------------- << Album >>   ----------------------")
            a.all_album()
            print("1.View Album   \n2.Add Song to Album \n3.Add Album")
            print("4.Delete Album \n5.play Album Songs  \n6.Back to Home")
            n = int(input())
            if n == 1:
                id = input("Enter ID of the album : ")
                a.view_album(id)
            elif n == 2:
                aID = input("Enter ID of the album : ")
                sID = input("Enter ID of the song : ")
                a.add_to_album(aID,sID)
            elif n == 3:
                title = input("Enter title of the album : ")
                b_name = input("Enter band name of the album : ")
                a.add_album(title,b_name)
            elif n == 4:
                id = int(input("Enter ID of the album to delete : "))
                a.delete_album(id)
            elif n == 5:
                id = input("Enter ID of the album : ")
                a.play_album_songs(id)
            elif n == 6:
                m.home()
            else:
                print("wrong choice")

    def library(self):
        while True:
            print("-------------------- << Library >>   ----------------------")
            print("1.View Song          | 2.Play song         | 3.Add song")
            print("4.Play Band's Songs  | 5.Play All Song     | 6.View All Song \n7.Back to Home")
            n = int(input())
            if n == 1:
                id = input("Enter ID of the song : ")
                s.view_song(id)
            elif n == 2:
                id = input("Enter ID of the song : ")
                l.play_song(id)
            elif n == 3:
                l.add_song()
            elif n == 4:
                id = input("Enter name of the band  : ")
                l.play_band_song(id)
            elif n == 5:
                l.play_all_song()
            elif n == 6:
                l.view_all_song()
            elif n == 7:
                m.home()
            else:
                print("wrong choice")

    def home(self):
        while True:
            print("-------------------------- Home ------------------------")
            print("1.PlayLists \n2.Artists \n3.Albums \n4.Library \n5.Exit")
            n = int(input())
            if n == 1:
                m.playlist()
            elif n == 2:
                m.artist()
            elif n == 3:
                m.album()
            elif n == 4:
                m.library()
            elif n == 5:
                break
            else:
                print("wrong choice")
        return "-------------------------- Program End ------------------------"

m = Musicly()
l = Library()
a = Album()
ar = Artist()
s = Song()
p = Playlist()
print(m.home())
