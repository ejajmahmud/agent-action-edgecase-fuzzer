"""Tests for ActionFuzzer."""
import unittest
from agent_action_edgecase_fuzzer.core import ActionFuzzer

class TestActionFuzzer(unittest.TestCase):
    def test_fuzzing_resilience(self):
        # Function that handles all inputs cleanly
        safe_fn = lambda x: f"Safe: {x}"
        rep = ActionFuzzer.fuzz_function(safe_fn)
        self.assertEqual(rep.crashes, 0)

    def test_crash_capture(self):
        fragile_fn = lambda x: x + 10
        rep = ActionFuzzer.fuzz_function(fragile_fn)
        self.assertTrue(rep.crashes > 0)
