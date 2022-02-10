import base64


class Reply:

    def __init__(self, success=True, error=None, keys=[], content=None):
        self.success = success
        self.error = error
        self.keys = keys
        self.content = content

    def to_json(self):
        res = {}
        if self.success:
            res["success"] = "true"
        else:
            res["success"] = "false"
            res["error"] = self.error.to_json()
            return res

        if len(self.keys) > 0:
            res["keys"] = self.keys
            return res

        if self.content is not None:
            res["content"] = self.content
            return res

        return res