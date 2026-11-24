"""Core Action Fuzzer implementation."""
from typing import Dict, List, Any, Callable

class FuzzReport:
    def __init__(self, runs: int, crashes: int, crash_inputs: List[Any]):
        self.runs = runs
        self.crashes = crashes
        self.crash_inputs = crash_inputs

class ActionFuzzer:
    FUZZ_VALUES = [
        None,
        "",
        "\x00\x01",
        "A" * 5000,
        -1,
        0,
        2147483647,
        -2147483648,
        [],
        {}
    ]

    @classmethod
    def fuzz_function(cls, fn: Callable[[Any], Any]) -> FuzzReport:
        crashes = 0
        crash_inputs = []

        for val in cls.FUZZ_VALUES:
            try:
                fn(val)
            except Exception as e:
                crashes += 1
                crash_inputs.append({"input": str(val)[:50], "error": str(e)})

        return FuzzReport(len(cls.FUZZ_VALUES), crashes, crash_inputs)
