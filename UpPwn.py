from lib.opts import Opts
from lib.core import Core
import sys
#opts is a simple python library which allows you to easiely parse command line arguments
def UpPwn(argv):
    opts = Opts(argv)
    opts.initialize_options()
    parsed_opts = opts.parse()

    core = Core(parsed_opts)
    core.run()
    core.stop()

if __name__ == '__main__':
    UpPwn(sys.argv[1:])
