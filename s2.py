def check_parentheses(input_str):
    stack = []
    result = ""

    for char in input_str:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                result += "x"
            else:
                stack_top = stack.pop()
                if (char == ")" and stack_top != "(") or \
                   (char == "]" and stack_top != "[") or \
                   (char == "}" and stack_top != "{"):
                    result += "?"
        else:
            result += char


    while stack:
        result += "?"

    return result


sample_inputs = [
    "7896)))))))))",
    "((769679769))))))",

]

for input_str in sample_inputs:
    output = check_parentheses(input_str)
    print(f"输入：{input_str}")
    print(f"输出：{output}\n")
