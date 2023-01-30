def build_query_string(params):
    result = ''
    sorted_params = dict(sorted(params.items()))
    for elem in sorted_params:
        result += str(elem) + '=' + str(sorted_params[elem]) + '&'
    result = result[:len(result) - 1]
    return result

params = {'per': 10, 'page': 1}
build_query_string(params)