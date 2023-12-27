# 7，大寫幾個，小寫幾個，數字幾個，空白建有幾個
with open("text.txt", 'r') as file:
    # 初始化計數器
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    space_count = 0

    # 讀取文件內容
    content = file.read()

    # 遍歷每個字符
    for char in content:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

# 輸出結果
print("大寫字母數量:", uppercase_count)
print("小寫字母數量:", lowercase_count)
print("數字數量:", digit_count)
print("空白字符數量:", space_count)



# 8 func，接受字串，回傳內容一樣，第一個字會大寫
def capitalize_first_letter(input_str):
    # 使用 split 將字串分割成單字的列表
    words = input_str.split()

    # 對每個單字處理，將第一個字母轉換為大寫
    capitalized_words = [word.capitalize() for word in words]

    # 使用 join 將處理後的單字組合成字串
    result_str = ' '.join(capitalized_words)

    return result_str

# 測試函數
input_string = input()
result = capitalize_first_letter(input_string)
print(result)

# 12 接收字串，把第一個字母移到後面

def move_first_letter_to_end(input_str):
    # 使用 split 將字串分割成單字的列表
    words = input_str.split()

    # 對每個單字處理，將第一個字母移到尾部，再加上 'AY'
    modified_words = [(word[1:] + word[0] + 'AY') for word in words]

    # 使用 join 將處理後的單字組合成字串
    result_str = ' '.join(modified_words)

    return result_str

# 測試函數
input_string = input()
result = move_first_letter_to_end(input_string)
print(result)