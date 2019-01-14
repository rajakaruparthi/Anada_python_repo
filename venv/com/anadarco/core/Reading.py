import os
import WriteFile
import Calculations
import PathFile
from PathFile import get_path
from Calculations import calculate


class ReadFile:

    def read(self, path):
        lines = [line.rstrip('\n') for line in open(path)]
        lines.sort()
        return lines

    def format_data(self, lines):
        all_readings = []
        for line in lines:
            array = line.split(",")
            all_readings.append(array)
        return all_readings


app = ReadFile()
lines = app.read(PathFile.get_path())

formatted_data = app.format_data(lines)

output_reading = Calculations.calculate(formatted_data)

WriteFile.Write(output_reading)