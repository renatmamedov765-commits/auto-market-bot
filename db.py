import aiosqlite

DB_NAME = "market.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            description TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            car_id INTEGER,
            contact TEXT
        )
        """)
        await db.commit()


async def add_car(title, price, description):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO cars (title, price, description) VALUES (?, ?, ?)",
            (title, price, description)
        )
        await db.commit()


async def get_cars():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM cars")
        return await cursor.fetchall()


async def add_request(user, car_id, contact):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO requests (user, car_id, contact) VALUES (?, ?, ?)",
            (user, car_id, contact)
        )
        await db.commit()
