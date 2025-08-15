class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        if "method" in request and request["method"] != "GET":
            return None
        else:
            request["method"] = "GET"

        return self.get(self.func, request)

    @staticmethod
    def get(func, request):
        return f"GET: {func(request)}"
