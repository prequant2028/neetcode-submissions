class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if op not in ["+", "D", "C"]:
                scores.append(int(op))

            elif op == "+":
                scores.append(scores[-1] + scores[-2])

            elif op == "D":
                scores.append(scores[-1] * 2)

            else:  # C
                scores.pop()

        return sum(scores)