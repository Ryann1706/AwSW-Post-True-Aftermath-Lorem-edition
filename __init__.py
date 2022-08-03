
from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

@loadable_mod
class AWSWMod(Mod):
    name = "Post-True + Aftermath: Lorem edition"
    version = "1.0"
    author = "Ryann1706"
    dependencies = ["MagmaLink"]

    def mod_load(self):

        ml.find_label("trueendings") \
            .search_say("She closed her eyes as a single tear ran down her face.", depth=2000) \
            .hook_to("ryann_lorem_post_true", condition="loremscenesfinished == 4" and "loremstatus == \"good\"")

    def mod_complete(self):
        pass
