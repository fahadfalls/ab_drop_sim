# ArtBlocks Drop Simulator

Tool for locally testing your ArtBlocks project drop

# Sample Usage

python3 ab_drop_sim.py ../testproject1/testproject1.js ../testproject1/features.js -n 100 -p 345

# Args

positional arguments:
  script_path         path to project .js script
  features_path       path to features .js script

optional arguments:
  -h, --help          show this help message and exit
  -n number_of_mints  number of mints in the drop (default: 500)
  -p project_number   project number (default: 452)