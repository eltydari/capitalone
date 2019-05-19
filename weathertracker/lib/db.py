"""
Simple dictionary db interface that lives in process memory

"""

_db_instance = None

def get_db():
    global _db_instance
    if _db_instance is None:
        _db_instance = {}
    return _db_instance