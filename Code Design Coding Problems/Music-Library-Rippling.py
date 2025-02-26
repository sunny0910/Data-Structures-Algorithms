'''
It was like design a Music Player analytics sort of service(in memory), that prints most played song.


void playSong(songId, userId);

void addSong(songId, title);

void printAnalytics();
I was able to code. Then they asked a follow up to add a feature to star/unstar song(s) for a user and get last N favourite songs played(something like that). 
I wasn't able to fully write the working code for it as time was up.
'''

import random
from collections import defaultdict, deque


class DllNode:
    def __init__(self, freq):
        self.songList = set()
        self.freq = freq

class TrendingSongs:
    def __init__(self):
        self.head = DllNode(None)
        self.tail = DllNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.songIdToNode = {}
    
    def incrementFreq(self, songId):
        if songId in self.songIdToNode:
            currNode = self.songIdToNode[songId]
            currNode.songList.remove(songId)
            
            if currNode.prev.freq == currNode.freq + 1:
                node = currNode.prev
            else:
                node = DllNode(currNode.freq + 1)
                node.next = currNode
                node.prev = currNode.prev
                currNode.prev.next = node
                currNode.prev = node
            
            node.songList.add(songId)
            self.songIdToNode[songId] = node
        else:
            if self.tail.prev.freq == 1:
                node = self.tail.prev
            else:
                node = DllNode(1)
                node.next = self.tail
                node.prev = self.tail.prev
                self.tail.prev.next = node
                self.tail.prev = node
            
            node.songList.add(songId)
            self.songIdToNode[songId] = node
    
    def listTrendingSongs(self):
        curr = self.head.next
        while curr.freq:
            print("{}: {}".format(curr.freq, curr.songList), end=", ")
            curr = curr.next
        print()
    
    def getTopSongs(self, n=10):
        output = []
        curr = self.head.next
        while curr.freq and len(output) < 10:
            output.extend(list(curr.songList))
            curr = curr.next
        
        return output[:n]

class MusicLibrary:
    def __init__(self):
        self.songLibrary = {}
        self.trendingSongs = TrendingSongs()
        self.userTrendingSongs = defaultdict(TrendingSongs)
        self.userFavoriteSongs = defaultdict(set)
        self.songHistory = defaultdict(deque)
    
    def playSong(self, songId, userId):
        if songId not in self.songLibrary:
            raise KeyError('{} not found'.format(songId))
        
        self.trendingSongs.incrementFreq(songId)
        # self.trendingSongs.listTrendingSongs()
        self.songHistory[userId].appendleft(songId)
        self.userTrendingSongs[userId].incrementFreq(songId)

    def addSong(self, songId, title):
        self.songLibrary[songId] = title
    
    def getTopSongs(self, n=2):
        return self.trendingSongs.getTopSongs(n)
    
    def getTopSongsForEachUser(self, n=2):
        userToTopSongs = {}
        for user, trendingDll in self.userTrendingSongs.items():
            topSongs = trendingDll.getTopSongs(n)
            userToTopSongs[user] = topSongs
        
        return userToTopSongs

    def addFavorite(self, songId, userId):
        self.userFavoriteSongs[userId].add(songId)
    
    def removeFavorite(self, songId, userId):
        self.userFavoriteSongs[userId].remove(songId)


ms = MusicLibrary()
songs = ['senorita', 'shazam', 'Jaan', 'Kasam', 'Pyaar', 'Dil', 'Baarat', 'APT', 'Espreosso']
for i, song in enumerate(songs):
    ms.addSong(i+1, song)

for i in range(20):
    songId = random.randint(1, len(songs))
    userID = random.randint(1,3)
    ms.playSong(songId, userID)
    print("Song with id: {}, title: {} played by User: {}".format(songId, songs[songId-1], userID))
    if i % 5 == 0:
        ms.trendingSongs.listTrendingSongs()
        # print(ms.getTopSongs(2))
        print(ms.getTopSongsForEachUser())