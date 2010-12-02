#! /usr/bin/env python
import yaml
import sys

##########
# README #
##########
#
# This script search for missing package names in rosdep.yaml files.
#
# It makes sure that all ROS required packages will be found by rosdep
# when compiling on a specific distribution.
#
# You can generate the concatenation of all rosdep.yaml files of your
# current ROS installation by typing in your shell:
#
#  (find $ROS_ROOT -name rosdep.yaml | xargs cat) > all_rosdep.yaml
#
# Then you can run this script:
# ./search_missing_rosdep_info.py fedora all_rosdep.yaml
#

if len(sys.argv) != 3:
    print "This script requires exactly two arguments:"
    print sys.argv[0] + " <distribution> <rosdep.yaml file>"
    sys.exit(1)

os = sys.argv[1]
filename = sys.argv[2]

stream = file(filename)
doc = yaml.load(stream)

print "Package names are missing for:"
for k,v in doc.iteritems():
    if not os in v.keys():
        print "\t * " + k
