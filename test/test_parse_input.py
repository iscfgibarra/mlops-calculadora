from src import parse_input, parse_float, execute_operation
import pytest


def test_parse_input_ok():
    ok, a, op, b = parse_input("1/2*2")
    assert ok is True
    assert a == "1/2"
    assert op == "*"
    assert b == "2"


def test_parse_input_error():
    ok, a, op, b = parse_input("defe * 2")
    assert ok is False


def test_parse_operator_ok():
    float_operator = parse_float("1/2")
    assert float_operator == 0.5


def obtener_datos_test_execute_operation():
    return [("3", "*", "1/2", 1.5), ("2", "+", "20", 22), ("5", "-", "2", 3), ("10", "/", "5", 2)]


@pytest.mark.parametrize('a,oper,b,esperado', obtener_datos_test_execute_operation())
def test_execute_operations_ok(a, oper, b, esperado):
    result = execute_operation(a + ' ' + oper + ' ' + b)
    assert result == esperado

