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
    
class SubtractionOperation(MathOperation):
    def __init__(self):
        super().__init__("Subtraction")
    def execute_mathematical_calculation(self, first_operand_value, second_operand_value):
        return first_operand_value - second_operand_value
    
class MultiplicationOperation(MathOperation):
    def __init__(self):
        super().__init__("Multiplication")
    def execute_mathematical_calculation(self, first_operand_value, second_operand_value):
        return first_operand_value * second_operand_value

class DivisionOperation(MathOperation):
    def __init__(self):
        super().__init__("Division")
    def execute_mathematical_calculation(self, first_operand_value, second_operand_value):
        if second_operand_value == 0:
            raise ZeroDivisionError("Mathematical Error: Dividing a number by zero is strictly prohibited.")
        return first_operand_value / second_operand_value

class ExponentiationOperation(MathOperation):
    def __init__(self):
        super().__init__("Exponentiation (Power)")
    def execute_mathematical_calculation(self, first_operand_value, second_operand_value):
        return first_operand_value ** second_operand_value

class ModuloOperation(MathOperation):
    def __init__(self):
        super().__init__("Modulo (Remainder)")
    def execute_mathematical_calculation(self, first_operand_value, second_operand_value):
        if second_operand_value == 0:
            raise ZeroDivisionError("Mathematical Error: Modulo by zero is strictly prohibited.")
        return first_operand_value % second_operand_value