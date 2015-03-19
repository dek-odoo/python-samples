#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar

# load demo data
# repair invalid json files
# delete student
# never open file in each function, which will cause too many open file handlers
# viewdata,loaddemodata,insertdata

#PLEASE READ
#THE FOLLOWING REQUIRES MY CUSTOM DEBUGG CLASS TO WORK
import os
import sys

from time import gmtime, strftime

import json
import urlparse


import inspect

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException
from werkzeug.wsgi import SharedDataMiddleware
from jinja2 import Environment, FileSystemLoader
import jinja2
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class deprecatedd():

    def __init__(self, f):
        self.fun = f
        print "init"

    def __call__(self, *arg):
        print "call"
        self.fun()


class DataStore:
    sid = -1


class App:
    __jsonFileName = 'newdata.json'
    __backupFileName = 'backupjson.json'
    __datafilesPath = 'static/datafiles/'
    jsonFile = __datafilesPath + __jsonFileName
    backupjsonFile = __datafilesPath + __backupFileName

    def __init__(self):
        self.url_map = Map([
            Rule('/', endpoint='index'),
            Rule('/index', endpoint='index'),
            Rule('/insert', endpoint='insert'),
            Rule('/edit', endpoint='edit'),
            Rule('/loaddemodata', endpoint='loadDemoData'),
            Rule('/remove', endpoint='remove'),
            Rule('/search', endpoint='search'),
        ])
        self.templateLoader = FileSystemLoader(searchpath="templates/")
        self.templateEnv = Environment(
            loader=self.templateLoader,
            undefined=jinja2.StrictUndefined)
        self.indexTemplate = "newjinjatem.html"
        self.insertTemplate = "insertTemplate.html"
        self.editTemplate = "editTemplate.html"

    class gateway():

        def __init__(self, mimetype='text/html'):
            self.mimetype = mimetype

        def __call__(self, fun):
            self.fun = fun

            def setRes(*args):
                return Response(self.fun(*args), mimetype=self.mimetype)
            return setRes

    # Endpoints
    #*************************************************************************

    # loadDemoData- to load demo data
    @gateway(mimetype="text/html")
    def loadDemoData(self, request, args):
        backupcontent = open(App.backupjsonFile, 'r').read()
        App.replaceFiledata(App.jsonFile, backupcontent)
        return self.loadDefaultTemplate(request)

    @gateway(mimetype='text/html')
    def index(self, request, args):
        return self.loadDefaultTemplate(request)

    @gateway(mimetype='text/html')
    def edit(self, request, args):
        postDataLen = len(request.form.values())
        print "postDataLen", postDataLen
        if postDataLen != 0:
            print "!@#$%^&*()**********"
            studentdata = ''
            for firstrec in request.form.iteritems():
                studentdata = str(list(firstrec)[0])
            self.removeIdFromFile(DataStore.sid)
            self.insertRecord(App.jsonFile, studentdata)
            jsondata = App.getJsonFromFile(App.jsonFile)
            self.renderTemplate(self.indexTemplate, jsondata=jsondata,
                                loadstudentid=self.sid)
        # self.deletesid = self.sid
        # //we can use sessionMIddleware/hidden fields/DataStore,
        # but a workaround solution
        DataStore.sid = self.sid
        self.template = self.templateEnv.get_template(self.editTemplate)
        jsondata = App.getJsonFromFile(App.jsonFile)
        return self.template.render(jsondata=jsondata[self.sid])

    @gateway(mimetype='text/html')
    def remove(self, request, args):
        # self.removeCurIdFromFile()
        self.removeIdFromFile(self.sid)
        return self.loadDefaultTemplate(request)

    @gateway(mimetype='text/html')
    def insert(self, request, args):
        postdatalen = len(request.form.values())
        if postdatalen != 0:
            studentdata = ''
            for firstrec in request.form.iteritems():
                studentdata = str(list(firstrec)[0])
            App.insertRecord(App.jsonFile, studentdata)
            return self.loadDefaultTemplate(request)
        self.template = self.templateEnv.get_template(self.insertTemplate)
        return self.template.render()

    def renderTemplate(self, templateName, **dataDict):
        template1 = self.templateEnv.get_template(templateName)
        return template1.render(dataDict)

    # pass
    # @gateway(mimetype='application/json')
    # def search(self, request, args):
    #     pass
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S

    @staticmethod
    def insertRecord(file, record):
        jsoncontent = open(App.jsonFile).read()
        App.replaceFiledata(
            App.jsonFile, jsoncontent[0:len(jsoncontent) - 1] +
            # "," +
            record + "]")

    # @staticmethod
    def removeIdFromFile(self, sid):
        Debugg.info("Removing SID : " + str(sid))
        jsondata = App.getJsonFromFile(App.jsonFile)
        i = 0
        try:
            with open(App.jsonFile, 'w') as outfile:
                outfile.write('[')
                for student in jsondata:  # use yield
                    Debugg.info("STR(I) " + str(i))
                    if sid != i:
                        json.dump(jsondata[i], outfile)
                        try:
                            if jsondata[i + 1]:
                                outfile.write(',')
                        except IndexError, ie:
                            Debugg.info('IndexOutOfBounds %s', str(ie))
                    else:
                        Debugg.info(type(student))
                        Debugg.info(student)
                    i += 1
                outfile.write(']')
            self.sid -= 1
        except Exception as excep:
            Debugg.info(type(excep), magic="warning")
            Debugg.info(excep, magic="warning")

    # version management ;)
    @deprecatedd
    def removeCurIdFromFile(self):
        # acquire lock
        # Debugg.info(jsondata)
        # Debugg.info("i is %d" % i)
        Debugg.info(self.sid)
        jsondata = App.getJsonFromFile(App.jsonFile)
        i = 0
        try:
            with open(App.jsonFile, 'w') as outfile:
                outfile.write('[')
            for student in jsondata:  # use yield
                if self.sid != i:
                    json.dump(jsondata[i], outfile)
                    try:
                        if jsondata[i + 1]:
                            outfile.write(',')
                    except IndexError, ie:
                        Debugg.info('IndexOutOfBounds %s', str(ie))
                else:
                    Debugg.info(type(student))
                    Debugg.info(student)
                i += 1
            outfile.write(']')
        except Exception as excep:
            Debugg.info(type(excep))
            Debugg.info(excep)
            # release lock

    def loadDefaultTemplate(self, request):
        self.jsondata = App.getJsonFromFile(App.jsonFile)
        Debugg.info(self.sid)
        try:
            Debugg.info(self.jsondata[self.sid])
        except IndexError:
            Debugg.info(magic="warning", msg="*" * 50 + "IndexError")

        # Debugg.trace()
        return self.renderTemplate(self.indexTemplate, jsondata=self.jsondata,
                                   NosubjectRows=3,
                                   title="StudentForm",
                                   loadstudentid=self.sid)

    @staticmethod
    def repairJsonFile():
        Debugg.info('inside repairJsonFile')
        try:
            json_data = open(App.jsonFile).read()
            Debugg.info("@@@ " + "repairJsonFile")
            Debugg.info(json_data)
            json_data = json_data[0:json_data.rfind('}')]
            json_data = json_data + '}]'
            App.replaceFiledata(App.jsonFile, json_data)
            Debugg.info("$$$ " + json_data)
        except ValueError, v:
            Debugg.info(str(v))
            # App.repairJsonFile()

    @staticmethod
    def replaceFiledata(file, data):
        with open(file, 'w') as outfile:
            outfile.write(data)

    @staticmethod
    def getJsonFromFile(filename):
        try:
            json_data = open(filename)
            jsondata = json.load(json_data)
            json_data.close()
            return jsondata
        except ValueError, v:
            Debugg.info("%s", str(v))
            App.repairJsonFile()
            # A workaround solution
            json_data = open(filename)
            jsondata = json.load(json_data)
            json_data.close()
            return jsondata


