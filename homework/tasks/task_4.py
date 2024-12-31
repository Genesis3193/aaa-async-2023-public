sequence = []


async def task_1(i: int):
    if i == 0:
        return

    sequence.append(1)

    if i > 5:
        await task_2(i // 2)
    else:
        await task_2(i - 1)


async def task_2(i: int):
    if i == 0:
        return

    sequence.append(2)

    if i % 2 == 0:
        await task_1(i // 2)
    else:
        await task_2(i - 1)


async def coroutines_execution_order(i: int = 42) -> int:
    global sequence
    sequence = []

    await task_1(i)

    result = int("".join(map(str, sequence)))
    return result
