from {{cookiecutter.project_slug}}.{{cookiecutter.pipeline_slug}}.common import Task
import pkg_resources


class PythonTask(Task):
    def _execute_sql(self):
        self.logger.info("Launching SQL task")
        
    def launch(self):
        self.logger.info("Launching SQL task")
        self._execute_sql()
        self.logger.info("SQL task finished!")

# if you're using python_wheel_task, you'll need the entrypoint function to be used in setup.py
def entrypoint():  # pragma: no cover
    task = PythonTask()
    task.launch()

# if you're using spark_python_task, you'll need the __main__ block to start the code execution
if __name__ == '__main__':
    entrypoint()