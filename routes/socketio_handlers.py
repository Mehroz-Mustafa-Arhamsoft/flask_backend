# from flask_socketio import SocketIO, emit
# from flask_socketio import SocketIO, emit

def register_socketio_handlers(sio):
    @sio.event
    def message(sid, data):
        print('Message from {}: {}'.format(sid, data))
        sio.send('Hello from the server!')

    @sio.event
    def connect(sid, environ):
        print('Client connected: {}'.format(sid))
        sio.send('Welcome!')

    @sio.event
    def disconnect(sid):
        print('Client disconnected: {}'.format(sid))

    # @socketio.on('connect')
    # def handle_connect():
    #     print('Client connected')
    #     emit('response', {'message': 'Connected to server'})

    # @socketio.on('disconnect')
    # def handle_disconnect():
    #     print('Client disconnected')

    # @socketio.on('trigger_test')
    # def handle_trigger_test(data):
    #     # Handle trigger test event
    #     # You can call the function from your Flask route here
    #     emit('response', {'message': 'Test triggered', 'data': data})
