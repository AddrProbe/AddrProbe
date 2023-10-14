import os
import re
import subprocess
import pandas as pd
import torch
from config import DefaultConfig
from cvae import CVAE
from utils import *

config = DefaultConfig()
device = config.device


def probe(model, test_loader, model_id):
    # return new address with cluster label together
    generated_address_with_label = dict()
    model.eval()
    with torch.no_grad():
        for batch, c in enumerate(test_loader):
            c = c.float().to(device)
            # generate
            pred_x = model.generate(c).squeeze(1)
            # round pred_x to int and limit to [0, 15]
            pred_x[pred_x > 15] = 15
            pred_x[pred_x < 0] = 0
            # pred_x = pred_x.round().int()
            pred_x = pred_x.round().int()
            pred_x = pred_x.cpu().numpy()
            # save to new_address
            for i in range(pred_x.shape[0]):
                temp_address = format_vector_to_standard(pred_x[i].tolist())
                # turn one-hot to label
                temp_label = c[i].argmax().item()
                if temp_address not in generated_address_with_label:
                    generated_address_with_label[temp_address] = [model_id, temp_label]
                elif generated_address_with_label[temp_address] != [model_id, temp_label]:
                    print(f"Error: {temp_address} has different cluster label.")
                    print(f"Old label: {generated_address_with_label[temp_address]}, new label: {[model_id, temp_label]}")
                    generated_address_with_label[temp_address] = [model_id, temp_label]
    return generated_address_with_label