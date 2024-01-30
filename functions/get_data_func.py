from typing import Tuple

from utils.db_api import db_commands



async def get_data(telegram_id: int) -> Tuple[str, int, str, str, str, str, str, str, str, str, str, str, str]:
    user = await db_commands.select_user(telegram_id=telegram_id)
    user_name = user.get("name")
    user_number = user.get("phone")
    user_location = user.get("location"),


    return (
        user_name, user_number,  user_location
         
    )

