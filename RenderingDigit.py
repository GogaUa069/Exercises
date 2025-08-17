from string import digits


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(arguments):
            """
            Rendering all the arguments in list with RenderDigit
            :param arguments: string list
            :return: rendered list ex. [-1, -2, abc, --2, 5] >>> [-1, -2, None, None, 5]
            """
            rendered_list = [self.render(i) for i in arguments.split()]
            return rendered_list
        return wrapper


class RenderDigit:
    def __call__(self, value):
        """
        :param value: Some string
        :return: if string is integer - int(value), else None
        """
        if value[0] in digits + "-" and value[1:] in digits:
            return int(value)
        else:
            return None


render = RenderDigit()

@InputValues(render)
def input_dg(num_list):
    return num_list


res = input_dg(input())
print(res)
