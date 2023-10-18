from dotenv import load_dotenv
import os
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: str
    manager_id: str
    number_messages_review: int

@dataclass
class Settings:
    bots: Bots


def get_settings():

    load_dotenv()
    return Settings(
        bots=Bots(
            bot_token=os.getenv('TOKEN_TG_BOT'),
            admin_id=os.getenv('ADMIN_ID_TG_BOT'),
            manager_id=os.getenv('MANAGER_ID'),
            number_messages_review=int(os.getenv('NUMBER_MESSAGES_REVIEW'))
        )
    )

settings = get_settings()