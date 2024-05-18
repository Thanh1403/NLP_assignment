import nltk 
from nltk import Tree
nltk.download('punkt')

# Đọc cấu trúc ngữ pháp từ tệp grammar.txt
with open(r'data/structure.txt') as f:
    structure_input = f.read()

# Tạo cấu trúc ngữ pháp từ chuỗi đọc được
structure = nltk.CFG.fromstring(structure_input)

# Khởi tạo trình phân tích câu với cấu trúc ngữ pháp đã tạo
analyzer = nltk.ChartParser(structure)

def main():
    # Đọc các câu từ tệp sentences.txt
    f = open(r'data/sentences.txt', 'r')
    sentences = f.readlines()
    f.close()

    # Mở tệp parse-results.txt để ghi kết quả phân tích
    result = open(r'data/parse-results.txt', 'w')
    
    # Phân tích từng câu trong danh sách câu
    for sentence in sentences:
        # Tiền xử lý câu trước khi phân tích
        sentence = preprocessing(sentence)

        try: 
            # Thực hiện phân tích câu và lưu các cây cú pháp tìm được
            trees = list(analyzer.parse(sentence))
        except:
            # Nếu không tìm thấy cây cú pháp, gán một cây trống
            trees = tree = Tree("", [])

        # Ghi kết quả phân tích vào tệp parse-results.txt
        result.write(str(trees))
        result.write('\n')

        # In ra màn hình cây cú pháp của từng câu
        for tree in trees:
            tree.pretty_print()

    # Đóng tệp parse-results.txt
    result.close()

def preprocessing(sentence):
    # Tiền xử lý câu bằng cách chuyển đổi sang chữ thường và tách từ
    return sentence.lower().split()

main()