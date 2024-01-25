def get_by_data_id(data_id):
    return f"//*[data-id={data_id}]"

def get_by_class_css(selector):
    return f'[class={selector}]'