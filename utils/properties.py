import math
import os

from src.code.abstract.code import Code


class Properties:
    verbose = False
    depth = 1
    module_depth = 1
    vanilla_name = "vanilla"
    angular_name = "angular"
    jquery_name = "jquery"
    node_name = "node"
    node_multifile_name = "node_multifile"
    objectivec_name = "objectivec"
    swift_name = "swift"
    all_name = "all"
    test_name = "test"
    type = None
    root_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "../.."))
    output_dir = os.path.join(root_dir, "output")
    test_dir = os.path.join(root_dir, "test")
    all_constructs = "src/constructs/languages"
    js_constructs = "src/constructs/languages/javascript"
    construct_dirs = {
        vanilla_name: os.path.join(js_constructs, vanilla_name),
        angular_name: os.path.join(js_constructs, angular_name),
        jquery_name: os.path.join(js_constructs, jquery_name),
        node_name: os.path.join(js_constructs, node_name),
        node_multifile_name: os.path.join(js_constructs, node_multifile_name),
        objectivec_name: os.path.join(all_constructs, objectivec_name),
        swift_name: os.path.join(all_constructs, swift_name)
    }

    dirs = {
        vanilla_name:os.path.join(output_dir, vanilla_name + "/"),
        angular_name:os.path.join(output_dir, angular_name + "/"),
        jquery_name:os.path.join(output_dir, jquery_name + "/"),
        node_name:os.path.join(output_dir, node_name + "/"),
        node_multifile_name:os.path.join(output_dir, node_multifile_name + "/"),
        objectivec_name:os.path.join(output_dir, objectivec_name + "/"),
        swift_name:os.path.join(output_dir, swift_name + "/"),
        test_name: os.path.join(output_dir, test_name + "/")
    }

    js_ex = ".js"
    html_ex = ".html"
    objc_m_ex = ".m"
    swift_ex = ".swift"
    tab_size = 4
    vanilla_zero_padding = 0
    jquery_zero_padding = 0
    node_zero_padding = 0
    node_multifile_zero_padding = 0
    objectivec_zero_padding = 0
    swift_zero_padding = 0
    num_vanilla_files = 0
    num_jquery_files = 0
    num_node_files = 0
    num_node_multifile_dirs = 0
    num_objectivec_dirs = 0
    jquery_dep = "https://code.jquery.com/jquery-2.2.4.min.js"
    angular_dep = "https://ajax.googleapis.com/ajax/libs/angularjs/1.4.9/angular.min.js"

    def __init__(self, type, verbose, depth, mod_depth):

        if type is None:
            pass  # TODO determine default type
        if depth is None:
            depth = 1
        if mod_depth is None:
            mod_depth = 1

        self.set_type(type)
        self.set_verbose(verbose)
        self.set_depth(depth)
        self.set_module_depth(mod_depth)
        Properties.num_vanilla_files = self.calc_num_vanilla_files(depth)
        Properties.num_jquery_files = self.calc_num_jquery_files(depth)
        Properties.num_node_files = self.calc_num_node_files(depth, mod_depth)
        Properties.num_node_multifile_dirs = self.calc_num_node_multifile_dirs(depth, mod_depth)
        #Properties.num_objectivec_dirs = self.calc_num_objectivec_files(depth)

        Properties.vanilla_zero_padding = self.len_num(Properties.num_vanilla_files)
        Properties.jquery_zero_padding = self.len_num(Properties.num_jquery_files)
        Properties.node_zero_padding = self.len_num(Properties.num_node_files)
        Properties.node_multifile_zero_padding = self.len_num(self.num_node_multifile_dirs)
        #Properties.node_objectivec_padding = self.len_num(self.num_objectivec_dirs)

    @staticmethod
    def set_type(type):
        Properties.type = type

    @staticmethod
    def set_verbose(verbose):
        Properties.verbose = verbose

    # Set the depth
    @staticmethod
    def set_depth(depth):
        Properties.depth = depth

    @staticmethod
    def set_module_depth(module_depth):
        Properties.module_depth = module_depth

    @staticmethod
    def calc_num_vanilla_files(depth):
        vanilla_count = len(Code.enum_blocks)
        return math.pow(vanilla_count, depth)

    @staticmethod
    def calc_num_jquery_files(depth):
        vanilla_count = len(Code.enum_blocks)
        jq_count = len(Code.enum_jq_events)

        return math.pow(vanilla_count + jq_count, depth) - math.pow(vanilla_count, depth)

    @staticmethod
    def calc_num_node_files(depth, module_depth):
        vanilla_count = len(Code.enum_blocks)
        decorator_count = len(Code.enum_node_module_decorators)

        node_count = 0

        for d in range(0, module_depth+1):
            node_count += math.pow(decorator_count, d)

        return math.pow(vanilla_count + node_count, depth) - math.pow(vanilla_count, depth)

    @staticmethod
    def calc_num_node_multifile_dirs(depth, module_depth):
        vanilla_count = len(Code.enum_blocks)
        decorator_count = len(Code.enum_node_module_decorators)

        node_count = 0

        for d in range(0, module_depth+1):
            node_count += math.pow(decorator_count, d)

        return math.pow(vanilla_count, depth) * node_count

    @staticmethod
    def calc_num_objectivec_files(depth):
        objectivec_count = len(Code.enum_blocks)

        return math.pow(objectivec_count, depth)

    @staticmethod
    def len_num(num):
        num = math.fabs(num)

        # Corner case, cannot log <= 0
        if num == 0:
            return 1

        return math.floor(math.log(num, 10) + 1)