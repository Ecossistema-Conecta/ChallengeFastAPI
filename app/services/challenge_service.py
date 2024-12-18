import os
from functools import lru_cache
from typing import List, Optional
from app.utils.constants import Templates
from app.utils.regex_patterns import STEP_PATTERN


@lru_cache(maxsize=1)
def get_available_steps() -> List[int]:
    steps = sorted(
        int(match.group(1))
        for f in os.listdir(Templates.TEMPLATES_DIR)
        if (match := STEP_PATTERN.search(f))
    )
    return steps


def step_exists(step: Optional[int]) -> bool:
    if step is None:
        return True
    return step in get_available_steps()


def get_template_name(step: Optional[int]) -> str:
    return Templates.CHALLENGE_STEP.format(step=step)  if step else Templates.CHALLENGE_OVERVIEW


def calculate_next_step(step: Optional[int]) -> Optional[int]:
    steps = get_available_steps()
    if step is None:
        return steps[0] if steps else None
    try:
        current_index = steps.index(step)
        return steps[current_index + 1] if current_index + 1 < len(steps) else None
    except ValueError:
        return None


def calculate_previous_step(step: Optional[int]) -> Optional[int]:
    steps = get_available_steps()
    if step is None:
        return None
    try:
        current_index = steps.index(step)
        return steps[current_index - 1] if current_index > 0 else None
    except ValueError:
        return None
