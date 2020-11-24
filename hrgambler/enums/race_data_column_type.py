from enum import Enum


class RaceDataColumnType(Enum):
    ORDER = {'id': 1, 'column_order': 0, 'en': 'order', 'ja': '着順'}
    POSITION = {'id': 2, 'column_order': 1, 'en': 'position', 'ja': '枠'}
    NUMBER = {'id': 3, 'column_order': 2, 'en': 'number', 'ja': '馬番'}
    NAME = {'id': 4, 'column_order': 3, 'en': 'name', 'ja': '馬名'}
    Profile = {'id': 5, 'column_order': 4, 'en': 'Profile', 'ja': '性齢'}
    IMPOST = {'id': 6, 'column_order': 5, 'en': 'impost', 'ja': '斤量'}
    JOCKEY = {'id': 7, 'column_order': 6, 'en': 'jockey', 'ja': '騎手'}
    TIME = {'id': 8, 'column_order': 7, 'en': 'time', 'ja': 'タイム'}
    MARGIN = {'id': 9, 'column_order': 8, 'en': 'margin', 'ja': '着差'}
    FAVORITE = {'id': 10, 'column_order': 9, 'en': 'favorite', 'ja': '人気'}
    ODDS = {'id': 11, 'column_order': 10, 'en': 'odds', 'ja': '単勝オッズ'}
    WORKOUT = {'id': 12, 'column_order': 11, 'en': 'workout', 'ja': '後3F'}
    PASSING_ODER = {'id': 13, 'column_order': 12, 'en': 'passing_oder', 'ja': 'コーナー通過順'}
    STABLE = {'id': 14, 'column_order': 13, 'en': 'stable', 'ja': '厩舎'}
    HORSE_WEIGHT = {'id': 16, 'column_order': 14, 'en': 'horse_weight', 'ja': '馬体重'}
    HORSE_ID = {'id': 17, 'column_order': 15, 'en': 'horse_id', 'ja': 'id'}

    def __new__(cls, value, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.column_order = value['column_order']
        obj.en = value['en']
        obj.ja = value['ja']
        return obj
