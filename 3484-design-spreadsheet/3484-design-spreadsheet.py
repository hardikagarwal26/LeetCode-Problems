class Spreadsheet:

    def __init__(self, rows: int):
        self.cellValues = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cellValues[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cellValues[cell] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        leftOperand, rightOperand = formula.split("+")

        def eval(op):
            if op[0].isdigit():
                return int(op)
            return self.cellValues.get(op, 0)

        return eval(leftOperand) + eval(rightOperand)



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)