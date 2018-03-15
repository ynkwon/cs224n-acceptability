from __future__ import print_function
from datetime import datetime
import argparse
import torch

def get_parser():
    parser = argparse.ArgumentParser(description="Acceptability Judgments")
    parser.add_argument("-d", "--data_dir", type=str, default="./data",
                        help="Directory containing train.txt, test.txt" +
                        "and valid.txt")
    parser.add_argument("-e", "--embedding", type=str, default="glove.6B.300d",
                        help="Embedding type to be used, select from" +
                        "http://torchtext.readthedocs.io/en/latest/vocab.html#pretrained-aliases")

    # Preprocess arguments
    parser.add_argument("--preprocess_data", action="store_true", default=True,
                        help="Whether to preprocess data?")
    parser.add_argument("--should_not_lowercase", action="store_false", default=False,
                        help="Should lowercase data? Default: true")
    parser.add_argument("--preprocess_tokenizer", default='space', type=str,
                        help="Type of tokenizer to use (space|nltk)")

    parser.add_argument("-l", "--logs_dir", type=str, default="./logs",
                        help="Log directory")
    parser.add_argument("--should_not_log", action='store_true',
                        help="Specify when trainer should not log to file")

    parser.add_argument("-dt", "--data_type", type=str,
                        default="discriminator",
                        help="Data type")
    # TODO: Take a look on how to make this enum later
    parser.add_argument("-m", "--model", type=str,
                        default="lstm_pooling_classifier",
                        help="Type of the model you want to use")
    parser.add_argument("-s", "--save_loc", type=str, default="./save",
                        help="Save point for models")
    parser.add_argument("-g", "--gpu", type=bool, default=False,
                        help="Whether use GPU or not")
    parser.add_argument("-p", "--crop_pad_length", type=int, default=30,
                        help="Padding Crop length")

    # Chunk parameters
    parser.add_argument("--stages_per_epoch", type=int, default=2,
                        help="Eval/Stats steps per epoch")
    parser.add_argument("--prints_per_stage", type=int, default=1,
                        help="How many times print stats per epoch")
    parser.add_argument("--patience", type=int, default=20,
                        help="Early stopping patience")
    parser.add_argument("-n", "--epochs", type=int, default=10,
                        help="Number of epochs")
    parser.add_argument("-b", "--batch_size", type=int, default=32,
                        help="Batch size")
    parser.add_argument("--by_source", type=bool, default=False,
                        help="Break output stats by source")
    parser.add_argument("--max_pool", type=bool, default=False,
                        help="Use max pooling for CBOW")

    # Tuneable parameters
    parser.add_argument("--hidden_size", type=int, default=300,
                        help="Hidden dimension for LSTM")
    parser.add_argument("--num_layers", type=int, default=1,
                        help="Number of layers for LSTM")
    parser.add_argument("-lr", "--learning_rate", type=float, default=.0005,
                        help="Learning rate")

    # Encoder parameter
    parser.add_argument("--encoding_size", type=int, default=100,
                        help="Output size of encoder, input size of aj")
    parser.add_argument("--encoder_num_layers", type=int, default=1,
                        help="Number of layers in encoder network")

    ## Take care to pass this argument for loading a pretrained encoder
    parser.add_argument("--encoder_path", type=str, default=None,
                        help="Location of encoder checkpoint")
    parser.add_argument("--encoding_type", type=str,
                        default="lstm_pooling_classifier",
                        help="Class of encoder")

    # Train dataset evaluate parameters
    # Can be useful when train dataset is small (like directly evaluating acceptability dataset)
    parser.add_argument("--evaluate_train", action="store_true", default=False,
                        help="Whether to evaluate training set after some interval (default: False)")
    parser.add_argument("--train_evaluate_interval", type=int, default=10,
                        help="Interval after which train dataset needs to be evaluated.")

    parser.add_argument("--experiment_name", type=str,
                        default=None,
                        help="Name of the current experiment")
    parser.add_argument("-r", "--resume", type=str, default=None,
                        help="Checkpoint path for resuming")
    return parser


def get_lm_parser():
    parser = argparse.ArgumentParser("Acceptability Judgments Generator")
    parser.add_argument("-d", "--data", type=str,
                        help="Directory containing train.tsv and valid.tsv")
    parser.add_argument("-v", "--vocab_file", type=str,
                        help="Vocabulary file")

    parser.add_argument("-m", "--model", type=str, default="lstm",
                        help="Model to be used for LM")
    parser.add_argument("-l", "--logs_dir", type=str, default="./logs",
                        help="Folder for storing logs")
    parser.add_argument("--should_not_log", action='store_true',
                        help="Specify when trainer should not log to file")
    parser.add_argument("-se", "--stages_per_epoch", type=int, default=2,
                        help="Eval/Stats steps per epoch")

    parser.add_argument("-p", "--patience", type=int, default=20,
                        help="Early stopping patience")

    parser.add_argument("-en", "--experiment_name", type=str, default=None,
                        help="Name of the experiment")
    parser.add_argument("-es", "--embedding_size", type=int, default=300,
                        help="Size of the embedding dimension")
    parser.add_argument("-sl", "--seq_length", type=int, default=25,
                        help="Sequence length")
    parser.add_argument("-hs", "--hidden_size", type=int, default=600,
                        help="Size of the hidden dimension")
    parser.add_argument("-nl", "--num_layers", type=int, default=1,
                        help="Size of the hidden dimension")
    parser.add_argument("-b", "--batch_size", type=int, default=32,
                        help="Batch size")
    parser.add_argument("-e", "--epochs", type=int, default=10,
                        help="Number of epochs")
    parser.add_argument("-do", "--dropout", type=float, default=0.5,
                        help="Dropout")
    parser.add_argument("-g", "--gpu", action="store_true", default=torch.cuda.is_available(),
                        help="GPU")
    parser.add_argument("-lr", "--learning_rate", type=float, default=0.001,
                        help="Learning rate")
    parser.add_argument("-s", "--save_loc", type=str, default='./save',
                        help="Save folder")
    parser.add_argument("-r", "--resume", type=str, default=None,
                        help="Checkpoint for resuming")
    parser.add_argument('--clip', type=float, default=0.5,
                        help='gradient clipping')
    return parser
