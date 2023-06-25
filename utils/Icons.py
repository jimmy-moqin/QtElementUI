from io import BytesIO

from PyQt5.QtCore import QBuffer, QIODevice, QResource
from PyQt5.QtGui import QImage, QPixmap

# 获取资源文件中的根目录
root = QResource("Icons\Icons.qrc")

# 递归遍历资源文件树
def traverse_resources(directory):
    # 检查目录是否存在
    if not QResource.isDir(directory):
        print("目录不存在")
        return

    # 获取目录下的子项列表
    children = QResource.children(directory)

    # 遍历子项
    for child in children:
        child_path = directory + child

        # 检查子项是否为目录
        if QResource.isDir(child_path):
            traverse_resources(child_path)
        else:
            # 检查子项是否为图片资源
            if child_path.endswith(".png") or child_path.endswith(".jpg") or child_path.endswith(".jpeg"):
                # 读取图片数据
                resource_data = QResource(child_path).data()
                image_buffer = BytesIO(resource_data)

                # 创建QPixmap对象
                pixmap = QPixmap()
                pixmap.loadFromData(image_buffer.getvalue())

                # 在此处执行您希望进行的操作，例如保存图片或显示图片等
                # ...

# 遍历资源文件
traverse_resources(root)
