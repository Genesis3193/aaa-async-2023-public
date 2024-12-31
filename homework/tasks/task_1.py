from typing import Callable, Coroutine, Any, TypeVar, Union
from asyncio import Task


T = TypeVar("T")


async def await_my_func(
    f: Union[Callable[..., Coroutine[Any, Any, T]], Task[T], Coroutine[Any, Any, T]]
) -> T:

    if isinstance(f, Callable):
        coroutine = f()
        return await coroutine
    elif isinstance(f, Task):
        return await f
    elif isinstance(f, Coroutine):
        return await f
    else:
        raise ValueError("invalid argument")
