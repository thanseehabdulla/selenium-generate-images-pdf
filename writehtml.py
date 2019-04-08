# write-html.py

url = ""
classes = []

with open('project.json') as json_file:
    data = json_file
    for p in data['data']:
        url = p['url']
        classes = p['classess']
        images = p['images']


f = open('new.html', 'w')

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

message += """"<div class="col-lg-6 margintop"><img src="test2.png" style="width:100%" /></div>"""

for i in range(len(images)):
    message += """<div class="margintop""" + classes[i] + """ "><img src=""" + images[
        i] + """ style="width:100%" /></div>"""

message += """</div>

</div>

</body>

</html>"""

f.write(message)
f.close()