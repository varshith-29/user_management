from app.database import Database
from sqlalchemy.ext.asyncio import AsyncSession

async def get_db() -> AsyncSession:
    """
    Dependency that provides a database session
    """
    session_factory = Database.get_session_factory()
    async with session_factory() as session:
        try:
            yield session
        finally:
            await session.close()
