#!/usr/bin/env python3.6

# Convert videos into images
# You can run it like this: videos.py /videos /images

import argparse

#Create the parser:
my_parser = argparse.ArgumentParser(description='Videos converted to images')

# We create the variable indir with str as type and a help message is provided.
my_parser.add_argument('indir', type=str, help='Type the input directory for videos')

# We create the variable outdir in this case
my_parser.add_argument('outdir', type=str, help='Type the output directory for images')

#Next the args variable is set to the values of the parsed arguments.
args = my_parser.parse_args()

print(args.indir)


