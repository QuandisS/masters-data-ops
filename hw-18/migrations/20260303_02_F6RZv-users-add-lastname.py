"""
users: add lastname
"""

def step(context, *args, **kwargs):
    context.execute("ALTER TABLE users ADD COLUMN lastname VARCHAR(100);")

def rollback(context, *args, **kwargs):
    context.execute("ALTER TABLE users DROP COLUMN lastname;")
