class SocketIOHandlers:
    def __init__(self, sio):
        self.sio = sio

    def register_handlers(self):
        @self.sio.event
        def message(sid, data):
            print('Message from {}: {}'.format(sid, data))
            self.sio.send('Hello from the server!')

        @self.sio.event
        def connect(sid, environ):
            print('Client connected: {}'.format(sid))
            self.sio.send(f'Welcome! {environ}')

        @self.sio.event
        def disconnect(sid):
            print('Client disconnected: {}'.format(sid))
