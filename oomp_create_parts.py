
import importlib
import oomp

part_types = []

part_types.append("breakout_board")
part_types.append("button")
part_types.append("capacitor")
part_types.append("crystal")
part_types.append("diode")
part_types.append("header")
part_types.append("ic")
part_types.append("led")
part_types.append("mounting_hole")
part_types.append("pmic")
part_types.append("resistor")
part_types.append("socket")



for type in part_types:
    importlib.import_module(f'oomp_create_parts_{type}')

def load_parts(**kwargs):
    print("loading parts from modules")
    for type in part_types:
        importlib.import_module(f'oomp_create_parts_{type}').load_parts(**kwargs)


def load_parts_from_yaml(**kwargs):
    print("loading parts from yaml")
    import yaml
    with open("parts.yaml", "r") as infile:
        parts = yaml.load(infile, Loader=yaml.FullLoader)
    oomp.parts = parts

def save_parts_to_yaml(**kwargs):
    print("saving parts to yaml")
    import yaml
    with open("parts.yaml", "w") as outfile:
        yaml.dump(oomp.parts, outfile, indent=4)

def save_parts_to_individual_yaml_files(**kwargs):
    print("saving parts to yaml")
    import yaml
    for part_id in oomp.parts:
        part = oomp.parts[part_id]
        del part['make_files']
        yaml_file = f"parts/{part_id}/working/working.yaml"
        with open(yaml_file, "w") as outfile:
            print(f"writing {yaml_file}")
            yaml.dump(part, outfile, indent=4)