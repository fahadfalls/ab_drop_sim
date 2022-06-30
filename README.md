
# ArtBlocks Drop Simulator

Tool for locally testing your ArtBlocks project drop!

For each test mint, two HTML files will be produced: one that displays the generated artwork and another that writes feature info to the browser console.

# Sample Usage

    python3 ab_drop_sim.py ../testproject1/testproject1.js ../testproject1/features.js -n 100 -p 345

# Args

|arg|description  | arg type |
|--|--|--|
| script_path | path to project .js script | required, positional
| features_path | path to features .js script | required, positional
| -n | number of mints in the drop (default: 500) | optional
| -p | project number (default: 452) | optional