import json
import logging
import xmltodict


def convert_xml_to_json(xml_data: str) -> str:
    data_dict = xmltodict.parse(xml_data)
    return json.dumps(data_dict, indent=4)


def save_json_output(json_data: str, output_file: str) -> None:
    with open(output_file, 'w') as file:
        file.write(json_data)
    logging.debug(f"JSON output saved to {output_file}")
