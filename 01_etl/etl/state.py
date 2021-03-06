import logging
from abc import ABCMeta, abstractmethod
from typing import Optional

import backoff
from config import BACKOFF_CONFIG, RedisSettings
from redis import Redis


def redis_conn_is_alive(redis_conn: Redis) -> bool:
    """Функция для проверки аботоспособности редис"""
    try:
        redis_conn.ping()
    except Exception:
        return False
    return True


class BaseState:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, key: str, default_value: Optional[str] = None) -> Optional[str]:
        """Получение состояния"""

    @abstractmethod
    def set(self, key: str, value: str) -> None:
        """Установка состояния"""


class RedisState(BaseState):
    """Класс для управления состоянием ETL."""

    logger = logging.getLogger(__name__)

    def __init__(self, settings: RedisSettings, redis_conn: Optional[Redis] = None) -> None:
        self._settings = settings
        self._redis_conn = redis_conn

    @backoff.on_exception(**BACKOFF_CONFIG, logger=logger)
    def _reconnection(self):
        if self._redis_conn is not None:
            self._redis_conn.close()

        return Redis(**self._settings.dict())

    @property
    def redis_conn(self) -> Redis:
        if self._redis_conn is None or not redis_conn_is_alive(self._redis_conn):
            self._redis_conn = self._reconnection()
        return self._redis_conn

    @backoff.on_exception(**BACKOFF_CONFIG, logger=logger)
    def get(self, key: str, default_value: Optional[str] = None) -> Optional[str]:
        """Получение текущего состояния по ключу, в случае если оно не задано возвращается занчение default_value."""
        value = self.redis_conn.get(key)
        return value.decode() if value is not None else default_value

    @backoff.on_exception(**BACKOFF_CONFIG, logger=logger)
    def set(self, key: str, value: str) -> None:
        """Установка текущего состояния по ключу"""
        self.redis_conn.set(key, value.encode())
