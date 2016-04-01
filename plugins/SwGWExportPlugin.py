import SWPlugin
import logging
import json

logger = logging.getLogger("SWProxy")
open("SWGWexport.json", 'w').close()

class SwGWExportPlugin(SWPlugin.SWPlugin):
    def process_request(self, req_json, resp_json):
        if "Guild" in resp_json.get('command'):
            guild_id = resp_json.get('guild_id')
            filename = "SWGWexport.json"

            with open(filename, "a") as f:

                f.write("#" + resp_json.get('command') + "\n")
                f.write(json.dumps(resp_json, sort_keys=True, indent=4, separators=(',', ': ')))
                f.write("\n\n")
                
            print "Updated GW status file " + filename