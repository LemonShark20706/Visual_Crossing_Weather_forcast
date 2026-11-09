import os
import dataclasses
from dotenv import load_dotenv

class Env_Loader:
    def __init__(self, env_file="Weather_Crossing\\env_loader\\env\\.env"):
        self.env_file = env_file
        self.env_keys = []
        load_dotenv(self.env_file)

    def load_env_variables(self):
        try:
            with open(self.env_file, "r") as file:
                for line in file:
                    if line.strip() and not line.startswith("#"):
                        key, value = line.strip().split("=", 1)
                        os.environ[key] = value
                        self.env_keys.append(key)
        except FileNotFoundError:
            raise SystemExit(f"Nem található a {self.env_file} fájl.")

    def get_env_variable(self, key):
        return os.getenv(key)

    def set_env_variable(self, key, value):
        os.environ[key] = value
        self.env_keys.append(key)

    def delete_env_variable(self, key):
        if key in os.environ:
            del os.environ[key]
            self.env_keys.remove(key)
        else:
            raise KeyError(f"A(z) {key} környezeti változó nem található.")

@dataclasses.dataclass
class Loaded_Env_Variables:
    api_key: str
    base_url: str

    @classmethod
    def from_env_loader(cls, env_loader: Env_Loader):
        api_key = env_loader.get_env_variable("API_KEY")
        base_url = env_loader.get_env_variable("BASE_URL")
        if not api_key or not base_url:
            raise SystemExit("Az API_KEY vagy BASE_URL környezeti változó hiányzik.")
        return cls(api_key=api_key, base_url=base_url)

__all__ = ["Env_Loader", "Loaded_Env_Variables"]