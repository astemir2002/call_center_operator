import timeit
import memory_profiler
import logging
from typing import List


from call_center.core import min_operators
from call_center.utils import generate_test_log


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def benchmark_time(logs: List[str], description: str) -> None:
    """
        Измеряет время выполнения функции min_operators.
    """
    exec_time = timeit.timeit(lambda: min_operators(logs), number=1)
    logger.info(f"{description} - Execution time: {exec_time:.6f} seconds")


@memory_profiler.profile
def benchmark_memory(logs: List[str], description: str) -> None:
    """
        Измеряет использование памяти функцией min_operators.
    """
    logger.info(description)
    min_operators(logs)


if __name__ == "__main__":
    test_logs: List[str] = generate_test_log(1000)
    benchmark_time(test_logs, "Generated test - small")
    benchmark_memory(test_logs, "Generated test - small")

