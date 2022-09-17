

def instructions(software):
    if software == "all":
        all_directions = []
        with open("C:\\Users\\jacks\\coding\\Python_Projects\\Arch Reinstall\\arch_reconfig.txt", "r") as List:
            software_list = List.read()
        software_list = software_list.split(" ")
        for i in software_list:
            with open(f"C:\\Users\\jacks\\coding\\Python_Projects\\Arch Reinstall\\{i}.txt", "r") as directions:
                specific_directions = directions.read()
            all_directions.append(f"Directions for {i}: {specific_directions}")
        for i in all_directions:
            yield (f"{i}\n")

    else:
        with open(f"C:\\Users\\jacks\\coding\\Python_Projects\\Arch Reinstall\\{software}.txt", "r") as directions:
            specific_directions = directions.read()
        yield specific_directions
        

wanted_instructions = input("which software instructions do you want?   ")


# needs to be in a for loop even if software isn't all because since it has a yield in the function at all it automatically returns a generator no matter what. 

for i in instructions(wanted_instructions):
    print(i)
