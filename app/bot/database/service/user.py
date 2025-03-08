from database.base import User
from database.session import new_session


class UserService:


    async def get(chat_id : int) -> User | None:
        Session = new_session()

        async with Session() as session:
            return await session.get(User, chat_id)
        
    async def create(chat_id : int) -> User:
        Session = new_session()
        this_object = User(chat_id=chat_id)

        async with Session() as session:
            session.add(this_object)
            await session.commit()

        return this_object