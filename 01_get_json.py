import sys
import json
import glob
from jsonpath_ng import jsonpath, parse
def get_value_by_jsonpath(json_filepath, jsonpath):
    with open(json_filepath, 'r') as json_file:
        json_data = json.load(json_file)
    jsonpath_expression = parse(jsonpath)
    match = jsonpath_expression.find(json_data)
    return match[0].value
if __name__ == "__main__":
    rule_list = [
        {
            "jsonpath": '$.utterance.[*].original_form',
            "valid_values": [
                'CANCER',
                'I',
                'P',
                'LSIL',
                'HSIL',
            ]
        },
    ]
    #glob_result = glob.glob('/home/ubuntu/passbucket/local/test/json/FILES_/*.json')
    glob_result = glob.glob('/home/ubuntu/PASSBUCKET/src_dir/*.json')
    for f in glob_result:
        for rule in rule_list:
            value = get_value_by_jsonpath(f, rule['jsonpath'])
            print(value)

            

#            if value not in rule['valid_values']:
#                print("the value '"+value+"' is NOT valid")
#            else:
#                print("the value '"+value+"' is valid")
