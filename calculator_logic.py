class MathOperation:
    def __init__(self, assigned_operation_name):
        self.assigned_operation_name = assigned_operation_name

    def execute_mathematical_calculation(self, first_operand_value, second_operand_value):
        pass

class AdditionOperation(MathOperation):
    def __init__(self):
        super().__init__("Addition")
    def execute_mathematical_calculation(self, first_operand_value, second_operand_value):
        return first_operand_value + second_operand_value