import os
import subprocess


def train_fconv(dropout,
                share_input_output_embed,
                encoder_embed_dim,
                decoder_embed_dim,
                decoder_out_embed_dim,
                encoder_layers,
                decoder_layers,
                lr,
                momentum, clip_norm, optimizer, criterion, savedir, trainbin):
    fairseqdir = os.environ['FAIRSEQPY']
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    if share_input_output_embed:
        share = ' --share-input-output-embed '
    else:
        share = ''
    # ' --no-epoch-checkpoints ' + \
    cmd = 'python ' + fairseqdir + 'train.py --save-dir ' + savedir + \
          ' --arch fconv  --max-tokens 1000 --distributed-world-size 1  --log-format json ' + \
          '--encoder-embed-dim ' + str(encoder_embed_dim) + \
          ' --decoder-embed-dim ' + str(decoder_embed_dim) + \
          ' --decoder-out-embed-dim ' + str(decoder_out_embed_dim) + \
          ' --encoder-layers "' + encoder_layers + \
          '" --decoder-layers "' + decoder_layers + \
          '" --dropout ' + str(dropout) + \
          share + \
          ' --clip-norm ' + str(clip_norm) + \
          ' --lr ' + str(lr) + \
          ' --skip-invalid-size-inputs-valid-test ' + \
          ' --optimizer ' + optimizer + \
          ' --criterion ' + criterion + \
          ' --momentum ' + str(momentum) + \
          ' --max-epoch ' + str(20) + \
          ' --no-epoch-checkpoints ' + \
          ' --min-lr 1e-4   --batch-size 128 ' + trainbin

    cmd = cmd + " | tee " + savedir + "/log.txt"
    print(cmd)
    subprocess.call(cmd, shell=True)


def train_context(dropout,
                  share_input_output_embed,
                  encoder_embed_dim,
                  decoder_embed_dim,
                  decoder_out_embed_dim,
                  encoder_layers,
                  decoder_layers,
                  lr,
                  momentum, clip_norm, optimizer, criterion, savedir, trainbin):
    fairseqdir = os.environ['FAIRSEQPY']
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    if share_input_output_embed:
        share = ' --share-input-output-embed '
    else:
        share = ''

    cmd = 'python ' + fairseqdir + 'train.py --use-context --skip-invalid-size-inputs-valid-test --save-dir ' + savedir + \
          ' --arch fconv_context  --max-tokens 2000 --distributed-world-size 1  --log-format json ' + \
          '--encoder-embed-dim ' + str(encoder_embed_dim) + \
          ' --decoder-embed-dim ' + str(decoder_embed_dim) + \
          ' --decoder-out-embed-dim ' + str(decoder_out_embed_dim) + \
          ' --encoder-layers "' + encoder_layers + \
          '" --decoder-layers "' + decoder_layers + \
          '" --dropout ' + str(dropout) + \
          share + \
          ' --clip-norm ' + str(clip_norm) + \
          ' --lr ' + str(lr) + \
          ' --optimizer ' + optimizer + \
          ' --criterion ' + criterion + \
          ' --momentum ' + str(momentum) + \
          ' --max-epoch ' + str(20) + \
          ' --no-epoch-checkpoints  --min-lr 1e-4   --batch-size 48 ' + trainbin

    cmd = cmd + " | tee " + savedir + "/log.txt"
    print(cmd)
    subprocess.call(cmd, shell=True)


def train_trans(dropout,
                att_dropout,
                relu_dropout,
                encoder_embed_dim,
                decoder_embed_dim,
                encoder_attention_head,
                decoder_attention_head,
                encoder_layers,
                decoder_layers,
                lr,
                momentum,
                clip_norm,
                optimizer,
                criterion,
                savedir,
                trainbin):
    fairseqdir = os.environ['FAIRSEQPY']

    if not os.path.exists(savedir):
        os.makedirs(savedir)

    cmd = 'python ' + fairseqdir + 'train.py --skip-invalid-size-inputs-valid-test --save-dir ' + savedir + \
          ' --arch transformer --max-tokens 2000 --distributed-world-size 1 --log-format json ' + \
          '--encoder-embed-dim ' + str(encoder_embed_dim) + \
          ' --decoder-embed-dim ' + str(decoder_embed_dim) + \
          ' --encoder-attention-heads ' + str(encoder_attention_head) + \
          ' --decoder-attention-heads ' + str(decoder_attention_head) + \
          ' --encoder-layers ' + str(encoder_layers) + \
          ' --decoder-layers ' + str(decoder_layers) + \
          ' --dropout ' + str(dropout) + \
          ' --clip-norm ' + str(clip_norm) + \
          ' --attention-dropout ' + str(att_dropout) + \
          ' --relu-dropout ' + str(relu_dropout) + \
          ' --lr ' + str(lr) + \
          ' --optimizer ' + str(optimizer) + \
          ' --criterion ' + str(criterion) + \
          ' --momentum ' + str(momentum) + \
          ' --no-epoch-checkpoints ' + \
          ' --max-epoch 20  --batch-size 32 ' + str(trainbin)

    cmd = cmd + " | tee " + savedir + "/log.txt"
    print(cmd)
    subprocess.call(cmd, shell=True)


def train_lstm(dropout,
               encoder_embed_dim,
               decoder_embed_dim,
               decoder_out_embed_dim,
               decoder_attention,
               encoder_layers,
               decoder_layers,
               lr,
               momentum,
               clip_norm,
               optimizer,
               criterion,
               savedir,
               trainbin):
    fairseqdir = os.environ['FAIRSEQPY']

    if not os.path.exists(savedir):
        os.makedirs(savedir)

    cmd = 'python ' + fairseqdir + 'train.py --skip-invalid-size-inputs-valid-test --save-dir ' + savedir + \
          ' --arch lstm --max-tokens 2000 --distributed-world-size 1  --no-epoch-checkpoints --log-format json ' + \
          '--encoder-embed-dim ' + str(encoder_embed_dim) + \
          ' --decoder-embed-dim ' + str(decoder_embed_dim) + \
          ' --decoder-out-embed-dim ' + str(decoder_out_embed_dim) + \
          ' --encoder-layers ' + str(encoder_layers) + \
          ' --decoder-layers ' + str(decoder_layers) + \
          ' --dropout ' + str(dropout) + \
          ' --clip-norm ' + str(clip_norm) + \
          ' --lr ' + str(lr) + \
          ' --optimizer ' + optimizer + \
          ' --criterion ' + criterion + \
          ' --momentum ' + str(momentum) + \
          ' --decoder-attention ' + str(decoder_attention) + \
          ' --no-epoch-checkpoints ' + \
          ' --max-epoch 20  --batch-size 32 ' + trainbin

    cmd = cmd + " | tee " + savedir + "/log.txt"
    print(cmd)
    subprocess.call(cmd, shell=True)
