import socketio

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='sockets'
)

clients_connected=dict()
@sio_server.event
async def connect(sid, environ, auth):
    print(f'{sid}: connected')
    
    await sio_server.emit('join', {'sid': sid})
    sio_server.enter_room(sid,sid)

@sio_server.event
async def chat(sid, message):
    
    await sio_server.emit('chat', {'sid': sid, 'message': message},room=sid)


@sio_server.event
async def disconnect(sid):
    print(f'{sid}: disconnected')
    #remove the session
    sio_server.leave_room(sid, sid)
    
    
