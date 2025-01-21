import re

input_file = 'events_1.45.txt'
output_file = 'extracted_types.txt'

# 使用正則表達式來匹配 Type 行
type_pattern = re.compile(r'Type: (\d{2}\(.*?\))')

types = set()

# 讀取輸入檔案並提取 Type 資訊
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = type_pattern.search(line)
        if match:
            types.add(match.group(1))

# 將提取的 Type 資訊寫入輸出檔案
with open(output_file, 'w', encoding='utf-8') as f:
    for type_info in sorted(types):
        f.write(f'{type_info}\n')

print(f'Types 已提取並寫入 {output_file}')