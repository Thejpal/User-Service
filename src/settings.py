from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    jwt_secret_key: str
    algorithm: str
    token_expiration_minuites: int
    database_url: str
    
    model_config = SettingsConfigDict(env_file = ".env")

settings = Settings()