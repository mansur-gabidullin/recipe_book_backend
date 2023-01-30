from dataclasses import dataclass


@dataclass
class UserEntity:
    id: int
    login: str
    password_solt: str
    password_hash: str
    email: str | None
