def arithmetic_arranger(problems, show_solution=False):
    if len(problems) > 5: return "Error: Too many problems."

    def err_check(problem):
        try:
            op1, operator, op2 = problem.split()
        except:
            return "Error: Something is wrong with the problems list..."
        try:
            if operator != "+" and operator != "-":
                raise BaseException
        except:
            return "Error: Operator must be '+' or '-'."
        try:
            int(op1)
            int(op2)
        except:
            return "Error: Numbers must only contain digits."
        try:
            if len(op1) > 4 or len(op2) > 4:
                raise BaseException
        except:
            return "Error: Numbers cannot be more than four digits."
        return None

    for problem in problems:
        problem_check = err_check(problem)
        if problem_check: return problem_check

    arranged_problems, row1, row2, row3, row4, solution = "","","","","",""
    for i in range(len(problems)):
        op1, operator, op2 = problems[i].split()
        solution = str(eval(problems[i]))
        print(solution)
        longest_op = max(len(op1), len(op2))
        if i == 0:
            row3 += "-" * (longest_op + 2)
            row2 += operator + " " + op2.rjust(longest_op)
            row1 += op1.rjust(longest_op + 2)
            if show_solution:
                row4 +=solution.rjust(longest_op + 2)
        else:
            row2 += "    " + operator + " " + op2.rjust(longest_op)
            row3 += "    " + "-" * (longest_op + 2)
            row1 += "    " + op1.rjust(longest_op + 2)
            if show_solution:
                row4 += "    " + solution.rjust(longest_op + 2)
    if show_solution:
        arranged_problems = f"{row1}\n{row2}\n{row3}\n{row4}"
    else:
        arranged_problems = f"{row1}\n{row2}\n{row3}"
    return arranged_problems
