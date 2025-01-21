import os
import xml.etree.ElementTree as ET

# 輸入輸出類型（1: 簡要描述, 2: 完整信息）
output_type = input("請輸入輸出類型(1: 簡要描述, 2: 完整信息): ")
# 輸入事件資料夾的路徑
event_folder = input('請輸入事件資料夾的路徑: ')
# 輸入輸出文件的名稱
output_file = input('請輸入輸出文件的名稱(txt): ')

with open(output_file, 'w', encoding='utf-8') as f:
    if output_type == '1':
        # 簡要描述模式
        for subdir in os.listdir(event_folder):
            subdir_path = os.path.join(event_folder, subdir)
            if os.path.isdir(subdir_path):
                event_file = os.path.join(subdir_path, 'event.xml')
                if os.path.exists(event_file):
                    tree = ET.parse(event_file)
                    root = tree.getroot()
                    
                    # 提取事件名稱
                    event_str = root.find('name/str').text
                    
                    f.write(f'{event_str}\n')
    if output_type == '2':
        # 完整信息模式
        for subdir in os.listdir(event_folder):
            subdir_path = os.path.join(event_folder, subdir)
            if os.path.isdir(subdir_path):
                event_file = os.path.join(subdir_path, 'event.xml')
                if os.path.exists(event_file):
                    tree = ET.parse(event_file)
                    root = tree.getroot()
                    
                    # 提取數據名稱和事件ID
                    data_name = root.find('dataName').text
                    event_id = root.find('name/id').text
                    event_str = root.find('name/str').text
                    
                    if len(event_id) >= 9: 
                        # 解析日期和事件類型
                        date = f'20{event_id[0:2]}-{event_id[2:4]}-{event_id[4:6]}' 
                        event_type_code = event_id[6:8] 
                        index = event_id[8]
                        
                        event_type_dict = {
                            "01": "01(歌曲/區域/事件介紹)",
                            "02": "02(歌曲解鎖)",
                            "03": "03(區域解鎖)",
                            "04": "04(事件區域解鎖)",
                            "05": "05(區域完美挑戰)",
                            "06": "06(雙倍票解鎖)",
                            "07": "07(新印章卡獎勵)",
                            "09": "09(傳導歌曲條件放寬)"
                        }
                        event_type = event_type_dict.get(event_type_code, "未知類型")
                        
                        f.write('----------------------------------------\n')
                        f.write(f'ID: {event_id}\n')
                        f.write(f'描述: {event_str}\n')
                        f.write(f'日期: {date}\n')
                        f.write(f'類型: {event_type}\n')
                        f.write(f'索引: {index}\n')
        f.write('----------------------------------------\n')

print(f'輸出已寫入 {output_file}')