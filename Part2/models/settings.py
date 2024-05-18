from .procedure import Procedure

N = "NOUN"
V = "VERB"
PP = "PREPOSITION" 
TIME = "TIME"  
Q = "QUERY"  
NAME = "NAME" 
PUNC = "PUNC"  
DURATION = "DURATION"  
YN = "YESNO"

DURATION_FROM_HCMC = {
    "NT_": "5 giờ",
    "DN_": "2 giờ"
}

TRANSPORTATION = {
    "PQ_": "airplane",
    "DN_": "airplane",
    "NT_": "train"
}

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
# Data
DATA = [
    {"TOUR PQ_": ["DTIME", "HCMC", "7:00HR"],
     "TOUR DN_": ["DTIME", "HCMC", "7:00HR"],
     "TOUR NT_": ["DTIME", "HCMC", "7:00HR"]},
    {"TOUR PQ_": ["ATIME", "PQ", "9:00HR"],
     "TOUR DN_": ["ATIME", "DN", "9:00HR"],
     "TOUR NT_": ["ATIME", "NT", "12:00HR"]},
    {"TOUR PQ_": ["RUN-TIME", "HCM", "NT", "2:00HR"],
     "TOUR DN_": ["RUN-TIME", "HCM", "PQ", "2:00HR"],
     "TOUR NT_": ["RUN-TIME", "HCM", "PQ", "5:00HR"]}
]

# Hàm xử lý các câu hỏi
def execute(procedure: Procedure, data):
    TOUR_DATA, ATIME_DATA, DTIME_DATA, RUNTIME_DATA = data
    
    q_type = None
    result = ""

    for pro in procedure.args:
        if isinstance(pro, Procedure) and pro.name == "PRINT-ALL":
            # Trường hợp in ra tất cả các tour
            result += ", ".join(TOUR_DATA.keys()) + "."
        
        elif isinstance(pro, Procedure) and pro.name == "DURATION-FROM-HCMC-TO":
            # Trường hợp tính toán thời gian từ Hồ Chí Minh tới các địa điểm khác
            destination = pro.args[0]
            if destination in DURATION_FROM_HCMC:
                duration = DURATION_FROM_HCMC[destination]
                result += f"Thời gian từ Hồ Chí Minh tới {destination} là {duration}."
            else:
                result += "Không tìm thấy thông tin về thời gian đi từ Hồ Chí Minh tới đích đến này."
        
        elif isinstance(pro, Procedure) and pro.name == "TOUR-COUNT-TO-PQ":
            # Trường hợp đếm số lượng tour đi Phú Quốc
            pq_tours = [tour for tour in TOUR_DATA.keys() if "PQ_" in tour]
            result += f"Số lượng tour đi Phú Quốc là {len(pq_tours)}."
        
        elif isinstance(pro, Procedure) and pro.name == "TRANSPORT-FROM-NT":
            # Trường hợp xác định phương tiện đi từ Nha Trang
            if "NT_" in ATIME_DATA:
                transport = ATIME_DATA["NT_"][0]  # Giả sử phương tiện được lưu ở vị trí đầu tiên
                result += f"Tour Nha Trang đi bằng phương tiện: {transport}."
            else:
                result += "Không tìm thấy thông tin về phương tiện đi từ Nha Trang."
        
        elif isinstance(pro, Procedure) and pro.name == "DAYS-TO-NT":
            # Trường hợp xác định ngày đi đến Nha Trang
            if "NT_" in DTIME_DATA:
                days = DTIME_DATA["NT_"][1:]  # Giả sử ngày đi được lưu từ vị trí thứ hai trở đi
                result += f"Tour đi Nha Trang có những ngày: {', '.join(days)}."
            else:
                result += "Không tìm thấy thông tin về ngày đi đến Nha Trang."
        
        # Thêm các trường hợp xử lý cho các câu hỏi mới ở đây...

    return result