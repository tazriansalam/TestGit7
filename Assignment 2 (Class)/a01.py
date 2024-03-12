class Vinyl:

    Album = ""
    Artist = ""
    Year = ""

def main():

    vinyl_instance = Vinyl()

    vinyl_instance.Album = "Abbey Road"
    vinyl_instance.Artist = "The Beatles"
    vinyl_instance.Year = 1969

    print("Album:", vinyl_instance.Album)
    print("Artist:", vinyl_instance.Artist)
    print("Year:", vinyl_instance.Year)