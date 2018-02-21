from gevent import Greenlet

class BroadcastGreenlet(Greenlet):
    def __init__(self, converter, websocket):
        super().__init__()
        self.converter = converter
        self.websocket = websocket

    def _run(self):
        try:
            print('Reading into a buffer')
            while True:
                buf = self.converter.stdout.read(512)
                if buf:
                    self.websocket.send(buf)
                elif self.converter.poll() is not None:
                    break
        finally:
            print('Closing converter')
            self.converter.stdout.close()