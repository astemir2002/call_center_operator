import pytest

from call_center.core import min_operators


def test_single_call():
    """
        Тестирует случай с одним звонком. Ожидается, что потребуется один оператор.
    """
    logs = [
        "FROM:2021-01-30 22:18 TO:2021-01-30 22:31",
    ]
    assert min_operators(logs) == 1


def test_no_overlap():
    """
        Тестирует случай с двумя звонками, которые не пересекаются. Ожидается, что потребуется один оператор.
    """
    logs = [
        "FROM:2021-01-30 22:18 TO:2021-01-30 22:31",
        "FROM:2021-01-30 22:32 TO:2021-01-30 22:45",
    ]
    assert min_operators(logs) == 1


def test_overlap():
    """
        Тестирует случай с двумя звонками, которые пересекаются. Ожидается, что потребуется два оператора.
    """
    logs = [
        "FROM:2021-01-30 22:18 TO:2021-01-30 22:31",
        "FROM:2021-01-30 22:25 TO:2021-01-30 22:45",
    ]
    assert min_operators(logs) == 2


def test_multiple_overlaps():
    """
        Тестирует случай с несколькими звонками, которые пересекаются
    """
    logs = [
        "FROM:2021-01-30 22:18 TO:2021-01-30 22:31",
        "FROM:2021-01-30 22:25 TO:2021-01-30 22:45",
        "FROM:2021-01-30 22:27 TO:2021-01-30 22:35",
        "FROM:2021-01-30 22:30 TO:2021-01-30 22:50",
    ]
    assert min_operators(logs) == 4


def test_empty_log():
    """
        Тестирует случай с пустым списком звонков
    """
    logs = []
    assert min_operators(logs) == 0


def test_edge_case_exact_overlap():
    """
        Тестирует случай, когда несколько звонков имеют точное совпадение по времени
    """
    logs = [
        "FROM:2021-01-30 22:18 TO:2021-01-30 22:31",
        "FROM:2021-01-30 22:18 TO:2021-01-30 22:31",
    ]
    assert min_operators(logs) == 2


if __name__ == "__main__":
    pytest.main()
