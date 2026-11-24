"""CLI for Action Edgecase Fuzzer."""
import argparse
from .core import ActionFuzzer

def main():
    parser = argparse.ArgumentParser(description="Agent Action Edgecase Fuzzer CLI")
    parser.add_argument("--demo", action="store_true", help="Run action fuzzer demo")
    args = parser.parse_args()

    def sample_tool(val):
        if val is None:
            raise ValueError("Val cannot be None")
        return str(val)

    rep = ActionFuzzer.fuzz_function(sample_tool)
    print(f"Fuzzing Complete: {rep.runs} runs, {rep.crashes} crashes detected.")

if __name__ == "__main__":
    main()
