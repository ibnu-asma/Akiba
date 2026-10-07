class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        kelvin = celsius + 273.15
        return [kelvin, (celsius * 1.80) + 32.00]
        