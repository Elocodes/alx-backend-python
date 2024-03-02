#!/usr/bin/env python3
""" Basics of async """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Function waits for max_delay and returns the value """
    response = random.uniform(0, max_delay)
    await asyncio.sleep(response)
    return response
