"""
Simple dictionary db interface that lives in process memory.
Can be extended in the future to accept more types of dbs.

Note: I would have renamed "utils" as "lib" but I don't think that's in scope for this test
"""

_db_instance = None

def get_db():
    global _db_instance
    if _db_instance is None:
        _db_instance = {}
    return _db_instance