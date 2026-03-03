"""
users: create table
"""

def step(context, *args, **kwargs):
    context.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

def rollback(context, *args, **kwargs):
    context.execute("DROP TABLE users;")