"""Programming assignment for NORITEX.com software engineering position.

Su tarea es IMPLEMENTAR la función evaluate() a continuación para la especificación
proporcionado en la cadena de documentación.
Si cree que las funciones auxiliares serían útiles, no dude en
escríbelos Puede cambiar cualquier cosa en este archivo, excepto que no está permitido
para alterar el nombre o la firma de la función de evaluación ().

Aunque le proporcionamos algunos casos de prueba, no asuma que estos cubren
todos los casos de esquina, y podemos usar un conjunto diferente de entradas para validar su
solución. Analizaremos su solución tanto para la corrección como para
estilo.

----------------------------------------------

Your task is to implement the function evaluate() below to the specification
provided in the documentation string.
If you feel that auxiliary helper functions would be helpful, feel free to
write them. You may change anything in this file except you are not permitted
to alter the name or function signature of evaluate().

Although we provide you with some test cases, do not assume that these cover
all corner cases, and we may use a different set of inputs to validate your
solution. We will be looking at your solution both for correctness and for
style.

Best of luck!
"""

# =============================================================================
#
# Implement this function
#
# =============================================================================

def evaluate(m):
    for i in range(len(m)):
        for x in range(len(m[i])):
            try:
                m[i][x] = int(m[i][x])
            except:
                m[i][x] = find_calc(m[i][x], m)
    return m

def find_calc(value, iterator):
    columns = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if value == None or len(value) <= 0:
        raise ValueError

    if value[0] != "=":
        raise ValueError
    
    
    if value[0] == "=":
        iterable = value[2:]
        op = ""
        for z in iterable:
            if z == "+":
                op = "+"
                break

            if z == "-":
                op = "-"
                break

            if z == "*":
                op = "*"
                break
                
            if z == "/":
                op = "/"
                break


    value_format = value[1:]    
    value1 = ""
    value2 = ""
    
    if len(value_format) > 2:
        value1, value2 = value_format.split(op)
    else:
        value1 = value_format

    if value1 == None or value1 == "":
        raise ValueError    

    column_index = ""
    column_index2 = ""
    row_index = 0
    row_index2 = 0
    result = ""
    val1 = value1.strip()
    val2 = value2.strip()
    column_index = find_column_index(val1)
    column_index2 = find_column_index(val2)
    new_iter = iterator

    if column_index >= 0 :
        row_index = find_row_index(val1)

        if row_index > len(new_iter) or column_index > len(new_iter):
            raise ReferenceError
        
        if len(val1) < 3 and val2 == "":
            if op != "" and val2 == "":
                raise ValueError

            result = new_iter[row_index][column_index]
            return result

        if column_index2 >= 0:
            row_index2 = find_row_index(val2)
            return get_result(op, new_iter[row_index][column_index], new_iter[row_index2][column_index2])
        else:
            return get_result(op, new_iter[row_index][column_index], val2)

        
    else:
        result = get_result(op, val1, val2)

    return result


def find_column_index(value):
    columns = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    new_value = ""

    if value[:1] in "-/*+":
        new_value = value[1:2]
    else:
        new_value = value[:1]

    try:
        return columns.index(new_value.upper())
    except:
        return -1

def find_row_index(value):
    return int(value[1:]) - 1


def get_result(op, value1, value2):
    
    if isinstance(value1, str):
        if value1.isdigit():
            try:
                value1 = int(value1)
            except:
                value1 = float(value1)
        else:
            if value1[0] == "-":
                try:
                    value1 = int(value1)
                except:
                    value1 = float(value1)

    if isinstance(value2, str):
        if value2.isdigit():
            try:
                value2 = int(value2)
            except:
                value2 = float(value2)
        else:
            if value2[0] == "-":
                try:
                    value2 = int(value2)
                except:
                    value2 = float(value2)



    if isinstance(value1, int) or isinstance(value1, float):
        if isinstance(value2, int) or isinstance(value2, float):
            
            if value1 == 0 and value2 == 0:
                raise ZeroDivisionError

            match op:
                case "+": return value1 + value2
                case "-": return value1 - value2
                case "*": return value1 * value2
                case "/": return value1 / value2
        
        else:
            if isinstance(value1, int) or isinstance(value1, float) and isinstance(value2, str):
                raise ValueError
            
            if isinstance(value2, str):
                return value1

            raise ValueError

    else:
        if isinstance(value1, str):
                print("")

        raise ValueError
            

    """ if value1 != "" and value2 != "":
        if isinstance(value2, int) <= 0 or isinstance(value2, float) <= 0  and op == "/":
            raise ZeroDivisionError

    
    if value1 != "" and value2 != "" and op != "":
        match op:
            case "+": return value1 + value2
            case "-": return value1 - value2
            case "*": return value1 * value2
            case "/": return value1 / value2
    else:
        if value2 == "" and value1 != "" and op == "":
             return value1
        else:
            if value2 != "" and value1 == "" and op == "":
                return value2
            else:
                raise ValueError """



# =============================================================================
#
# Some example inputs and solutions to test against
#
# =============================================================================



testcase = []
solution = []

# Case: simple spreadsheet with strings and ints
testcase.append(
    [
        [1, "2"],
        ["3", 4]
    ]
)
solution.append (
    [
        [1, 2],
        [3, 4]
    ]
)

