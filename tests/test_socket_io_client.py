import os
import pytest
import socketio
from dotenv import load_dotenv

load_dotenv()
local_port = int(os.getenv('LOCAL_PORT', '8000'))
SERVER_URL = f"http://127.0.0.1:{local_port}"


@pytest.fixture(scope='module')
def socketio_client():
    client = socketio.Client()
    client.connect(SERVER_URL)
    yield client
    client.disconnect()


def test_socketio_connection(socketio_client):
    assert socketio_client.connected


def test_trigger_test_event(socketio_client):
    def message_handler(msg):
        assert msg['message'] == 'Test triggered'
        assert 'data' in msg

    socketio_client.on('response', message_handler)
    socketio_client.emit('trigger_test', {'test_type': 'portScan', 'target_ip': 'google.com', 'port_range': '1-1000'})


def test_connect_event(socketio_client):
    messages = []

    def message_handler(msg):
        messages.append(msg)

    socketio_client.on('response', message_handler)
    socketio_client.emit('connect')
    socketio_client.sleep(1)
    assert any(msg['message'] == 'Connected to server' for msg in messages)
