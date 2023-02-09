#importing and reading the movie.xml file 

import xml.etree.ElementTree as ET
tree = ET.parse('movie.xml')
root = tree.getroot()


#using iter() to print all the movies 
for movie in root.iter('movie'):
    print(movie.attrib)


#using itertext() to get the movie descriptions    
for description in root.iter('description'):
    print("".join(description.itertext()))

#using movie.get to get the value of the attribute 'favorite'
count = 0
for movie in root.iter('movie'):
    favorite = movie.get('favorite')
    if favorite == 'True':
        count+=1
print(f"There are {count} favorite movies in the movie.xml file")
   

