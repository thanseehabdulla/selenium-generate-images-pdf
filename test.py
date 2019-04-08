import os

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from pyvirtualdisplay import Display
import time


def get_file_screenshot(url):
    try:
        display = Display(visible=0, size=(1800, 1600))
        display.start()
        # now  Firefox will run in a virtual display.
        browser = webdriver.Firefox(executable_path='/home/sinergia/Desktop/davis/selenium/geckodriver')
        # browser.set_window_size(2046, 2046)
        # browser.fullscreen_window()
        browser.implicitly_wait(30)
        browser.set_page_load_timeout(150)
        browser.get(url)
        time.sleep(30)
        elements = browser.find_elements_by_css_selector('.react-grid-item.react-draggable.react-resizable')
        i = 0
        for element in elements:
            i = i + 1
            element_png = element.screenshot_as_png
            with open(f"test{i}.png", "wb") as file:
                file.write(element_png)
        # browser.get_screenshot_as_png(filename="test.png")
        browser.quit()
        display.stop()
    except Exception as e:
        print(e)


url = "https://demo.elastic.co/app/kibana#/dashboard/06fa0b60-121a-11e8-8c94-a3d8d0cfd62b?_g=(refreshInterval:(pause:!t,value:0),time:(from:now-5y,mode:quick,to:now))&_a=(description:'',filters:!(),fullScreenMode:!f,options:(darkTheme:!t,hidePanelTitles:!f,useMargins:!f),panels:!((embeddableConfig:(mapCenter:!(35.746512259918504,-29.443359375000004),mapZoom:3),gridData:(h:25,i:'2',w:48,x:0,y:70),id:'7fe767b0-11fd-11e8-8c94-a3d8d0cfd62b',panelIndex:'2',title:'Global%20User%20Activity',type:visualization,version:'6.5.4'),(gridData:(h:30,i:'17',w:24,x:0,y:10),id:a0340090-1389-11e8-8c94-a3d8d0cfd62b,panelIndex:'17',title:Users,type:visualization,version:'6.5.4'),(gridData:(h:10,i:'26',w:24,x:24,y:0),id:fec4c5c0-139a-11e8-8c94-a3d8d0cfd62b,panelIndex:'26',title:'User%20Activity',type:visualization,version:'6.5.4'),(gridData:(h:5,i:'29',w:24,x:0,y:5),id:'5e89e2b0-13a0-11e8-8c94-a3d8d0cfd62b',panelIndex:'29',title:'',type:visualization,version:'6.5.4'),(gridData:(h:5,i:'32',w:24,x:0,y:0),id:aa01fff0-13bb-11e8-8c94-a3d8d0cfd62b,panelIndex:'32',title:'',type:visualization,version:'6.5.4'),(gridData:(h:10,i:'33',w:24,x:24,y:10),id:'27f9bd40-13ca-11e8-8c94-a3d8d0cfd62b',panelIndex:'33',title:'Access%20Requests',type:visualization,version:'6.5.4'),(gridData:(h:20,i:'34',w:24,x:24,y:20),id:fca6aa70-13cb-11e8-8c94-a3d8d0cfd62b,panelIndex:'34',title:'Resource%20Changes',type:visualization,version:'6.5.4'),(gridData:(h:15,i:'35',w:24,x:24,y:55),id:f7d7bb80-1824-11e8-8c94-a3d8d0cfd62b,panelIndex:'35',title:'Top%20Resource%20Groups',type:visualization,version:'6.5.4'),(embeddableConfig:(vis:(params:(sort:(columnIndex:3,direction:desc)))),gridData:(h:30,i:'37',w:24,x:0,y:40),id:f93f09d0-1bec-11e8-8c94-a3d8d0cfd62b,panelIndex:'37',title:'Top%20Caller%20IPs',type:visualization,version:'6.5.4'),(gridData:(h:15,i:'38',w:24,x:24,y:40),id:'2e863080-1bef-11e8-8c94-a3d8d0cfd62b',panelIndex:'38',title:'Top%20Resource%20Types',type:visualization,version:'6.5.4')),query:(language:lucene,query:''),timeRestore:!f,title:'%5BAzure%20Monitor%5D%20User%20Activity',viewMode:view)"

get_file_screenshot(url)

# write-html.py

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

    <div class="row">
    <div class="col-lg-6 margintop"><img src="test2.png" style="width:100%" /></div>
    <div class="col-lg-6 margintop"><img src="test5.png" style="width:100%" /></div>
    <div class="col-lg-6 margintop"><img src="test4.png" style="width:100%" /></div>
    <div class="col-lg-6 margintop"><img src="test7.png" style="width:100%" /></div>
    <div class="col-lg-6 margintop"><img src="test6.png" style="width:100%" /></div>
    <div class="col-lg-6 margintop"><img src="test8.png" style="width:100%" /></div>
    <div class="col-lg-6 margintop"><img src="test9.png" style="width:100%" /></div>
    <div class="col-lg-6 margintop"><img src="test11.png" style="width:100%" /></div>
    <div class="col-lg-6 margintop"><img src="test10.png" style="width:100%" /></div>


    </div>

</div>

</body>

</html>"""

f.write(message)
f.close()