def getParamFromUrlRequest(request, filterStr):
    try:
        urldict = urlparse.parse_qs(request.environ['QUERY_STRING'])
        Debugg.info("SID ISSSS " + urldict[filterStr][0])
        # do not write here self.sid
        # doing that will blow up the whole thing
        sid = urldict[filterStr][0]
        Debugg.info(sid)
        if sid:
            print "return", sid
            return sid
    except:
        Debugg.info(
            __file__ + sys._getframe().f_code.co_name)
        return 0


def getCurrentSid(request):
    return int(getParamFromUrlRequest(request, "sid"))


def processRequest(request):
    app = App()
    urls = app.url_map.bind_to_environ(request.environ)
    try:
        endpoint, args = urls.match()
        # refactor
        # common parameter SID that is assigned on each request to use later
        app.sid = getCurrentSid(request)
        if app.sid is None:
            app.sid = 0
        print inspect.currentframe().f_back.f_lineno
        # Debugg.info(msg, lineno)
        Debugg.info(
            msg="SID is " + str(app.sid),
            lineno=inspect.currentframe().f_back.f_lineno)
        # Debugg.info()
        return getattr(app, endpoint)(request, args)
    except HTTPException, e:
        print e
        # Debugg.info("Exception" + str(e))


@Request.application
def application(request):
    Debugg.info('App Started')  # use Debugg
    return Response(processRequest(request), mimetype='text/html')
    # return processRequest(request)

if __name__ == '__main__':
    application = SharedDataMiddleware(application, {
        '/static': os.path.join(os.path.dirname(__file__), 'static')
    })

    try:
        port = int(sys.argv[1])
    except:
        port = 4000
    run_simple('localhost', port, application)
