#!/usr/bin/env python3

import json

mail = [ 'p2' ]

groups = {
	'testservers'  : {
		"hosts" : [ "w00", "d00" ],
		"vars"	: {
			"http_port" : 80,
			"beverage"  : "0xC0FFEE",
			"os"	    : "CentOS",
            "ansible_user" : "ansible",
		},
	},
	'mailservers' : mail,
	"_meta" : {
		"hostvars" : {
			"w00" : { "ansible_python_interpreter" : "auto_silent" },
			"p2" : { "ansible_host" : "alice" },
		}
	}
}

print(json.dumps(groups, indent=4))
