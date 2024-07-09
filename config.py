import threading

# In-memory storage for tests
tests = {}
tests_lock = threading.Lock()
