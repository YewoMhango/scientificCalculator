from tkinter import *
import math

# all operators in order of decreasing precedence
OPERATORS = ["~", "!", "cos", "sin", "tan", "acos", "asin",
             "atan", "log", "ln", "√", "P", "C", "^", "×", "÷", "%", "+", "-"]
UNARY_OPERATORS = ["~", "!", "cos", "sin", "tan",
                   "acos", "asin", "atan", "log", "ln", "√"]
CONSTANTS = ["π", "e"]


class Calculator:
    def __init__(self):
        window = Tk()
        window.title("Scientific Calculator")

        self.label = Label(window, width=53, font="Consolas 14",
                           bg="white", relief=SUNKEN)
        self.label.grid(row=1, column=0, columnspan=9, padx=5, pady=5)

        # This is where all the input from the user gets stored whenever the user clicks the buttons.
        # I could have simply used a string whereby the input just gets concatenated into one string upon
        # entry but I feel using a list instead makes each element more atomic and hence a lot easier to parse.
        self.inputElements = []

        numberBg = "#e2e2e2"
        fontStyle = "Consolas"

        self.button_7 = Button(window, text="7", command=lambda: self.enter_symbol(
            "7"), padx=20, pady=0, font=fontStyle, bg=numberBg, relief=FLAT)
        self.button_8 = Button(window, text="8", command=lambda: self.enter_symbol(
            "8"), padx=20, pady=0, font=fontStyle, bg=numberBg, relief=FLAT)
        self.button_9 = Button(window, text="9", command=lambda: self.enter_symbol(
            "9"), padx=20, pady=0, font=fontStyle, bg=numberBg, relief=FLAT)
        self.button_4 = Button(window, text="4", command=lambda: self.enter_symbol(
            "4"), padx=20, pady=0, font=fontStyle, bg=numberBg, relief=FLAT)
        self.button_5 = Button(window, text="5", command=lambda: self.enter_symbol(
            "5"), padx=20, pady=0, font=fontStyle, bg=numberBg, relief=FLAT)
        self.button_6 = Button(window, text="6", command=lambda: self.enter_symbol(
            "6"), padx=20, pady=0, font=fontStyle, bg=numberBg, relief=FLAT)
        self.button_1 = Button(window, text="1", command=lambda: self.enter_symbol(
            "1"), padx=20, pady=0, font=fontStyle, bg=numberBg, relief=FLAT)
        self.button_2 = Button(window, text="2", command=lambda: self.enter_symbol(
            "2"), padx=20, pady=0, font=fontStyle, bg=numberBg, relief=FLAT)
        self.button_3 = Button(window, text="3", command=lambda: self.enter_symbol(
            "3"), padx=20, pady=0, font=fontStyle, bg=numberBg, relief=FLAT)
        self.button_0 = Button(window, text="0", command=lambda: self.enter_symbol(
            "0"), padx=20, pady=0, font=fontStyle, bg=numberBg, relief=FLAT)
        self.button_point = Button(window, text=".", command=lambda: self.enter_symbol(
            "."), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_clear = Button(
            window, text="Clr", command=self.clear, padx=10, pady=0, font=fontStyle, relief=FLAT)
        self.button_equal = Button(
            window, text="=", command=self.equals, padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_plus = Button(window, text="+", command=lambda: self.enter_symbol(
            "+"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_minus = Button(window, text="-", command=lambda: self.enter_symbol(
            "-"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_multiply = Button(window, text="×", command=lambda: self.enter_symbol(
            "×"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_divide = Button(window, text="÷", command=lambda: self.enter_symbol(
            "÷"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_pi = Button(window, text="π", command=lambda: self.enter_symbol(
            "π"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_opening_brac = Button(window, text="(", command=lambda: self.enter_symbol(
            "("), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_closing_brac = Button(window, text=")", command=lambda: self.enter_symbol(
            ")"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_exponent = Button(window, text="^", command=lambda: self.enter_symbol(
            "^"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_sqrt = Button(window, text="√", command=lambda: self.enter_symbol(
            "√"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_ln = Button(window, text="ln", command=lambda: self.enter_symbol(
            "ln"), padx=15, pady=0, font=fontStyle, relief=FLAT)
        self.button_log = Button(window, text="log", command=lambda: self.enter_symbol(
            "log"), padx=10, pady=0, font=fontStyle, relief=FLAT)
        self.button_sin = Button(window, text="sin", command=lambda: self.enter_symbol(
            "sin"), padx=10, pady=0, font=fontStyle, relief=FLAT)
        self.button_cos = Button(window, text="cos", command=lambda: self.enter_symbol(
            "cos"), padx=10, pady=0, font=fontStyle, relief=FLAT)
        self.button_tan = Button(window, text="tan", command=lambda: self.enter_symbol(
            "tan"), padx=10, pady=0, font=fontStyle, relief=FLAT)
        self.button_atan = Button(window, text="atan", command=lambda: self.enter_symbol(
            "atan"), padx=5, pady=0, font=fontStyle, relief=FLAT)
        self.button_asin = Button(window, text="asin", command=lambda: self.enter_symbol(
            "asin"), padx=5, pady=0, font=fontStyle, relief=FLAT)
        self.button_acos = Button(window, text="acos", command=lambda: self.enter_symbol(
            "acos"), padx=5, pady=0, font=fontStyle, relief=FLAT)
        self.button_e = Button(window, text="e", command=lambda: self.enter_symbol(
            "e"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_bkSpace = Button(window, text="⇐", command=lambda: self.backspace(
        ), padx=16, pady=0, font=fontStyle, relief=FLAT)
        self.button_P = Button(window, text="P", command=lambda: self.enter_symbol(
            "P"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_C = Button(window, text="C", command=lambda: self.enter_symbol(
            "C"), padx=20, pady=0, font=fontStyle, relief=FLAT)
        self.button_factorial = Button(window, text="!", command=lambda: self.enter_symbol(
            "!"), padx=20, pady=0, font=fontStyle, relief=FLAT)

        self.button_7.grid(row=2, column=4)
        self.button_8.grid(row=2, column=5)
        self.button_9.grid(row=2, column=6)
        self.button_4.grid(row=3, column=4)
        self.button_5.grid(row=3, column=5)
        self.button_6.grid(row=3, column=6)
        self.button_1.grid(row=4, column=4)
        self.button_2.grid(row=4, column=5)
        self.button_3.grid(row=4, column=6)
        self.button_0.grid(row=5, column=5)
        self.button_point.grid(row=5, column=6)
        self.button_clear.grid(row=2, column=7)
        self.button_plus.grid(row=3, column=7)
        self.button_minus.grid(row=3, column=8)
        self.button_multiply.grid(row=4, column=7)
        self.button_divide.grid(row=4, column=8)
        self.button_equal.grid(row=5, column=8)
        self.button_pi.grid(row=5, column=4)
        self.button_opening_brac.grid(row=5, column=1)
        self.button_closing_brac.grid(row=5, column=2)
        self.button_exponent.grid(row=5, column=3)
        self.button_sqrt.grid(row=4, column=1)
        self.button_ln.grid(row=4, column=2)
        self.button_log.grid(row=4, column=3)
        self.button_sin.grid(row=3, column=1)
        self.button_cos.grid(row=3, column=2)
        self.button_tan.grid(row=3, column=3)
        self.button_asin.grid(row=2, column=1)
        self.button_acos.grid(row=2, column=2)
        self.button_atan.grid(row=2, column=3)
        self.button_bkSpace.grid(row=2, column=8)
        self.button_e.grid(row=5, column=7)
        self.button_P.grid(row=2, column=0)
        self.button_C.grid(row=3, column=0)
        self.button_factorial.grid(row=4, column=0)

        window.mainloop()

    def enter_symbol(self, symbol):
        self.inputElements.append(symbol)
        self.updateOutput()

    def clear(self):
        self.inputElements = []
        self.updateOutput()

    def backspace(self):
        """
        Removes the last element from the `inputElements` property and
        accordingly updates the output screen
        """
        if len(self.inputElements) > 0:
            self.inputElements.pop()
            self.updateOutput()

    def stringifyInput(self):
        """
        Concatenates all the elements of the `inputElements` property
        into one string for use by other functions of the object
        """
        result = ""

        for element in self.inputElements:
            result += element

        return result

    def equals(self):
        """
        Evaluates the input from the user and displays the answer
        """
        answer = self.__evaluatePostfix(self.__infixToPostfix())

        if answer % 1 == 0.0:
            answer = int(answer)

        asString = str(answer)
        self.inputElements = []

        # Instead of just adding the whole result to the array, it gets
        # spread over into individual string elements for each character
        for character in asString:
            self.inputElements.append(character)

        # self.inputElements = [asString]
        self.updateOutput()
        # self.inputElements = []

    def updateOutput(self):
        self.label["text"] = self.stringifyInput()

    def __infixToPostfix(self):
        """
        Converts the input from the user (which is supposed to be in infix
        notation) into postfix notation for easier evaluation
        """
        expression = self.inputElements

        stack = []
        result = []

        i = 0

        while i < len(expression):
            if expression[i].isdigit() or expression[i] == ".":
                num = expression[i]

                # This takes care of implicit multiplication between the number and
                # a parentheses or constant. In such cases, the × sign is inserted
                if i != 0 and (expression[i - 1] == ")" or (expression[i] in CONSTANTS)):
                    stack.append("×")

                while (not i == len(expression) - 1) and (expression[i + 1].isdigit() or expression[i + 1] == "."):
                    i += 1
                    num += expression[i]

                asNumber = float(num)

                result.append(asNumber)

            elif expression[i] in OPERATORS:
                # This helps to take care of cases where the - sign is used to negate a number rather than subtracting.
                # In such cases the - sign is converted into a ~ sign which the evaluator interprets as a negation operator
                if expression[i] == "-":
                    if i == 0 or (expression[i - 1] in OPERATORS) or expression[i - 1] == "(":
                        expression[i] = "~"

                # This helps to take care of cases where there's an implicit multiplication between a number or parentheses
                # and a function, such as "3cos(27)" or "(4 - 2)ln(50)". In both cases we have to insert the × operator in between
                if ((expression[i] in UNARY_OPERATORS) and expression[i] != "~" and expression[i] != "!") and i != 0 \
                        and (expression[i - 1].isdigit() or expression[i - 1] == ")" or (expression[i] in CONSTANTS)):
                    stack.append("×")

                while len(stack) > 0 and (not stack[len(stack) - 1] == "(") and self.__hasHigherPrecedence(stack[len(stack) - 1], expression[i]):
                    result.append(stack.pop())

                # If the operator is a factorial operator ("!"), immediately insert it at the end of
                # the postfix expression after its operand since "!" is already a postfix notation
                if expression[i] == "!":
                    result.append(expression[i])
                else:
                    stack.append(expression[i])

            elif expression[i] in CONSTANTS:
                # More implicit multiplication
                if i != 0 and (expression[i - 1].isdigit() or expression[i - 1] == ")" or (expression[i - 1]) in CONSTANTS):
                    stack.append("×")

                if expression[i] == "π":
                    result.append(math.pi)
                elif expression[i] == "e":
                    result.append(math.e)

            elif expression[i] == "(":
                # Implicit multiplication cases
                if i != 0 and (expression[i - 1].isdigit() or expression[i - 1] == ")" or (expression[i] in CONSTANTS)):
                    stack.append("×")

                stack.append("(")

            elif expression[i] == ")":
                while len(stack) > 0 and not stack[len(stack) - 1] == "(":
                    result.append(stack.pop())

                stack.pop()

            i += 1

        while len(stack) > 0:
            result.append(stack.pop())

        return result

    def __hasHigherPrecedence(self, first, second):
        '''
        Returns true if the first argument has a higher precedence
        than the second argument
        '''
        return OPERATORS.index(first) < OPERATORS.index(second)

    def __evaluatePostfix(self, expression):
        '''
        Evaluates the postfix expression as produced by the `__infixToPostfix`
        function
        '''
        # Could be removed. Just placed it here so I could
        # see the values everytime I ran the program
        print(expression)

        stack = []

        for element in expression:
            if type(element) == float:
                stack.append(element)

            elif element in OPERATORS:
                answer = 0

                print(stack)  # Could also be removed or just commented out

                if element in UNARY_OPERATORS:
                    answer = self.__operation(element, stack.pop())
                else:
                    answer = self.__operation(
                        element, stack.pop(), stack.pop())

                stack.append(answer)

        return stack.pop()

    def __operation(self, operator, operand2, operand1=0):
        """
        Used by the `__evaluatePostfix` function to perform individual operations
        """
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "×":
            return operand1 * operand2
        elif operator == "÷":
            return operand1 / operand2
        elif operator == "^":
            return math.pow(operand1, operand2)
        elif operator == "!":
            return math.factorial(operand2)
        elif operator == "sin":
            return math.sin(operand2)
        elif operator == "cos":
            return math.cos(operand2)
        elif operator == "tan":
            return math.tan(operand2)
        elif operator == "asin":
            return math.asin(operand2)
        elif operator == "acos":
            return math.acos(operand2)
        elif operator == "atan":
            return math.atan(operand2)
        elif operator == "~":
            return -1 * operand2
        elif operator == "ln":
            return math.log(operand2)
        elif operator == "log":
            return math.log10(operand2)
        elif operator == "√":
            return math.sqrt(operand2)
        elif operator == "P":
            return math.factorial(operand1) / math.factorial(operand1 - operand2)
        elif operator == "C":
            return math.factorial(operand1) / (math.factorial(operand1 - operand2) * math.factorial(operand2))


Calculator()
