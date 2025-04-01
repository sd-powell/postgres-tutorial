from sqlalchemy import (
create_engine, Column, Integer, String, Float, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql://stevenpowell:stevenpowell@localhost:5432/chinook")
base = declarative_base()


# create a class-based model for the "artist" table
class Artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)
    
# create a class-based model for the "album" table
class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))
    

# create a class-based model for the "track" table
class Track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.album_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer)
    bytes = Column(Integer)
    unit_price = Column(Float)


# instead of connecting to the database directly, we create a session
# create a new instance of sessionmaker, then point to the engine
Session = sessionmaker(db)
# opens an actual session by calling the Session( subclass defined above
session = Session()

#creating the database using the declarative_base subclass
base.metadata.create_all(db)


# Query 1  - select all the records from the "artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.artist_id, artist.name, sep=" | ")


# Query 2 - select only the "name" column from the "artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.name)
    
    
# Query 3 - select only "Queen" from the "artist" table
# artist = session.query(Artist).filter(Artist.name == "Queen").first()
# print(artist.artist_id, artist.name, sep=" | ")


# Query 4 - select only by "artist_id" #51 from the "artist" table
# artist = session.query(Artist).filter(Artist.artist_id == 51).first()
# print(artist.artist_id, artist.name, sep=" | ")


# Query 5 - select only by "artist_id" #51 from the "album" table
# albums = session.query(Album).filter(Album.artist_id == 51)
# for album in albums:
#     print(album.album_id, album.title, album.artist_id, sep=" | ")
    

# Query 6 - select all tracks where the composer is "Queen" from the "track" table
track = session.query(Track).filter(Track.composer == "Queen")
for track in track:
    print(
        track.track_id, 
        track.name, 
        track.album_id, 
        track.media_type_id, 
        track.genre_id, 
        track.composer, 
        track.milliseconds, 
        track.bytes, 
        track.unit_price, 
        sep=" | "
        )