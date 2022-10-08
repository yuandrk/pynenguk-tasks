def test_task_stdout(capsys):
    """
    Проверка работы задания
    """
    import task_6_3

    out, err = capsys.readouterr()
    correct_stdout = (
        "[100, 30, 10, 20, 15, 100]"
    )
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


def test_task_variables():
    """
    Проверка что в задании создана нужная переменная
    и в ней содержится правильный результат
    """
    import task_6_3

    # переменные созданные в задании:
    task_vars = [var for var in dir(task_6_3) if not var.startswith("_")]

    correct_result = [100, 30, 10, 20, 15, 100]

    assert (
        "result" in task_vars
    ), "Итоговый список должен быть записан в переменную result"
    assert (
        type(task_6_3.result) == list
    ), f"По заданию в переменной result должен быть список, а в ней {type(task_6_3.result).__name__}"
    assert (
        correct_result == task_6_3.result
    ), f"В переменной result должен быть список {correct_result}"

