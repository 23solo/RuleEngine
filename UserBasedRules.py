class RuleEngine:
    def __init__(self):
        self.conditions = []
        self.action = ""
        self.actions = []
        self.operator = "or"
        self.is_multiple_action = False
        self.num_conditions = 0
# Gives user the info to add 
    def help_user(self):
        print("User Guide :\n")
        print("For Greater Than and Equal, Enter: \n`input >=`")
        print("For Less Than and Equal, Enter: \n`input <=`")
        print("For Equal, Enter: \n input `==`")
        print("For multiple conditions if any true, Enter \n`input < 10 or input > 20`")
        print("For multiple conditions if all true, Enter \n`input > 10 and input < 20`")
        _ = input("Enter anything to continue\n")
        return

    def multiple_actions(self):
        multiple_action = input(
            "If you have actions per condition enter `Y` else enter `N`\n")
        if (multiple_action.upper() == 'Y'):
            self.is_multiple_action = True
        operator = input(
            "Do you want action to take place only if all condtion satisfy enter `Y` else enter `N`\n")
        if (operator.upper() == 'Y'):
            self.operator = "and"

    def generate_conditions(self):
        self.num_conditions = int(input("Enter the number of conditions: "))
        for i in range(self.num_conditions):
            if(self.is_multiple_action):
              condition = input(f"Enter condition {i+1}: ")
              action = input("Enter the corresponding action ")
              self.actions.append(action)
            else:
                condition = input(f"Enter condition {i+1}: ")
            self.conditions.append(condition)

    def get_action(self):
        self.action = input("Enter the action: ")

    def generate_rule(self):
        rule = self.conditions[0]
        for i in range(1, len(self.conditions)):
            rule += f" {self.operator} {self.conditions[i]}"
        return rule

    def apply_rule(self, input):
        if self.is_multiple_action:
            for i in range(0,self.num_conditions):
                if (eval(self.conditions[i])):
                    return f"Action: {self.actions[i]}"
        else:
            rule = self.generate_rule()
            if (eval(rule)):
                return f"Action: {self.action}"
        return "No Action To Be Performed"


# Creating the Model
rule_engine = RuleEngine()
rule_engine.help_user()
rule_engine.multiple_actions()
rule_engine.generate_conditions()
if not rule_engine.is_multiple_action: 
  rule_engine.get_action()

while True:
  input_value = input("Enter the Value to test")
  result = rule_engine.apply_rule(input_value)
  print(result)
  break
