## 授業前課題_Python 演習_3

WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']

def output_schedule(study_time_list, holiday):
    '''今週の勉強予定を出力します'''

#’月’ = “月曜日は、”
 ‘火’ = “火曜日は、”
 ‘水’ = “水曜日は、”
 ‘木’ = “木曜日は、”
 ‘金’ = “金曜日は、”
 ‘土’ = “土曜日は、”
 ‘日’ = “日曜日は、”

#0 = “お休みです。”
 1 = “1時間勉強する予定です。”
 2 = “2時間勉強する予定です。”
 3 = “3時間勉強する予定です。”
 4 = “4時間勉強する予定です。”

＃line1 = “1限目”
　line2 = “2限目”
　line3 = “3限目”
　line4 = “4限目”

def main():
    '''勉強情報をoutput_scheduleに渡します'''
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list)


if __name__ == '__main__':
    main()
