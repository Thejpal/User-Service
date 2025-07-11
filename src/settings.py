from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    jwt_secret_key: str
    algorithm: str
    token_expiration_minutes: int
    database_url: str
    postgres_user: str
    postgres_password: str
    postgres_db: str
    service_name: str
    
    model_config = SettingsConfigDict(env_file = ".env")

# Setting type ignore comment to suppress mypy warning about missing initialization arguments for Settings class
settings = Settings()  # type: ignore