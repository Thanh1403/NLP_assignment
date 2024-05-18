from nltk.parse.generate import generate
from nltk import CFG
import nltk
nltk.download('punkt')

# Đọc cấu trúc ngữ pháp từ tệp grammar.txt
with open(r'data/structure.txt') as f:
    structure_input = f.read()

# Mở tệp samples.txt để ghi các câu mẫu được tạo ra
f = open(r'data/samples.txt', 'w')

# Tạo cấu trúc ngữ pháp từ chuỗi đọc được
structure = CFG.fromstring(structure_input)

# Tạo ra 10 câu mẫu từ cấu trúc ngữ pháp với độ sâu là 5
for sentence in generate(structure, depth=5 , n=10):
    # Ghi câu mẫu vào tệp samples.txt
    f.write(' '.join(sentence)+'\n')

# Đóng tệp samples.txt
f.close()