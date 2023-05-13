"""Dictionary format formater."""


def stylish(diff_list):
    """Converts a list of differences to dictionary format. Returns string."""
    return get_diff_stylish(diff_list)


def get_diff_stylish(diff_list, level=0):
    result = '{\n'
    indent = '  '
    for i in range(level):
        indent += '    '
    diff_list.sort(key=lambda x: x['name'])
    for node in diff_list:
        if node['status'] == 'nested':
            data = get_diff_stylish(node['children'], level + 1)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'not changed':
            data = format_data(node['data'], indent)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'added':
            data = format_data(node['data'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
        if node['status'] == 'deleted':
            data = format_data(node['data'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
        if node['status'] == 'changed':
            data = format_data(node['data before'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
            data = format_data(node['data after'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
    result += indent[:-2] + '}'
    return result


def format_data(data, indent):
    """Parses the data. Returns it in the correct format as a string."""
    if type(data) is dict:
        indent += '    '
        result = '{\n'
        for key in data.keys():
            value = format_data(data[key], indent)
            result += indent + '  ' + key + ': ' + value + '\n'
        result += indent[:-2] + '}'
    elif data is False:
        result = 'false'
    elif data is True:
        result = 'true'
    elif data is None:
        result = 'null'
    else:
        result = str(data)
    return result