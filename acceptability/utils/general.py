import torch

from torch import nn
from datetime import datetime
from acceptability.models import LSTMPoolingClassifier
from acceptability.models import LinearClassifierWithEncoder
from acceptability.models import CBOWClassifier
from acceptability.models import LSTMLanguageModel


def get_model_instance(args):
    # Get embedding size from embedding parameter
    args.embedding_size = int(args.embedding.split('.')[-1][:-1])
    if args.model == "lstm_pooling_classifier":
        return LSTMPoolingClassifier(
            hidden_size=args.hidden_size,
            embedding_size=args.embedding_size,
            num_layers=args.num_layers
        )
    elif args.model == "linear_classifier":
        # TODO: Add support for encoder here later
        return LinearClassifierWithEncoder(
            hidden_size=args.hidden_size,
            embedding_size=args.embedding_size,
            encoding_size=args.encoding_size,
            num_layers=args.num_layers,
            encoder_type=args.encoding_type,
            encoder_num_layers=args.encoder_num_layers,
            encoder_path=args.encoder_path
        )
    elif args.model == "cbow_classifier":
        return CBOWClassifier(
            hidden_size=args.hidden_size,
            input_size=args.embedding_size,
            max_pool=args.max_pool
        )
    else:
        return None

def get_lm_model_instance(args):
    if args.model == "lstm":
        return LSTMLanguageModel(
            args.embedding_size,
            args.seq_length,
            args.hidden_size,
            args.batch_size,
            args.vocab_size,
            args.num_layers,
            args.dropout
        )

def get_lm_experiment_name(args):
    # mapping:
    # h -> hidden_size
    # l -> layers
    # lr -> learning rate
    # e -> encoding_size
    name = "experiment_%s_s_%d_h_%d_l_%d_lr_%.4f_d_%.2f" % (
        args.model,
        args.seq_length,
        args.hidden_size,
        args.num_layers,
        args.learning_rate,
        args.dropout
    )

    return name


def get_experiment_name(args):
    # mapping:
    # h -> hidden_size
    # l -> layers
    # lr -> learning rate
    # e -> encoding_size
    name = "experiment_%s_h_%d_l_%d_lr_%.4f_e_%d" % (
        args.model,
        args.hidden_size,
        args.num_layers,
        args.learning_rate,
        args.encoding_size
    )

    return name
