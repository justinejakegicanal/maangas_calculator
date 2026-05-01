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
        
    def start_calculator_interface(self):
        dynamic_system_greeting = self.generate_time_based_greeting()
        print(f"🔥 {dynamic_system_greeting.upper()}! WELCOME TO MAANGAS PRO CALCULATOR 🔥")

        while True:
            try:
                print("\nAVAILABLE MATHEMATICAL OPERATIONS:")
                print("[1] Addition  [2] Subtraction")
                print("[3] Multiplication  [4] Division")
                
                selected_menu_index_choice = input("Select operation index number: ")

                if selected_menu_index_choice not in self.mathematical_operations_registry:
                    raise ValueError("The operation choice provided is out of bounds.")

                user_provided_first_number = float(input("Enter first numerical value: "))
                user_provided_second_number = float(input("Enter second numerical value: "))

                active_math_operation_instance = self.mathematical_operations_registry[selected_menu_index_choice]
                final_computed_result = active_math_operation_instance.execute_mathematical_calculation(user_provided_first_number, user_provided_second_number)
                
                self.successful_calculation_session_counter += 1
                print(f"\n✅ COMPUTATION RESULT ({active_math_operation_instance.assigned_operation_name}): {final_computed_result}")

            except ValueError as captured_value_error_message:
                print(f"⚠️  INVALID INPUT DETECTED: {captured_value_error_message}")
            except ZeroDivisionError as captured_zero_division_error:
                print(f"🚫 OPERATION DENIED: {captured_zero_division_error}")
            except Exception as unhandled_system_error:
                print(f"💥 CRITICAL SYSTEM ERROR: {unhandled_system_error}")
