from threading import Timer
import datetime
from urllib.request import urlopen


class UpdatedURL:
    def __init__(self, url):
        self.url = url
        self.contents = ""
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

    def __getstate__(self):
        new_state = self.__dict__.copy()
        if "timer" in new_state:
            del new_state["timer"]
        return new_state

    def __setstate__(self, data):
        self.__dict__ = data
        self.schedule()
