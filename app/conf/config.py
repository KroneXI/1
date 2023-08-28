from dotenv import dotenv_values
from pathlib import Path
import os
import sys

class Config:
    def __init__(self) -> None:
        self.docker = self.is_docker()

    def is_docker(self) -> bool:
        return Path('/.dockerenv').exists()

    def get_config(self, param: str):
        env = dotenv_values('/.env') if self.docker else dotenv_values(f'{os.path.dirname(sys.argv[0])}/../.env')
        return env[param]