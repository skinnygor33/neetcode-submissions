
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if operations is None: 
            return "No operations where found"
        record = []
        for op in operations: 
            if op == "+": 
                record.append(record[-1] + record[len(record) - 2])
            elif op == "D": 
                print("Hi")
                record.append(record[-1] * 2 )
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))

        return sum(record)