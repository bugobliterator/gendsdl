import sys
import os
from glob import glob

parser_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parser_dir + "/src")

import genmsg.template_tools

msg_template_map = { 'msg.h.template':'@NAME@.h' }
srv_template_map = { 'srv.h.template':'@NAME@.h' }

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser("[options] <root_directory>")
    parser.add_option("-o", dest='outdir',
                      help="directory in which to place output files")
    parser.add_option("-e", dest='emdir',
                      help="directory containing template files",
                      default=sys.path[0])

    (options, argv) = parser.parse_args(sys.argv)

    if( not options.outdir or not options.emdir):
        parser.print_help()
        exit(-1)
    file_list = [y.replace(argv[1]+'/','') for x in os.walk(argv[1]) for y in glob(os.path.join(x[0], '*.uavcan'))]
    includepath = [':'.join([x[0].replace(argv[1]+'/',''), x[0]]) for x in os.walk(argv[1])]
    for file_name in file_list:
        print('')
        if len(file_name) > 1:
            genmsg.template_tools.generate_from_file(argv[1], file_name, os.path.dirname(file_name), options.outdir, options.emdir, includepath, msg_template_map, srv_template_map)

