import sys

def parse_number_word(word, num_dict):
    if 'c' not in word:
        if word in num_dict:
            return num_dict[word]
        else:
            return None
    
    parts = word.split('c')
    num_str = ""
    for part in parts:
        if part in num_dict:
            num_str += str(num_dict[part])
        else:
            return None
    
    return int(num_str)

def solve():
    op_words = {"add", "sub", "mul", "rem", "pow"}
    num_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    try:
        line = sys.stdin.readline().strip()
        if not line:
            return
        
        words = line.split()
    except (IOError, ValueError):
        return

    # Phase 1: Word Validation
    for word in words:
        if word in op_words:
            continue
        if parse_number_word(word, num_words) is not None:
            continue
        
        print("expression evaluation stopped invalid words present")
        return

    # Phase 2: Expression Evaluation
    
    # We use a mutable list as a queue to consume tokens
    tokens = words[:]
    
    def evaluate(token_list):
        if not token_list:
            raise ValueError("Not enough operands")
            
        token = token_list.pop(0)

        if token in op_words:
            op1 = evaluate(token_list)
            op2 = evaluate(token_list)

            if token == "add":
                return op1 + op2
            elif token == "sub":
                return op1 - op2
            elif token == "mul":
                return op1 * op2
            elif token == "rem":
                # Handle division by zero, although problem says no negative numbers and no floats.
                # A remainder operation with 0 can be a problem.
                if op2 == 0:
                    raise ZeroDivisionError("Division by zero")
                return op1 % op2
            elif token == "pow":
                return op1 ** op2
        else:
            # It must be a number word, as validated earlier
            num_val = parse_number_word(token, num_words)
            if num_val is None:
                raise ValueError("Invalid number word after validation")
            return num_val
    
    try:
        result = evaluate(tokens)
        
        # Check if all tokens were consumed
        if tokens:
            print("expression is not complete or invalid")
        else:
            print(result)

    except (ValueError, IndexError, ZeroDivisionError):
        # A simple IndexError can indicate not enough operands.
        # ZeroDivisionError is for the rem operation.
        print("expression is not complete or invalid")


if __name__ == "__main__":
    solve()
