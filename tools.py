from datetime import datetime


def datetime_tool(_: str) -> str:
    try:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        return f"Tool error: {str(e)}"


def calculator_tool(question: str) -> str:
    try:
        expr = question.lower().replace("calculate", "").strip()
        if not expr:
            return "Tool error: no expression provided."
        allowed_chars = set("0123456789+-*/(). %")
        if not all(ch in allowed_chars for ch in expr):
            return "Tool error: unsupported characters in expression."
        result = eval(expr, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Tool error: {str(e)}"