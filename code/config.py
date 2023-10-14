import os
import torch


class DefaultConfig(object):
    # general
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    device = torch.device("mps" if torch.backends.mps.is_available() else device)
    current_path = os.path.dirname(os.path.abspath(__file__))

    # data pre path
    knowledge_base_threshold = 1000
    ipasn_path = os.path.join(current_path, '../data/input/ipasn.dat')
    model_prefix_seed_number = os.path.join(current_path, '../data/result_info/prefix_seednum.txt')
    other_prefix_attr_path = os.path.join(current_path, '../data/result_info/unseeded_prefix_as_attr.txt')

    # data pre / train / test
    data_path = os.path.join(current_path, '../data/result_addrprobe_input_data/')

    # data pre / test
    model_prefix_attr_path = os.path.join(current_path, '../data/result_info/seeded_prefix_as_attr.txt')

    # train / test
    model_path = os.path.join(current_path, '../model/model/')
    init_cluster_info_path = os.path.join(current_path, '../model/init_cluster_info.txt')

    # test
    prefix_budget = 1000   # all prob budget
    init_prob_budget = prefix_budget * 0.05 # init prob budget
    growth_factor = 10
    fine_lower_limit = 128
    iter_model_path = os.path.join(current_path, '../model/iter_model/')
    is_model_prefix = True   # True (seeded prefix) or False (unseeded prefixs)
    # seeded prefix
    test_seeded_prefix_and_attr_path = os.path.join(current_path, '../data/result_info/seeded_prefix_as_attr.txt') 

    # unseeded prefixs
    test_unseeded_prefix_and_attr_path = os.path.join(current_path, '../data/result_info/unseeded_prefix_as_attr.txt') 

    # fre prefix 
    get_fre_pattern_path = os.path.join(current_path, '../result/result_seeded_prefix/zmap_result/')

    # seeded/unseeded prefix result path
    generated_address_path = os.path.join(current_path, '../result/result/generated_address/')
    new_address_path = os.path.join(current_path, '../result/result/new_address/')
    address_bank_path = os.path.join(current_path, '../result/result/address_bank/')
    active_address_bank_path = os.path.join(current_path, '../result/result/active_address_bank/')
    zmap_result_path = os.path.join(current_path, '../result/result/zmap_result/')


    # zmap
    local_ipv6 = "********"
    password = "*******"

    input_size = 32
    latent_size = 8     

    eps_threshold = 16
    eps_ratio = 0.01
    eps_min_sample = 100

    batch_size = 64
    test_batch_size = 100

    beta = 1
    block_num = 8
    feature_num = 128
    intermediate_size = 128

    epoch_num = 20
    lr = 1e-3

    warmup_epoch_num = 3
    warmup_lr = 1e-5