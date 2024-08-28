from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admins: list[int]


@dataclass
class Config:
    bot: TgBot


def config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(bot=TgBot(token=env('BOT_TOKEN'), admins=[int(admin) for admin in env.list('ADMINS')]))
