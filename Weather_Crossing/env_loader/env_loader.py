import os
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

__all__ = ["Env_Loader"]