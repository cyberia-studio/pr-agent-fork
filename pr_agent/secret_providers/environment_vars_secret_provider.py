import ujson
import os
from google.cloud import storage

from pr_agent.config_loader import get_settings
from pr_agent.log import get_logger
from pr_agent.secret_providers.secret_provider import SecretProvider


class EnvironmentVarsSecretProvider(SecretProvider):
    def __init__(self):
        try:
            return
        except Exception as e:
            get_logger().error(f"Failed to initialize Google Cloud Storage Secret Provider: {e}")
            raise e

    def get_secret(self, secret_name: str) -> str:
        try:
            return os.getenv(secret_name)
        except Exception as e:
            get_logger().error(f"Failed to get secret {secret_name} from Environment: {e}")
            return ""

    def store_secret(self, secret_name: str, secret_value: str):
        try:
            os.environ[secret_name] = secret_value
        except Exception as e:
            get_logger().error(f"Failed to store secret {secret_name} in Environment: {e}")
            raise e
