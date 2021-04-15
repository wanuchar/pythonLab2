from base_serializer import BaseSerializer

import pickle


class PickleSerializer(BaseSerializer):
    def dump(self, obj, file_path, convert=False):
        try:
            with open(file_path, 'wb') as write_file:
                if not convert:
                    obj = super().serialize_object(obj)
                pickle.dump(obj, write_file)
        except Exception:
            return None

    def dumps(self, obj):
        return pickle.dumps(super().serialize_object(obj))

    def load(self, file_path, convert=False):
        try:
            with open(file_path, 'rb') as read_file:
                if convert:
                    return pickle.load(read_file)
                return super().deserialize_object(pickle.load(read_file))
        except Exception:
            return None

    def loads(self, str_obj):
        try:
            return super().deserialize_object(pickle.loads(str_obj))
        except Exception:
            return None
