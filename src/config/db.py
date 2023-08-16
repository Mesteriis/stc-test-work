from pydantic_settings import BaseSettings


class SettingsDB(BaseSettings):
    user: str
    password: str
    host: str
    port: str
    name: str

    class Config:
        env_prefix = "db_"
        validate_assignment = True

    @property
    def url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
