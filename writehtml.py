import json
import os
# write-html.py

data = json.load(open('project.json', 'r'))
classes = data['classes']
images = data['images']
output_image_folder = data['output_image_folder']
output_html_folder = data['output_html_folder']


if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) +"/"+ output_html_folder):
    os.makedirs(output_html_folder)

f = open(output_html_folder+'/new.html', 'w')

message = """<html>

<head>
    <title>Flex</title>

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<style>

    .margintop{
        margin-top:10px;
    }
</style>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</head>

<body>

<div class="main">

    <div class="row">"""

for i in range(len(images)):
    message += """<div class="margintop """ + classes[i] + """ "><img src=../""" + output_image_folder + "/" + images[
        i] + """ style="width:100%" /></div>"""

message += """</div>

</div>

</body>

</html>"""

f.write(message)
f.close()
