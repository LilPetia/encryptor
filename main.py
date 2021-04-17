import argparse
import json
import sys
from encode import encode, decode, train, hack


def parse_args():
    
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    # Encoding
    encode_parser = subparsers.add_parser('encode')
    encode_parser.set_defaults(mode='encode')
    encode_parser.add_argument('--cipher',
                               choices=['caesar', 'vigenere', 'vernam'],
                               help='Type of cipher', required=True)
    encode_parser.add_argument('--key', help='Key to encode',
                               required=True)
    encode_parser.add_argument('--input', type=argparse.FileType('r'),
                               help='Input file', required=True)
    encode_parser.add_argument('--output', type=argparse.FileType('w'),
                               help='Output file', required=True)
    
    # Decoding
    decode_parser = subparsers.add_parser('decode')
    decode_parser.set_defaults(mode='decode')
    decode_parser.add_argument('--cipher',
                               choices=['caesar', 'vigenere', 'vernam'],
                               help='Type of cipher', required=True)
    decode_parser.add_argument('--key', help='Key to decode',
                               required=True)
    decode_parser.add_argument('--input', type=argparse.FileType('r'),
                               help='Input file', required=True)
    decode_parser.add_argument('--output', type=argparse.FileType('w'),
                               help='Output file', required=True)

    # Train
    train_parser = subparsers.add_parser('train')
    train_parser.set_defaults(mode='train')
    train_parser.add_argument('--input', type=argparse.FileType('r'),
                              help='File with text')
    train_parser.add_argument('--output', type=argparse.FileType('w'),
                              help='File for model', required=True)

    # Hack
    hack_parser = subparsers.add_parser('hack')
    hack_parser.set_defaults(mode='hack')
    hack_parser.add_argument('--input', type=argparse.FileType('r'),
                             help='Input file')
    hack_parser.add_argument('--output', type=argparse.FileType('w'),
                             help='Output file')
    hack_parser.add_argument('--model', type=argparse.FileType('r'),
                             help='File with model', required=True)

    return parser.parse_args()
    


def input(args) -> dict:
   
    args = parse_args()

    if args.input:
        args.text = args.input.read()
    else:
        args.text = sys.stdin.read()

    if args.mode == 'encode':
        return {
            "mode": args.mode,
            "cipher": args.cipher,
            "key": args.key,
            "text": args.text
        }
    elif args.mode == 'decode':
        return {
            "mode": args.mode,
            "cipher": args.cipher,
            "key": args.key,
            "text": args.text
        }
    elif args.mode == 'train':
        return {
            "mode": args.mode,
            "text": args.text
        }
    elif args.mode == 'hack':
        try:
            args.model = json.load(args.model)
        except json.JSONDecodeError:
            raise Exception('Model file is not in json format')

        return {
            "mode": args.mode,
            "text": args.text,
            "model": args.model
        }

        


def output(args, result: str):
  

    if args.output:
        args.output.write(result)
    else:
        sys.stdout.write(result)
    



shell_args = parse_args()
args = input(shell_args)

if args['mode'] == 'encode':
    result = encode(cipher=args['cipher'],
                    key=args['key'], text=args['text'])
elif args['mode'] == 'decode':
        result = decode(cipher=args['cipher'],
                        key=args['key'], text=args['text'])
elif args['mode'] == 'train':
        result = train(text=args['text'])
elif args['mode'] == 'hack':
        result = hack(model=args['model'], text=args['text'])

output(shell_args, result)

