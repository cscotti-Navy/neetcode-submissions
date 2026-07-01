class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        record = []
        for i in range(n):
            if operations[i] == '+':
               x = record[-1] + record[-2]
               record.append(x)
            elif operations[i] == 'D': 
                x = 2 * record[-1]
                record.append(x)
            elif operations[i] == 'C':
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)