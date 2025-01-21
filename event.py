import os
import xml.etree.ElementTree as ET

# 設定資料夾路徑
event_folder = 'event'
output_file = 'output.txt'

# 開啟輸出檔案
with open(output_file, 'w', encoding='utf-8') as f:
    # 遍歷 event 資料夾中的所有子資料夾
    for subdir in os.listdir(event_folder):
        subdir_path = os.path.join(event_folder, subdir)
        if os.path.isdir(subdir_path):
            event_file = os.path.join(subdir_path, 'event.xml')
            if os.path.exists(event_file):
                # 解析 XML 檔案
                tree = ET.parse(event_file)
                root = tree.getroot()
                
                # 取得所需的資訊
                data_name = root.find('dataName').text
                event_id = root.find('name/id').text
                event_str = root.find('name/str').text
                
                # 檢查 event_id 是否以 'event25' 開頭
                if data_name.startswith('event25') and len(event_id) >= 9: 
                    # 解析 event_id 來取得日期、類型和索引 
                    # # 250108011 -> 2025-01-08, 1(樂曲/區域/活動介紹), 1(索引) 
                    date = f'20{event_id[0:2]}-{event_id[3:5]}-{event_id[6:8]}' 
                    event_type_code = event_id[6:8] 
                    index = event_id[8]
                    
                    # 設定類型描述
                    event_type_dict = {
                        "01": "01(樂曲/區域/活動介紹)",
                        "02": "02(樂曲解禁)",
                        "03": "03(區域解禁)",
                        "04": "04(活動區域解禁)",
                        "05": "05(區域完美挑戰)",
                        "06": "06(倍卷解禁)",
                        "07": "07(新增印章卡獎勵)",
                        "09": "09(伝導楽曲条件緩和)"
                    }
                    event_type = event_type_dict.get(event_type_code, "未知類型")
                    
                    # 寫入輸出檔案
                    f.write('----------------------------------------\n')
                    f.write(f'ID: {event_id}\n')
                    f.write(f'Description: {event_str}\n')
                    f.write(f'Date: {date}\n')
                    f.write(f'Type: {event_type}\n')
                    f.write(f'Index: {index}\n')
    f.write('----------------------------------------\n')

print(f'輸出已寫入 {output_file}')