# The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.
#To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

def get_sensor_data():
    with open('./modules/day1_data.txt') as f:
        data = [line for line in f]
    return data

def depth_measurement_increase(sensor_inputs):
    keys = []
    increases = 0
    decreases = 0
    same = 0
    size_dataset = len(sensor_inputs)
    for num in range(0, size_dataset):
        keys.append(num)
    sensor_map = dict(zip(keys, sensor_inputs))

    for key in sensor_map:
        if key == 0:
            continue
        else:
            current_datum = sensor_map[key]
            prev_datum = sensor_map[key-1]

            if current_datum > prev_datum:
                increases += 1

    return increases


def sum_depth_measurement_increase(sensor_inputs):
    keys = []
    increases = 0
    size_dataset = len(sensor_inputs)
    last_window = size_dataset-3
    for num in range(0, len(sensor_inputs)):
        keys.append(num)
    sensor_map = dict(zip(keys, sensor_inputs))

    for key in sensor_map:
        if key >= last_window:
            continue

        else:
            window_a = int(sensor_map[key]) + int(sensor_map[key+1]) + int(sensor_map[key+2])
            window_b = int(sensor_map[key+1]) + int(sensor_map[key+2]) + int(sensor_map[key+3])

            if window_b > window_a:
                increases += 1

    return increases

sensor_inputs = get_sensor_data()
increases_raw = depth_measurement_increase(sensor_inputs)
increases_noise_correction = sum_depth_measurement_increase(sensor_inputs)

print(">", increases_raw)
print(">", increases_noise_correction)
