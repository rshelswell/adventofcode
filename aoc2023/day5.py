import re
#import itertools
from pprint import pprint

def get_mapping(line) -> dict:
    """Return dict"""
    map_params = re.findall(r'(\d+)', line)
    ret = dict()

    # source = map_params[1]
    # destination = map_params[0]
    s_d = int(map_params[0]) - int(map_params[1])
    # map_range = map_params[2]

    ret.update({(int(map_params[1]), int(map_params[1]) + int(map_params[2])):s_d})

#    for i in range(int(map_params[2])):
#        ret.update({int(map_params[1])+i: int(map_params[0])+i})
    # print(ret)
    return ret

def read_mapping(n, mapping):
    for ss, diff in mapping.items():
        if n >= ss[0] and n < ss[1]:
            return n + diff
    return n

def read_mapping2(n, mapping):
    for mps in mapping:
        if n >= mps[0] and n < mps[1]:
            return mps[2] - mps[0] + n
    return n

def get_mapping2(line):
    ldata = [int(i) for i in re.findall(r'(\d+)', line)]
    return (ldata[1], ldata[1] + ldata[2] - 1, ldata[0])

def day5a():
    file5 = open(r'aoc2023/day5.input', 'r')
    Lines = file5.readlines()
    file5.close()
    seeds = []
    seed_soil = dict()
    soil_fertiliser = dict()
    fertiliser_water = dict()
    water_light = dict()
    light_temperature = dict()
    temperature_humidity = dict()
    humidity_location = dict()
    section = 1
    loc = 2**63-1
    for line in Lines:
        if line == "\n":
            section += 1
            continue
        if section == 1:
            # seed list
            seeds = [int(i) for i in re.findall(r'(\d+)', line)]
        elif section == 2:
            # seed to soil map
            if ":" in line:
                continue
            seed_soil.update(get_mapping(line))
        elif section == 3:
            # soil-to-fertilizer map
            if ":" in line:
                continue
            soil_fertiliser.update(get_mapping(line))
        elif section == 4:
            # fertilizer-to-water map
            if ":" in line:
                continue
            fertiliser_water.update(get_mapping(line))
        elif section == 5:
            # water-to-light map
            if ":" in line:
                continue
            water_light.update(get_mapping(line))
        elif section == 6:
            # light-to-temperature map
            if ":" in line:
                continue
            light_temperature.update(get_mapping(line))
        elif section == 7:
            # temperature-to-humidity map
            if ":" in line:
                continue
            temperature_humidity.update(get_mapping(line))
        elif section == 8:
            # humidity-to-location map
            if ":" in line:
                continue
            humidity_location.update(get_mapping(line))
    maps = [seed_soil, soil_fertiliser, fertiliser_water, water_light, 
            light_temperature, temperature_humidity, humidity_location]
    for seed in seeds:
        # print(seed)
        s = read_mapping(seed, seed_soil)
        f = read_mapping(s, soil_fertiliser)
        w = read_mapping(f, fertiliser_water)
        l = read_mapping(w, water_light)
        t = read_mapping(l, light_temperature)
        h = read_mapping(t, temperature_humidity)
        loc = min(read_mapping(h, humidity_location), loc)
    print(f"location = {loc}")


