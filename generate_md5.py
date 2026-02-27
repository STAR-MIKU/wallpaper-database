import hashlib

# 生成从6到100的MD5哈希值
md5_list = []
for i in range(6, 101):
    # 将数字转换为字符串并计算MD5
    md5_hash = hashlib.md5(str(i).encode()).hexdigest()
    md5_id = f"wp-{md5_hash}"
    md5_list.append(f"{i}\t{md5_id}")

# 输出结果
for item in md5_list:
    print(item)