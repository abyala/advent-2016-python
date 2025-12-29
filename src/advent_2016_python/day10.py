import re
from typing import Dict, List, Tuple


class BotSystem:
    def give_bot(self, b: str, v: int):
        self.bots.setdefault(b, []).append(v)

    def give_output(self, o: str, v: int):
        self.outputs[o] = v

    def init_rule(self, b: str, type0, id0, type1, id1):
        self.rules[b] = (type0, id0, type1, id1)

    def __init__(self, data: str):
        self.bots: Dict[str, List[int]] = {}
        self.outputs: Dict[str, int] = {}
        self.rules: Dict[str, Tuple[str, str, str, str]] = {}
        self.responsibilities: Dict[Tuple[int, int], str] = {}

        for line in sorted(data.splitlines()):
            if line.startswith("value "):
                v, b = re.findall("\\d+", line)
                self.give_bot(b, int(v))
            else:
                _, b, t0, v0, t1, v1, _ = re.split("bot (\\d+) gives low to (\\w+) (\\d+) and high to (\\w+) (\\d+)",
                                                   line)
                self.init_rule(b, t0, v0, t1, v1)
        self.process()

    def give_away(self, b: str):
        vals = sorted(self.bots[b])
        if len(vals) != 2:
            raise AssertionError(f"Bot {b} should have two values but instead has values {vals}")

        type0, id0, type1, id1 = self.rules[b]
        if type0 == 'bot':
            self.give_bot(id0, vals[0])
        else:
            self.give_output(id0, vals[0])
        if type1 == 'bot':
            self.give_bot(id1, vals[1])
        else:
            self.give_output(id1, vals[1])

        del self.bots[b]
        self.responsibilities[(vals[0], vals[1])] = b

    def process(self):
        while True:
            bot_id = next((id for id in self.bots.keys() if len(self.bots[id]) == 2), None)
            if bot_id is None:
                break
            self.give_away(bot_id)

    def who_processes(self, v0: int, v1: int) -> str | None:
        return self.responsibilities.get((v0, v1) if v0 < v1 else (v1, v0))


def part1(data: str, v0: int, v1: int) -> str:
    return BotSystem(data).who_processes(v0, v1)


def part2(data: str) -> int:
    outputs = BotSystem(data).outputs
    return outputs["0"] * outputs["1"] * outputs["2"]