def day5b():
    file5 = open(r'aoc2023/day5.input', 'r')
    Lines = file5.readlines()
    file5.close()
    seeds = []
    seed_soil = []
    soil_fertiliser = []
    fertiliser_water = []
    water_light = []
    light_temperature = []
    temperature_humidity = []
    humidity_location = []
    section = 1
    loc = 2**63-1
    for line in Lines:
        #print(section)
        if line == "\n":
            section += 1
            continue
        if section == 1:
            # seed list
            seed_data = [int(i) for i in re.findall(r'(\d+)', line)]
            seeds = list(zip(seed_data[::2], seed_data[1::2]))
        elif section == 2:
            # seed to soil map
            if ":" in line:
                continue
            seed_soil.append(get_mapping2(line))
        elif section == 3:
            # soil-to-fertilizer map
            if ":" in line:
                continue
            soil_fertiliser.append(get_mapping2(line))
        elif section == 4:
            # fertilizer-to-water map
            if ":" in line:
                continue
            fertiliser_water.append(get_mapping2(line))
        elif section == 5:
            # water-to-light map
            if ":" in line:
                continue
            water_light.append(get_mapping2(line))
        elif section == 6:
            # light-to-temperature map
            if ":" in line:
                continue
            light_temperature.append(get_mapping2(line))
        elif section == 7:
            # temperature-to-humidity map
            if ":" in line:
                continue
            temperature_humidity.append(get_mapping2(line))
        elif section == 8:
            # humidity-to-location map
            if ":" in line:
                continue
            humidity_location.append(get_mapping2(line))
    print("number of seeds", len(seeds))
    print("Finished mapping")
    print("seed_soil", len(seed_soil))
    print("soil_fertiliser", len(soil_fertiliser))
    print("fertiliser_water", len(fertiliser_water))
    print("water_light", len(water_light))
    print("light_temperature", len(light_temperature))
    print("temperautr_humidity", len(temperature_humidity))
    print("humidity_location", len(humidity_location))
    pprint(humidity_location)
    return
    for sr in seeds:
        for sd in range(sr[0], sr[0]+sr[1]):
            s = read_mapping2(sd, seed_soil)
            f = read_mapping2(s, soil_fertiliser)
            w = read_mapping2(f, fertiliser_water)
            l = read_mapping2(w, water_light)
            t = read_mapping2(l, light_temperature)
            h = read_mapping2(t, temperature_humidity)
            loc = min(read_mapping2(h, humidity_location), loc)
    print(f"location = {loc}")

def day5b2():
    file5 = open(r'aoc2023/day5.input', 'r')
    Lines = file5.readlines()
    file5.close()
    seeds = []
    seed_soil = []
    soil_fertiliser = []
    fertiliser_water = []
    water_light = []
    light_temperature = []
    temperature_humidity = []
    humidity_location = []
    section = 1
    loc = 2**63-1
    for line in Lines:
        #print(section)
        if line == "\n":
            section += 1
            continue
        if section == 1:
            # seed list
            seed_data = [int(i) for i in re.findall(r'(\d+)', line)]
            seeds = list(zip(seed_data[::2], seed_data[1::2]))
        elif section == 2:
            # seed to soil map
            if ":" in line:
                continue
            seed_soil.append(get_mapping2(line))
        elif section == 3:
            # soil-to-fertilizer map
            if ":" in line:
                continue
            soil_fertiliser.append(get_mapping2(line))
        elif section == 4:
            # fertilizer-to-water map
            if ":" in line:
                continue
            fertiliser_water.append(get_mapping2(line))
        elif section == 5:
            # water-to-light map
            if ":" in line:
                continue
            water_light.append(get_mapping2(line))
        elif section == 6:
            # light-to-temperature map
            if ":" in line:
                continue
            light_temperature.append(get_mapping2(line))
        elif section == 7:
            # temperature-to-humidity map
            if ":" in line:
                continue
            temperature_humidity.append(get_mapping2(line))
        elif section == 8:
            # humidity-to-location map
            if ":" in line:
                continue
            humidity_location.append(get_mapping2(line))
    print("number of seeds", len(seeds))
    print("Finished mapping")
    print("seed_soil", len(seed_soil))
    print("soil_fertiliser", len(soil_fertiliser))
    print("fertiliser_water", len(fertiliser_water))
    print("water_light", len(water_light))
    print("light_temperature", len(light_temperature))
    print("temperautr_humidity", len(temperature_humidity))
    print("humidity_location", len(humidity_location))
    pprint(humidity_location)
    return
    for sr in seeds:
        for sd in range(sr[0], sr[0]+sr[1]):
            s = read_mapping2(sd, seed_soil)
            f = read_mapping2(s, soil_fertiliser)
            w = read_mapping2(f, fertiliser_water)
            l = read_mapping2(w, water_light)
            t = read_mapping2(l, light_temperature)
            h = read_mapping2(t, temperature_humidity)
            loc = min(read_mapping2(h, humidity_location), loc)
    print(f"location = {loc}")

if __name__ == "__main__":
    day5b2()