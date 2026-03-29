# -*- coding: utf-8 -*-
import yaml
import os


class YamlUtil:
    """YAML 数据读取工具类"""

    @staticmethod
    def read_yaml(file_path):
        """
        读取指定的 yaml 文件并返回内容
        :param file_path: 相对于项目根目录的路径，例如 'data/baidu_data.yaml'
        """
        # 1. 获取当前文件的绝对路径
        current_path = os.path.abspath(__file__)
        # 2. 获取项目的根目录 (utils 的上一层)
        root_path = os.path.dirname(os.path.dirname(current_path))
        # 3. 拼接出 yaml 文件的完整路径
        full_path = os.path.join(root_path, file_path)

        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                # 使用 safe_load 将 YAML 转为 Python 的字典/列表
                data = yaml.safe_load(f)
                return data
        except FileNotFoundError:
            print(f"错误：找不到文件 {full_path}")
            return None