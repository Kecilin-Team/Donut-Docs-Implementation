"""
# Donut
# Copyright (c) 2022-present NAVER Corp.
# MIT License
# """


import torch
from PIL import Image
from donut import DonutModel


def inference():
    pretrained_model = DonutModel.from_pretrained("result/train/20241222_185915")
 
    if torch.cuda.is_available():
        pretrained_model.half()
        pretrained_model.to("cuda")

    pretrained_model.eval()

    image = Image.open("data/test/534030.5.6.jpg") #.convert("RGB") # Change here
    output = pretrained_model.inference(image=image, prompt="<s_data>")["predictions"][0]
    print(output)


if __name__ == "__main__":
    predictions = inference ()



