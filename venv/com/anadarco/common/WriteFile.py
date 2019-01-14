import csv


class Write:

    def __init__(self, output_reading):
        with open('output.csv', mode='w') as csv_file:
            fields = ["Platform name", "Total Gap Time", "Average Gap Time", "Min Value", "Max Flight Time"]
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()
            for each in output_reading:
                writer.writerow({"Platform name": each.platform_name, "Total Gap Time": each.total_gap_time,
                                 "Average Gap Time": each.avg_gap_time, "Min Value": each.min_value,
                                 "Max Flight Time": each.max_flight_time})

            print("Writing finished")
