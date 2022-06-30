import math
import random
from datetime import datetime
import os
import argparse

def gen_token_data(project_num, mint_num):
  hashv = "0x"
  for i in range(64):
    arg = random.randint(0,15);
    hashv += hex(arg)[2:]
  tokenid = str(project_num * 1000000 + mint_num)
  return (tokenid, hashv)


parser = argparse.ArgumentParser(description="ArtBlocks Drop Simulator", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", dest='num_mints', metavar='number_of_mints', type=int, default=500, help="number of mints in the drop")
parser.add_argument("-p", dest='project_num', metavar='project_number', type=int, default=452, help="project number")
parser.add_argument("script_path", help="path to project .js script")
parser.add_argument("features_path", help="path to features .js script")

args = parser.parse_args()

if args.num_mints < 1:
  print('number of mints ({}) must be a positive number'.format(args.num_mints))
  quit()

if args.project_num < 1:
  print('project number ({}) must be a positive number'.format(args.project_num))
  quit()

if not os.path.isfile(args.script_path):
  print('invalid script_path ({}); file not found'.format(args.script_path))
  quit()

if not os.path.isfile(args.features_path):
  print('invalid features_path ({}); file not found'.format(args.features_path))
  quit()

template = ""
with open("template_script.html", "r") as f:
  template = f.readlines()
template_features = ""
with open("template_features.html", "r") as f:
  template_features = f.readlines()

template = "".join(template)
template_features = "".join(template_features)
folder_name = datetime.now().strftime("SIM%Y%m%d%H%M%S")

print('Simulating AB drop with {} mints'.format(args.num_mints))
for i in range(args.num_mints):
  vals = gen_token_data(args.project_num, i);
  code = 'let tokenData = {{\"tokenId\":\"{}\",\"hash\":\"{}\"}}'.format(vals[0], vals[1]);
  content = template.replace('TOKENINFO', code).replace('SCRIPTINFO', args.script_path);
  content2 = template_features.replace('TOKENINFO', code).replace('SCRIPTINFO', args.features_path);
  filename = "{}/mint_{}.html".format(folder_name, i)
  filename2 = "{}/mint_{}_features.html".format(folder_name, i)
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  os.makedirs(os.path.dirname(filename2), exist_ok=True)
  with open(filename, "w") as f:
      f.write(content)
      print('Created: {}'.format(filename))
  with open(filename2, "w") as f:
      f.write(content2)
      print('Created: {}'.format(filename2))

print('Done. Congrats on your release!')