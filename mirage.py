import numpy as np
from PIL import Image
from argparse import ArgumentParser
import time

parser = ArgumentParser()
parser.add_argument("-t", "--top", required=True, help="顶层图片路径", metavar="\"./top.png\"")
parser.add_argument("-b", "--bottom", required=True, help="底层图片路径", metavar="\"./bottom.png\"")
parser.add_argument("-o", "--output", required=True, help="输出路径", metavar="\"./out.png\"")
parser.add_argument("-s", "--silent", help="取消控制台输出", action="store_true")


def hollow(image: np.ndarray, mode: int) -> np.ndarray:
    """
    镂空一张图片

    :param image: 原图
    :param mode: 0为底图，1为顶图
    :return: 处理后的图
    """
    image = image.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i, j, 1] = 255 - image[i, j, 0]
            if (i + j) % 2 == mode:
                image[i, j, 1] = 0
                image[i, j, 0] = 0
            else:
                image[i, j, 0] = mode * 255
    return image


def generate_mirage(top_hollowed: np.ndarray, bottom_hollowed: np.ndarray) -> np.ndarray:
    """
    生成最终图像

    :param top_hollowed: 镂空后顶图
    :param bottom_hollowed: 镂空后底图
    :return: 结果图
    """
    mirage_size = np.maximum(top_hollowed.shape, bottom_hollowed.shape)
    mirage_im = np.zeros(mirage_size)
    top_padding = mirage_size - top_hollowed.shape
    bottom_padding = mirage_size - bottom_hollowed.shape
    top_hollowed = np.pad(top_hollowed, ((0, top_padding[0]), (0, top_padding[1]), (0, 0)))
    bottom_hollowed = np.pad(bottom_hollowed, ((0, bottom_padding[0]), (0, bottom_padding[1]), (0, 0)))
    return (mirage_im + top_hollowed + bottom_hollowed).astype("uint8")


if __name__ == '__main__':
    args = vars(parser.parse_args())
    if args.get("silent", False):
        top = np.array(Image.open(args.get("top"), mode="r").convert("LA"))
        bottom = np.array(Image.open(args.get("bottom"), mode="r").convert("LA"))
        top = hollow(top, mode=1)
        bottom = hollow(bottom, mode=0)
        out = generate_mirage(top, bottom)
        Image.fromarray(out).save(args.get("output"))
    else:
        now = time.time()
        print("开始处理...")
        top = np.array(Image.open(args.get("top"), mode="r").convert("LA"))
        bottom = np.array(Image.open(args.get("bottom"), mode="r").convert("LA"))
        print("读取图片耗时: %.2fs" % (time.time() - now))
        now = time.time()
        top = hollow(top, mode=1)
        bottom = hollow(bottom, mode=0)
        print("处理图片耗时: %.2fs" % (time.time() - now))
        now = time.time()
        out = generate_mirage(top, bottom)
        print("合成图片耗时: %.2fs" % (time.time() - now))
        now = time.time()
        Image.fromarray(out).save(args.get("output"))
        print("保存图片耗时: %.2fs" % (time.time() - now))
        print("生成成功！")

