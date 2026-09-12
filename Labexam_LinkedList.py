
class MusicPlayer():
    def __init__(self, ID, title, artist, duration):

        self._song_id = ID
        self._song_title = title
        self._song_artist = artist
        self._song_duration = duration 


    def __str__(self):
        return f"[Song ID:{self._song_id}] | Song Title:{self._song_title} | Artist:{self._song_artist} | Duration:({self._song_duration} Minutes)"
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size 

    def displaysong(self):

        print("=" * 50)
        print(f"{'MUSIC PLAYLIST MANAGER':^50}")
        print("=" * 50)


        if self._head is None:
            print(f"{'!No songs added!':^50}")
            return
        
        current = self._head
        pos = 1 
        while current is not None:
            print(f"{pos} {current.data}")
            current = current.next
            pos += 1

    def display_list(self):
        print(f"{'=DISPLAY PLAYLIST SIZE=':^50}")
        if self._head is None:
            print(f"{'!No songs added!':^50}")
            return


        current = self._head

        while current is not None:
            print(f"[{current.data._song_title}]", end = " => ")
            current = current.next
        print("NULL")
       


    def input_song(self):
        print(f"{'ADDING SONG...':^50}")
        ID = input("ENTER SONG ID:")
        title = input("ENTER SONG TITLE:").upper()
        artist = input("ENTER SONG ARTIST:").upper()
        duration = int(input("ENTER SONG DURATION:"))
        return MusicPlayer(ID, title, artist, duration)
        

    def search (self, key):
        if self._head is None:
            print(f"No created playlists for '{key}")
            return False
        
        current = self._head
        pos = 1
        while current is not None:
            if current.data._song_id == key:
                print(f"song found position in queue {pos}:\nTitle:{current.data._song_title} by {current.data._song_artist}")
                return True
            current = current.next
            pos += 1
        print(f"No results for '{key}")
        return False
    
    def insert_front(self, data):

        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

        print("Song Playing Now")
        
    def insert_end(self, data):

        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._size += 1
            print("\nSong added; Playing now")
            return
        current = self._head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self._size += 1
        print("Song added to play last")

    def insert_pos(self, data, pos):
        if pos < 1 or pos > self._size + 1:
            print("Song not found")
            return

        if pos == 1:
            self.insert_front(data)
            return
        
        new_node = Node(data)
        current = self._head
        if pos == 0:
            new_node.next = self._head
            self._head= new_node
            return
        for i in range (1, pos - 1):
            current = current.next 
        new_node.next = current.next
        current.next = new_node
        self._size += 1

        print(f"Song is placed at position:{pos}")


    def delete_node(self, song_id):
        if self._head is None:
            print("No created playlists")
            return 

        if self._head.data._song_id == song_id:
            song_title = self._head.data._song_title
            self._head = self._head.next
            self._size -= 1 
            print(f"Song:'{song_title}' was removed")
            return

        current = self._head

        while ( 
            current.next is not None and current.next.data._song_id != song_id
        ):
            
            current = current.next

        if current.next is not None:
            song_title = current.next.data._song_title
            current.next = current.next.next
            self._size -= 1
            print(f"Song ID '{song_id}' removed successfully.")
        else:
            print(f"Song ID '{song_id}' not found.")

       


def main_menu():
    Playlist = LList()

    menu_text = ''' select application:
    1.Music Playlist Manager
    '''
    array_text = '''
1.Add song at the beginning
2.Adds song at the End
3.Insert Song at a Position
4.Display Song
5.Search Song
6.Remove Song
7.Display Playlist size
8.Exit 
'''

    while True:
        print("=" * 50)
        print(f"{'APPLICATIONS':^50}")
        print("=" * 50)
        menu = input(menu_text + "\nEnter choice: ")

        match menu:

            case '1':

                while True:
                    print("=" * 50)
                    print(f"{'MUSIC PLAYLIST MANAGER':^50}")
                    print("=" * 50)
                    menu_array = input(array_text + "\nEnter choice: ")
                    print("\033c", end="\033[A")

                    match menu_array:
                        case '1':
                            Playlist.displaysong()
                            song = Playlist.input_song()
                            Playlist.insert_front(song)
                            test = input("\nPress ENTER to continue")
                        case '2':
                            Playlist.displaysong()
                            song = Playlist.input_song()
                            Playlist.insert_end(song)                                              
                            test = input("\nPress ENTER to continue")
                        case '3':
                            Playlist.displaysong()
                            song = Playlist.input_song()
                            try:
                                pos = int(input("ENTER POSITION: "))
                                Playlist.insert_pos(song, pos)
                            except ValueError:
                                print("Invalid position input!")
                            test = input("\nPress ENTER to continue")
                        case '4':
                            print(f"{'SONG DISPLAY':^50}")
                            Playlist.displaysong()
                            test = input("\nPress ENTER to continue")
                        case '5':
                            key = input("ENTER SONG ID TO SEARCH: ")
                            Playlist.search(key)
                            test = input("\nPress ENTER to continue")
                        case '6':
                            Playlist.displaysong()
                            key = input("ENTER SONG ID TO REMOVE: ")
                            Playlist.delete_node(key)
                            test = input("\nPress ENTER to continue")
                        case '7':
                            Playlist.display_list()
                            print(f"\nTotal songs in playlist: {len(Playlist)}")
                            test = input("\nPress ENTER to continue")
                        case '8':
                            print("Returning to Main Menu...")
                            break
                        case _:
                            print("Invalid choice!")



if __name__ == "__main__":
    main_menu()