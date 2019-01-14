import InputReading
import OutputReading
import Common
from Common import convert_epoch_to_time

def calculate(all_readings):
    output_reading_list = []
    count = 0
    min_value = 0
    diff = 0
    total_gap = 0
    max_flight_time = 0
    for i in range(len(all_readings)):
        reading1 = all_readings[i]
        reading2 = all_readings[i + 1] if i < len(all_readings) - 1 else ["0", "0", "0", "0", "0"]
        input_reading1 = InputReading.Input(reading1[0], int(reading1[1]), int(reading1[2]), int(reading1[3]),
                                            int(reading1[4]))
        input_reading2 = InputReading.Input(reading2[0], int(reading2[1]), int(reading2[2]), int(reading2[3]),
                                            int(reading2[4]))
        if input_reading1.platform_name == input_reading2.platform_name:
            count += 1
            diff = input_reading2.reading_receive_time - input_reading1.reading_receive_time
            total_gap = diff + total_gap

            if input_reading1.reading_value < min_value:
                min_value = input_reading1.reading_value

            if input_reading2.reading_value < min_value:
                min_value = input_reading2.reading_value

            flight_time_reading1 = input_reading1.reading_receive_time - input_reading1.reading_send_time
            flight_time_reading2 = input_reading2.reading_receive_time - input_reading2.reading_send_time

            if flight_time_reading1 > max_flight_time:
                max_flight_time = flight_time_reading1

            if flight_time_reading2 > max_flight_time:
                max_flight_time = flight_time_reading2

        else:
            if count == 0:
                min_value = input_reading1.reading_value
                max_flight_time = input_reading1.reading_receive_time - input_reading1.reading_send_time
                output_reading = OutputReading.Output(input_reading1.platform_name, "0", "0", min_value,
                                                      Common.convert_epoch_to_time(max_flight_time))
            else:
                output_reading = OutputReading.Output(input_reading1.platform_name,
                                                      Common.convert_epoch_to_time(total_gap),
                                                      Common.convert_epoch_to_time(
                                                          total_gap / count if count > 0 else total_gap),
                                                      min_value,
                                                      Common.convert_epoch_to_time(max_flight_time))
            output_reading_list.append(output_reading)
            count = 0
            min_value = 0
            diff = 0
            total_gap = 0
            max_flight_time = 0

    return output_reading_list
