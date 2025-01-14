def extract_parameter(unit_name, parameter_name, value):
    try:
        extracted_value = unit_operations_data[unit_name][parameter_name][value]
    except KeyError or UnboundLocalError:
        return "Invalid input"
    return (f"{unit_name}_{parameter_name}_{extracted_value}")