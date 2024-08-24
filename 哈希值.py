import hashlib
def get_file_hash(file_path, hash_algorithm='md5'):
    # 打开文件
    with open(file_path, 'rb') as f:
        # 读取文件内容
        data = f.read()
        # 计算哈希值
        if hash_algorithm == "1":
            hash_obj = hashlib.md5()
        elif hash_algorithm== "2":
            hash_obj = hashlib.sha1()
        elif hash_algorithm == "3":
            hash_obj = hashlib.sha256()
        else:
            raise ValueError('Unsupported hash algorithm: {}'.format(hash_algorithm))
        hash_obj.update(data)
        file_hash = hash_obj.hexdigest()
    # 返回哈希值
    return file_hash
file_path = input("文件路径 ")

print("哈希函数类型:\n（1)=>MD5\n (2)=>SHA1\n (3)=>SHA256")
hash_algorithm = input()
file_hash = get_file_hash(file_path, hash_algorithm)
print('File hash ({}): {}'.format(hash_algorithm.upper(), file_hash))
input("按回车键继续...\n")