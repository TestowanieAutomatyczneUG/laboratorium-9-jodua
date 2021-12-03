from datetime import datetime


class Env:

    def getTime() -> str:
        return datetime.now()

    def playWavFile(self, file) -> None:
        pass
