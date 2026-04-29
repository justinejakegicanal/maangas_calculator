import datetime
from calculator_logic import AdditionOperation, SubtractionOperation, MultiplicationOperation, DivisionOperation

class MaangasCalculatorApplication:
    def __init__(self):
        self.mathematical_operations_registry = {
            '1': AdditionOperation(),
            '2': SubtractionOperation(),
            '3': MultiplicationOperation(),
            '4': DivisionOperation()
        }
        self.successful_calculation_session_counter = 0
        