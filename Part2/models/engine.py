from models.procedure import Procedure
from models.grammar import construct_semantic
from models.dependency import malt_parse
from models.settings import execute 
from models.settings import DATA  


def get_questions():
    """
    Trả về danh sách các câu hỏi mới.
    """
    return [
        "em có thể nhắc lại tất cả các tour được không?",
        "đi từ Hồ Chí Minh tới Nha Trang hết bao lâu?",
        "đi từ Hồ Chí Minh tới Đà Nẵng hết bao lâu?",
        "có bao nhiêu tour đi Phú Quốc vậy bạn?",
        "tour Nha Trang đi bằng phương tiện gì vậy?",
        "đi Nha Trang có những ngày nào nhỉ?"
        # Thêm các câu hỏi mới ở đây...
    ]

def write_to_file(filename: str, data: str):
    """
    Ghi dữ liệu vào file với tên filename.
    """
    with open(filename, "w") as file:
        file.write(data)

def main():
    # Lấy danh sách câu hỏi mới
    questions = get_questions()

    # Thực thi các câu hỏi và ghi kết quả vào các tệp tin
    for i, question in enumerate(questions, start=1):
        # Ghi kết quả vào tệp tin với định dạng "output{i}.txt"
        output_filename = f"output{i}.txt"
        # Gọi hàm write_to_file để ghi kết quả vào tệp tin
        # write_to_file(output_filename, result)
if __name__ == "__main__":
    main()