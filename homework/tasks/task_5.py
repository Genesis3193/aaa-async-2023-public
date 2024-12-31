import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine, max_execution_time: float) -> None:
    try:
        await asyncio.wait_for(coro, timeout=max_execution_time)
    except asyncio.TimeoutError:
        print(
            f"Корутини выполнялась слишком долго и была отменена {max_execution_time} секунд."
        )
    except Exception as e:
        print(f"Ошибка: {e}")


async def limit_execution_time_many(
    *coros: Coroutine, max_execution_time: float
) -> None:
    try:
        await asyncio.wait_for(asyncio.gather(*coros), timeout=max_execution_time)
    except asyncio.TimeoutError:
        print(
            f"Корутины выполнялись слишком долго и была отменена {max_execution_time} секунд."
        )
    except Exception as e:
        print(f"Ошибка: {e}")
