import os
import sys
import Calculations
from Calculations import calculate
sys.path.append("..")
import common.WriteFile as WriteFile
import common.PathFile as PathFile
from common.PathFile import get_path

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
all_lines = app.read(PathFile.get_path())

formatted_data = app.format_data(all_lines)

output_reading = Calculations.calculate(formatted_data)

WriteFile.Write(output_reading)