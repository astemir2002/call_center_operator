import random
import logging

from datetime import datetime, timedelta
from typing import List


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def generate_test_log(num_entries: int = 1000) -> List[str]:
    """
        Генерирует тестовые записи логов звонков в call-центре.
    """
    logs = []
    for _ in range(num_entries):
        avg_time = datetime.now() - timedelta(seconds=random.randint(0, 1000000))
        from_time = avg_time - timedelta(seconds=random.randint(0, 1000))
        to_time = avg_time + timedelta(seconds=random.randint(0, 1000))
        log_entry = f"FROM:{from_time.strftime('%Y-%m-%d %H:%M')} TO:{to_time.strftime('%Y-%m-%d %H:%M')}"
        logger.info(f"Сгенерирован лог: {log_entry}")
        logs.append(log_entry)
    return logs


if __name__ == "__main__":
    generate_test_log()
