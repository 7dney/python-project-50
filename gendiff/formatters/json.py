"""Json format formater."""


def format_json(diff_list):
    return json.dumps(diff_list, indent=4)