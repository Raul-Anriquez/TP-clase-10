class Spotify:
    def play(self):
        print("Reproduciendo música")


class SpotifyAdapter:
    def __init__(self, spotify):
        self.spotify = spotify

    def reproducir(self):
        self.spotify.play()


spotify = Spotify()

adaptador = SpotifyAdapter(spotify)

adaptador.reproducir()
