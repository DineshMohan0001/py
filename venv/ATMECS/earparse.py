import argparse
import math

parser =  argparse.ArgumentParser(description="AIRTHMETIC OPERATION")



parser.add_argument("--num1",help="number1",type=int)
parser.add_argument("--num2",help="number2",type=int)
parser.add_argument("--operation",help="OPERATION",default='+')



args=parser.parse_args()
#print(args)

if args.operation == '+':
    print(args.num1 + args.num2)
if args.operation == '-':
    print(args.num1 - args.num2)
if args.operation == '*':
    print(args.num1 * args.num2)
if args.operation == 'pow':
    print(math.pow(args.num1,args.num2))