"""Loading environment variables"""

import os
import sys

from fastapi.logger import logger


class MissingEnvironmentVariableError(KeyError):
    """
    Raised when environment variable is not implemented yet.
    """

    def __init__(self, env: str) -> None:
        self.message = f"Environment variable {env} is not implemented yet"
        super().__init__(self.message)
        logger.error(self.message)
        sys.exit(1)


def get_env(name: str, default_value: str = None) -> str:
    """
    Get environment variable.
    :param name: Name of environment variable.
    :param default_value: Default value if environment variable is not set.
    :return: Value of environment variable.
    """
    try:
        return os.environ[name]
    except KeyError as error:
        if not default_value:
            raise MissingEnvironmentVariableError(name) from error
        return default_value


class Envs:
    ENVIRONMENT = get_env("ENVIRONMENT", "development")
    DATABASE_URI = get_env("DATABASE_URI")