# Case: simple (non-recursive) formulas
testcase.append(
    [
        [1, "=A1+1"],
        [3, "=A2+1"]
    ]
)
solution.append(
    [
        [1, 2],
        [3, 4]
    ]
)

testcase.append(
    [
        [1, "=1-1"],
        [3, "=A2+1"]
    ]
)
solution.append(
    [
        [1, 0],
        [3, 4]
    ]
)


# Case: formulas referencing two cells
testcase.append(
    [
        [1,     "=A1+1", "=A1 + B1"],
        ["=B1", "3",     "=C1 + B2"]
    ]
)
solution.append(
    [
        [1, 2, 3],
        [2, 3, 6]
    ]
)

# Cases: formula referencing cells out of range
testcase.append(
    [
        [1,         "=A5 + 2"],
        ["=B1 + 1", "=A2 + 1"]
    ]
)
solution.append(ReferenceError)

testcase.append([ [1, "=C1"] ])
solution.append(ReferenceError)

# Case: circular dependencies
testcase.append(
    [
        ["=B1 + 1", "=A1 + 1"]
    ]
)
solution.append(ValueError)

# Case: highly recursive spreadsheet, all operations represented
testcase.append(
    [
        [ "=C1+5", "=A3/2", "=c2-1" ],
        [ "=b3+7",       1, "=B1*4" ],
        [ "=B2+5", "=a1/5", "=A2-2" ]
    ]
)
solution.append(
    [
        [ 16,   3,   11   ],
        [ 10.2, 1,   12   ],
        [  6,   3.2,  8.2 ]
    ]
)

# Cases: malformed formulas
testcase.append([ [ 1, "=A1 +" ] ] )
solution.append(ValueError)

testcase.append([ [ 1, "=A1+5+6+7" ] ])
solution.append(ValueError)

testcase.append([ [ 1, "=A1 $ A1" ] ])
solution.append(ValueError)

# Case: division by zero
testcase.append([ [ 1, "=A1 - 1", "=A1 / B1" ] ])
solution.append(ZeroDivisionError)

# Case: negative numbers
testcase.append([ [ 1, "=A1 * -1" ] ])
solution.append([ [ 1, -1 ] ])

testcase.append([ [ -1, "=A1 * -5" ] ])
solution.append([ [ -1, 5 ] ])

testcase.append([ [ 1, "=-2 + a1" ] ])
solution.append([ [ 1, -1 ] ])

testcase.append([ [ 1, "=A1 + -5" ] ])
solution.append([ [ 1, -4 ] ])

testcase.append([ [ 1, "=A-1 + 1" ] ])
solution.append(ValueError)

testcase.append([ [ 1, "=-A1 + 1" ] ])
solution.append([ [ 1, 0 ] ])

# Case: Errors in input
testcase.append([ [ -1, "=A1 + - 5" ] ])
solution.append(ValueError)

testcase.append([ [ "" ] ])
solution.append(ValueError)

testcase.append([ [ None ] ])
solution.append(ValueError)

testcase.append([ [ None, "=A1" ] ])
solution.append(ValueError)

testcase.append([ [ "A1" ] ])
solution.append(ValueError)


def validate(proposed, actual):
    """Check if the proposed solution is the same as the actual solution.

    Feel free to modify this function as we will be testing your code with
    our copy of this function.

    :param proposed: The proposed solution
    :param actual: The actual solution
    :return: True if they are the same. Else, return False.
    """
    if proposed is None:
        print ("Oops! Looks like your proposed result is None.")
        return False
    proposed_items = [item for sublist in proposed for item in sublist]
    actual_items = [item for sublist in actual for item in sublist]
    if len(proposed_items) != len(actual_items):
        print ("Oops! There don't seem to be the same number of elements.")
        return False
    if proposed_items != actual_items:
        print ("Oops! Looks like your proposed solution is not right...")
        return False
    return True


# =============================================================================
#
# A simple main function for you to run. You should be able to test your
# implementation by simply running this module. E.g.
#   python spreadsheet.py
#
# =============================================================================

def print_error(solution, result):
    """Helper to print the error string"""
    print ("    Expected {}({}), got {}({})".format(
        type(solution), solution, type(result), result))

 
if __name__ == '__main__':
    """The main entry point for this module.

    The main entry point for the function that runs a couple tests to validate
    the implementation of evaluate().
    """

    # The number of test cases that are correct
    correct = 0

    for i in range(len(testcase)):

        print ("Test {}.".format(i))
        
        try:
            result = evaluate(testcase[i])
        except Exception as exc:
            result = exc

        # If the result is a matrix, make sure we were expecting a matrix
        if isinstance(result, list):
            if isinstance(solution[i], list):
                if validate(result, solution[i]):
                    print ("    OK.")
                    correct += 1
                else:
                    print ("    Results don't match")
            else:
                print_error(solution[i], result)

        # If the result is an error, make sure we were expecting an error
        else:
            if isinstance(solution[i], list):
                print_error(solution[i], result)
            else:
                if result.__class__ == solution[i]:
                    print ("    OK.")
                    correct += 1
                else:
                    print_error(solution[i], result)

    print ("------------------------------------------------------")
    print ("You got {} out of {} correct.".format(correct, len(testcase)))
