import os
import datetime
from calculator_logic import AdditionOperation, SubtractionOperation, MultiplicationOperation, DivisionOperation, ExponentiationOperation, ModuloOperation

class MaangasCalculatorApplication:
    def __init__(self):
        self.mathematical_operations_registry = {
            '1': AdditionOperation(),
            '2': SubtractionOperation(),
            '3': MultiplicationOperation(),
            '4': DivisionOperation(),
            '5': ExponentiationOperation(),
            '6': ModuloOperation()
        }
        self.successful_calculation_session_counter = 0
        self.calculation_history_log = []
        self.previous_computation_result = None
    
    def clear_terminal_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def generate_time_based_greeting(self):
        current_system_hour = datetime.datetime.now().hour
        if current_system_hour < 12:
            return "Good morning"
        elif 12 <= current_system_hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"
    
    def get_validated_numerical_input(self, prompt_message_text):
        while True:
            try:
                return float(input(prompt_message_text))
            except ValueError:
                print("⚠️  INVALID INPUT: Please enter a valid numerical value. Letters are not accepted.")
        
    def start_calculator_interface(self):
        while True:
            self.clear_terminal_screen()
            dynamic_system_greeting = self.generate_time_based_greeting()
            print(f"🔥 {dynamic_system_greeting.upper()}! WELCOME TO MAANGAS PRO CALCULATOR 🔥\n")

            try:
                print("AVAILABLE MATHEMATICAL OPERATIONS:")
                print("[1] Addition       [2] Subtraction")
                print("[3] Multiplication [4] Division")
                print("[5] Exponentiation [6] Modulo (Remainder)\n")
                
                selected_menu_index_choice = input("Select operation index number: ")

                if selected_menu_index_choice not in self.mathematical_operations_registry:
                    raise ValueError("The operation choice provided is out of bounds.")

                user_provided_first_number = None
                
                if self.previous_computation_result is not None:
                    use_previous_prompt = input(f"Use previous result ({self.previous_computation_result}) as first number? (y/n): ").lower().strip()
                    if use_previous_prompt == 'y':
                        user_provided_first_number = self.previous_computation_result

                if user_provided_first_number is None:
                    user_provided_first_number = self.get_validated_numerical_input("Enter first numerical value: ")
                
                user_provided_second_number = self.get_validated_numerical_input("Enter second numerical value: ")

                active_math_operation_instance = self.mathematical_operations_registry[selected_menu_index_choice]
                final_computed_result = active_math_operation_instance.execute_mathematical_calculation(user_provided_first_number, user_provided_second_number)
                
                self.successful_calculation_session_counter += 1
                self.previous_computation_result = final_computed_result
                
                history_entry = f"[{active_math_operation_instance.assigned_operation_name}] {user_provided_first_number} & {user_provided_second_number} = {final_computed_result}"
                self.calculation_history_log.append(history_entry)

                print(f"\n✅ COMPUTATION RESULT: {final_computed_result}")

            except ValueError as captured_value_error_message:
                print(f"\n⚠️  INVALID INPUT DETECTED: {captured_value_error_message}")
            except ZeroDivisionError as captured_zero_division_error:
                print(f"\n🚫 OPERATION DENIED: {captured_zero_division_error}")
            except Exception as unhandled_system_error:
                print(f"\n💥 CRITICAL SYSTEM ERROR: {unhandled_system_error}")
            
            finally:
                user_continue_prompt_response = input("\nWould you like to perform another mathematical operation? (y/n): ").lower().strip()
                if user_continue_prompt_response != 'y':
                    self.clear_terminal_screen()
                    
                    print("📊 SESSION CALCULATION HISTORY 📊")
                    if not self.calculation_history_log:
                        print("No successful calculations were made.")
                    else:
                        for entry in self.calculation_history_log:
                            print(f"  -> {entry}")
                            
                    print(f"\nTOTAL SUCCESSFUL CALCULATIONS RECORDED: {self.successful_calculation_session_counter}")
                    print("🔥 THANK YOU FOR UTILIZING MAANGAS PRO CALCULATOR. STAY ELITE. 🔥")
                    break

if __name__ == "__main__":
    primary_calculator_app_instance = MaangasCalculatorApplication()
    primary_calculator_app_instance.start_calculator_interface()
