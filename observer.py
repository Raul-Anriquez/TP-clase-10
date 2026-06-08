class Suscriptor:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, video):
        print(f"{self.nombre} recibió una notificación: {video}")


class Canal:
    def __init__(self):
        self.suscriptores = []

    def suscribir(self, usuario):
        self.suscriptores.append(usuario)

    def subir_video(self, video):
        print(f"Nuevo video: {video}")

        for usuario in self.suscriptores:
            usuario.actualizar(video)


canal = Canal()

u1 = Suscriptor("Marcos")
u2 = Suscriptor("Daniel")

canal.suscribir(u1)
canal.suscribir(u2)

canal.subir_video("Tutorial de Python")
