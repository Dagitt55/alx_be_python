class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b
