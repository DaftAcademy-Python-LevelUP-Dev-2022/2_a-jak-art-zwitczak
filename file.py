from functools import wraps


def num_converter(number_str):
    sum_a = 0
    if number_str[0] == "-":
        for el in number_str[1:]:
            sum_a -= int(el)
    else:
        for el in number_str:
            sum_a += int(el)

    return sum_a


def greeter(func):
    @wraps(func)
    def say_aloha(*args):
        
        result = "Aloha " + func(*args).title()
        return result
    
    return say_aloha


def sums_of_str_elements_are_equal(func):
    @wraps(func)
    def check_numbers(*args):
        elements = func(*args).split(" ")
        num1 = num_converter(elements[0])
        num2 = num_converter(elements[1])
        if num1 == num2:
            return f"{str(num1)} == {str(num2)}"
        else:
            return f"{str(num1)} != {str(num2)}"
    return check_numbers
    


def format_output(*required_keys):
    def decorator_func(to_be_decorated):
        def decoration(*args, **kwargs):
            category_dict = to_be_decorated(*args, **kwargs)

            final_dict = {}

            for category in required_keys:
                temp = []
                temp_len = 0
                for sub_category in category.split("__"):
                    print(sub_category)
                    if sub_category in category_dict.keys():
                        temp.append(category_dict[sub_category])
                        temp_len += len(category_dict[sub_category])
                    else:
                        raise ValueError("Wrong categories")
                    
                if temp_len == 0:
                    final_dict[category] = "Empty value"
                else:
                    final_dict[category] = " ".join(temp)

            return final_dict
        return decoration
    return decorator_func
            


def add_method_to_instance(klass):
    def wrapper(to_be_decorated):
        #print(to_be_decorated.__name__)
        def inner(*args, **kwargs):
            return to_be_decorated()
        setattr(klass, to_be_decorated.__name__, inner)

        return inner
    return wrapper
