class Gepclass:
    def __init__(self,sor):
        self.id=int(sor[0])
        self.hely=(sor[1])
        self.tipus=sor[2]
        self.ipcim=sor[3]

    def __str__(self):
        return f"{self.id},{self.hely},{self.tipus},{self.ipcim}"