from datetime import datetime
from typing import List
import logging

from call_center.utils import generate_test_log


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def min_operators(logs: List[str]) -> int:
    """
        Вычисляет минимальное количество операторов call-центра, необходимое для того,
        чтобы все звонки были обработаны без ожидания.
    """
    events = []

    for log in logs:
        parts = log.split()
        start_time_str = parts[0].split("FROM:")[1] + " " + parts[1]
        end_time_str = parts[2].split("TO:")[1] + " " + parts[3]

        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

        events.append((start_time, 1))
        events.append((end_time, -1))

    events.sort()

    max_operators = 0
    current_operators = 0

    for _, delta in events:
        current_operators += delta
        if current_operators > max_operators:
            max_operators = current_operators

    return max_operators


if __name__ == "__main__":
    logg = generate_test_log()
    min_operators_needed = min_operators(logg)
    logger.info(f"Минимальное количество операторов, чтобы ни один звонок не ожидал: {min_operators_needed}")
