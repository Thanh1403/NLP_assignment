from collections import OrderedDict

N = "NOUN"
V = "VERB"
PP = "PREPOSITION" 
TIME = "TIME"  
Q = "QUERY"  
NAME = "NAME" 
PUNC = "PUNC"  
DURATION = "DURATION"  
YN = "YESNO"

TOKENIZE_DICT = OrderedDict({
    "tàu hỏa": "tàu_hoả",
    "máy bay": "máy_bay",
    "tour": "tour",
    "thời gian": "thời_gian",
    "thành phố": "thành_phố",
    "đà nẵng": "đà_nẵng",
    "phú quốc": "phú_quốc",
    "nha trang": "nha_trang",
})

POS = {
    "tour": N,
    "thời_gian": DURATION,
    "đến": (V, PP),
    "từ": PP,
    "đi": V,
    "nào": Q,
    "mấy": Q,
    "giờ": N,
    "thành_phố": NAME,
    "đà_nẵng": NAME,
    "phú_quốc": NAME,
    "nha_trang": NAME,
    "lúc": PP,
    "?": PUNC,
    "không": YN,
    "PQ_": N,
    "DN_": N,
    "NT_": N
}