
#defining the class Album
class Album:
    
    #initialising the variables needed for the album class
    def __init__(self,albumName, numberofSongs, albumArtist):
        self.albumName = albumName 
        self.numberofSongs = numberofSongs 
        self.albumArtist = albumArtist 
    
    #defining a method that will print the information of an album 
    def __str__(self):
        print(f"{self.albumName} by {self.albumArtist}, {self.numberofSongs} tracks")



#making a list that contains a 5 album objects    
albums1 = [(Album("Aethiopes", 13, "billy woods")),(Album("Haram", 14, "Armand Hammer,The Alchemist")),
(Album("Wasteland",19, "Brent Faiyaz")),(Album("Too late to Die Young", 5,"Sonder")),
(Album("Pray for Haiti",16,"Mach Hommy"))]


#calling the print method to show each album on a new line 
for albums in albums1:
    albums.__str__()
    

#creating an empty list to appned the number of songs to the list
tracks = []
for albums in albums1:
    tracks.append(albums.numberofSongs)
print("\n")

#sorting the numbers from smallest to largest 
tracks.sort()


#a nested for loop that will check if the album object has the same number of 
#tracks as list item of tracks, if it does, then the album is placed at the index
#of its corresponding track number
for albums in albums1:
    for x in range(len(tracks)):
        if albums.numberofSongs == tracks[x]:
            tracks[x] = albums

#printing the ordered list 
print("\nOrdered Albums by Numbers of Tracks:")
for album in tracks:
    album.__str__()


#switching the first and second albums around             
for x in range(len(tracks)):    
    first_album = tracks[0]

    tracks[0] = tracks[1]
    tracks[1] = first_album
    
print("\nSwitching Album1 and Album2:")
for album in tracks:
    album.__str__()
 
#defining another list of albums 
albums2 = [(Album("Hatian Body Odor (H.B.O)",18,"Mach Hommy")),(Album("Hiding Places",12,"billy woods")),
            (Album("I Told Bessie",13,"E L U C I D")),
            (Album("Honor Killed The Samurai",10,"Ka")),(Album("Apollo XXI",12,"Steve Lacy"))]

#appending the first list of albums to the second 
for album in albums1:
    albums2.append(album)
    

#defining two more albums and adding them to the album list 
new1 = Album("Dark Side of the Moon",9, "Pink Floyd" )
new2 = Album("Oops!... I Did It Again",16, "Britney Spears" )

albums2.append(new1)
albums2.append(new2)

#defining an empty list to add the names of the albums 
first_letter = []


for album in albums2:
    first_letter.append(album.albumName)

    
#sorting the names alphabetically 
print("\nSorting Alphabetically:")
first_letter.sort()




for album in albums2:
    y = albums2.index(album)
    
    #a nested for loop that will replace list  ordered by album names with the 
    # corresponding album object
    for x in range(len(first_letter)):
        if first_letter[x] == album.albumName and album not in first_letter:
            first_letter[x] = album

#printing the new ordered album list            
for album in first_letter:
    album.__str__()


#finding a specific album by searching for its name
print("\nFinding Dark Side of The Moon")
name = "Dark Side"
for album in first_letter:
   
    if album.albumName.find(name) != -1:
        album.__str__()


            
    
        
    