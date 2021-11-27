import json
import os
class AppService:
    
    tasks = [
        {
	    'service_name': 'myapplication',
	    'version': '1.0.0',
	    'git_commit_sha': 'abc50002738',
	    "environment": {
		"service_port": os.getenv("port"),
		"log_level": os.getenv("loglevel")
	    }
	}
    ]

    def __init__(self):
        self.tasksJSON = json.dumps(self.tasks)

    def get_tasks(self):
        return self.tasksJSON

