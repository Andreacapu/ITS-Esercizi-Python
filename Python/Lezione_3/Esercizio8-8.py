#inizializzazione definizione
def make_album(artista, album = None):
    album_info = {"artista": artista, "album": album}
    return album_info
while True:#inizializzazione ciclo while for
        print("\nPrego inserire l'artista e l'album. digitare stop per interrompere il processo:  ")
        artista_input = input("artista: ")
        if artista_input.lower() == "stop":
            break

        album_input = input("album: ")
        if album_input.lower() == "stop":
            break

        album_info = make_album (artista_input, album_input)
        print(album_info)