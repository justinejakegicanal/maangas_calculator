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
    
    def generate_time_based_greeting(self):
        current_system_hour = datetime.datetime.now().hour
        if current_system_hour < 12:
            return "Good morning"
        elif 12 <= current_system_hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"

