# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import subprocess
import base64
import subprocess
import shlex
import flask

# Input injection
def transcode_file(request, filename):
    "DOC STRING"
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def foonction(request, user):
    "DOC STRING 2"
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh():
    "CLASS DOC STRING"
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))

def import_urlib_version(version):
    "ANOTHER DOC STRING"
    split_version = shlex.split(version)
    sanitized_version = shlex.quote(split_version)
    exec("import urllib%s as urllib" % sanitized_version)

@app.route('/')
def index():
    "LAST DOC STRING"
    module = flask.request.args.get("module")
    import_urlib_version(module)


print(base64.b64encode(pickle.dumps(RunBinSh())))
