python train.py -data data/kaggle_norm_competition/train_kaggle2transformer.atok.low.pt -save_model weights/trained_1decod_transf_100bdd -save_mode best -proj_share_weight

# Train parameters

# Namespace(batch_size=64, cuda=True, d_inner_hid=1024, d_k=64, d_model=512, d_v=64, d_word_vec=512, data='data/kaggle_norm_competition/train_kaggle2transformer.atok.low.pt', dropout=0.1, embs_share_weight=False, epoch=10, log=None, max_token_seq_len=52, n_head=8, n_layers=6, n_warmup_steps=4000, no_cuda=False, proj_share_weight=True, save_mode='best', save_model='weights/trained_1decod_transf_100bdd', src_vocab_size=35160, tgt_vocab_size=31179)
