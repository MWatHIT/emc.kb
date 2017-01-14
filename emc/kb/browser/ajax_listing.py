#-*- coding: UTF-8 -*-
from zope.interface import Interface
from zope.component import getMultiAdapter
from five import grok
import json
import datetime
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFCore import permissions
from Products.CMFCore.interfaces import ISiteRoot
from plone.memoize.instance import memoize
from emc.kb import _
from Products.Five.browser import BrowserView
# from collective.gtags.source import TagsSourceBinder
from zope.component import getUtility
# input data view
from plone.directives import form
from z3c.form import field, button
from Products.statusmessages.interfaces import IStatusMessage
from emc.kb.interfaces import InputError
from emc.kb.interfaces import IModelLocator,IFashejLocator,IJieshoujLocator,IFashetxLocator,IJieshoutxLocator,IDianxingtxzyzkLocator
from emc.kb.mapping_db import IModel,Model
from emc.kb.mapping_db import Fashej,IFashej
from emc.kb.mapping_db import Jieshouj,IJieshouj
from emc.kb.mapping_db import IFashetx,Fashetx
from emc.kb.mapping_db import IJieshoutx,Jieshoutx
from emc.kb.mapping_db import ILvboq,Lvboq
from emc.kb.mapping_db import IDianxingtxzyzk,Dianxingtxzyzk
from emc.kb.mapping_db import ITianxianzk,Tianxianzk
from emc.kb.mapping_db import IJieshoujzk,Jieshoujzk
from emc.kb.mapping_db import IFashejzk,Fashejzk
from emc.kb.contents.ormfolder import Iormfolder
# update data view
from zope.interface import implements
from zope.publisher.interfaces import IPublishTraverse
from zExceptions import NotFound
from emc.kb import InputDb
grok.templatedir('templates')

class ModelView(BrowserView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    @memoize
    def pm(self):
        context = aq_inner(self.context)
        pm = getToolByName(context, "portal_membership")
        return pm

    def getPathQuery(self):

        """返回 db url
        """
        query = {}
        query['path'] = "/".join(self.context.getPhysicalPath())
        return query

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        from emc.kb.mapping_db import  Model
        from emc.kb.interfaces import IModelLocator
        from zope.component import getUtility
        locator = getUtility(IModelLocator)
        models = locator.queryModel(start=query['start'],size=query['size'])
        return models

# fashej table
class FashejView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        from emc.kb.mapping_db import  Fashej
        from emc.kb.interfaces import IFashejLocator
        from zope.component import getUtility
        locator = getUtility(IFashejLocator)
        recorders = locator.query(start=query['start'],size=query['size'])
        return recorders


class JieshoujView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        from emc.kb.mapping_db import  Jieshouj
        from emc.kb.interfaces import IJieshoujLocator
        from zope.component import getUtility
        locator = getUtility(IJieshoujLocator)
        recorders = locator.query(start=query['start'],size=query['size'])
        return recorders


# fashej table
class FashetxView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        from emc.kb.mapping_db import  Fashetx
        from emc.kb.interfaces import IFashetxLocator
        from zope.component import getUtility
        locator = getUtility(IFashetxLocator)
        recorders = locator.query(start=query['start'],size=query['size'])
        return recorders


class JieshoutxView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        from emc.kb.mapping_db import  Jieshoutx
        from emc.kb.interfaces import IJieshoutxLocator
        from zope.component import getUtility
        locator = getUtility(IJieshoutxLocator)
        recorders = locator.query(start=query['start'],size=query['size'])
        return recorders

class LvboqView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        from emc.kb.mapping_db import  Lvboq
        from emc.kb.interfaces import ILvboqLocator
        from zope.component import getUtility
        locator = getUtility(ILvboqLocator)
        recorders = locator.query(start=query['start'],size=query['size'])
        return recorders


class DianxingtxzyzkView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        from emc.kb.interfaces import IDianxingtxzyzkLocator
        from zope.component import getUtility
        locator = getUtility(IDianxingtxzyzkLocator)
        recorders = locator.query(start=query['start'],size=query['size'])
        return recorders


class TianxianzkView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        from emc.kb.interfaces import ITianxianzkLocator
        from zope.component import getUtility
        locator = getUtility(ITianxianzkLocator)
        recorders = locator.query(start=query['start'],size=query['size'])
        return recorders


class JieshoujzkView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        from emc.kb.interfaces import IJieshoujzkLocator
        from zope.component import getUtility
        locator = getUtility(IJieshoujzkLocator)
        recorders = locator.query(start=query['start'],size=query['size'])
        return recorders


class FashejzkView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        from emc.kb.interfaces import IFashejzkLocator
        from zope.component import getUtility
        locator = getUtility(IFashejzkLocator)
        recorders = locator.query(start=query['start'],size=query['size'])
        return recorders





 # ajax multi-condition search relation db
class ajaxsearch(grok.View):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.context(Interface)
    grok.name('dbajaxsearch')
    grok.require('zope2.View')
#     grok.require('emc.project.view_projectsummary')
    def Datecondition(self,key):
        "构造日期搜索条件"
        end = datetime.datetime.today()
#最近一周
        if key == 1:
            start = end - datetime.timedelta(7)
#最近一月
        elif key == 2:
            start = end - datetime.timedelta(30)
#最近一年
        elif key == 3:
            start = end - datetime.timedelta(365)
#最近两年
        elif key == 4:
            start = end - datetime.timedelta(365*2)
#最近五年
        else:
            start = end - datetime.timedelta(365*5)
#            return    { "query": [start,],"range": "min" }
        datecondition = { "query": [start, end],"range": "minmax" }
        return datecondition

    def searchview(self,viewname="model_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def render(self):
#        self.portal_state = getMultiAdapter((self.context, self.request), name=u"plone_portal_state")
        searchview = self.searchview()
 # datadic receive front ajax post data
        datadic = self.request.form
        start = int(datadic['start']) # batch search start position
        size = int(datadic['size'])      # batch search size
        sortcolumn = datadic['sortcolumn']
        sortdirection = datadic['sortdirection']
        keyword = (datadic['searchabletext']).strip()
#         origquery = searchview.getPathQuery()
        origquery = {}
        origquery['sort_on'] = sortcolumn
        # sql db sortt_order:asc,desc
        origquery['sort_order'] = sortdirection
 #模糊搜索
        if keyword != "":
            origquery['SearchableText'] = '%'+keyword+'%'
#origquery provide  batch search
        origquery['size'] = size
        origquery['start'] = start
#totalquery  search all
        totalquery = origquery.copy()
        totalquery['size'] = 0
        # search all   size = 0 return numbers of recorders
        totalnum = searchview.search_multicondition(totalquery)
        resultDicLists = searchview.search_multicondition(origquery)
        del origquery
        del totalquery
#call output function
# resultDicLists like this:[(u'C7', u'\u4ed6\u7684\u624b\u673a')]
        data = self.output(start,size,totalnum, resultDicLists)
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(data)

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        for i in resultDicLists:
            out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(num)s</td>
                                <td class="col-md-2 text-left"><a href="%(objurl)s">%(title)s</a></td>
                                <td class="col-md-7">%(description)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            num=str(k + 1),
                                            title=i[0],
                                            description= i[1],
                                            edit_url="%s/@@update_model/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_model/%s" % (contexturl,i[0]))
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data


class Fashejajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """

    grok.name('fashej_ajaxsearch')

    def searchview(self,viewname="fashej_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        for i in resultDicLists:
            out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(sbdm)s</td>
                                <td class="col-md-1 text-left"><a href="%(objurl)s">%(sbmc)s</a></td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(freq)s</td>
                                <td class="col-md-1">%(pd_upper)s</td>
                                <td class="col-md-1">%(pd_lower)s</td>
                                <td class="col-md-1">%(num)s</td>
                                <td class="col-md-1">%(freq_upper)s</td>
                                <td class="col-md-1">%(freq_lower)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            sbdm=i[0],
                                            sbmc= i[1],
                                            pcdm= i[2],
                                            location= i[3],
                                            freq= i[4],
                                            pd_upper= i[5],
                                            pd_lower= i[6],
                                            num= i[7],
                                            freq_upper= i[8],
                                            freq_lower= i[9],
                                            edit_url="%s/@@update_fashej/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_fashej/%s" % (contexturl,i[0]))
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data


class Jieshoujajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """

    grok.name('jieshouj_ajaxsearch')

    def searchview(self,viewname="jieshouj_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        for i in resultDicLists:
            out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(sbdm)s</td>
                                <td class="col-md-1 text-left"><a href="%(objurl)s">%(sbmc)s</a></td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(fb_upper)s</td>
                                <td class="col-md-1">%(fb_lower)s</td>
                                <td class="col-md-1">%(freq)s</td>
                                <td class="col-md-1">%(f_upper)s</td>
                                <td class="col-md-1">%(f_lower)s</td>
                                <td class="col-md-1">%(bw_receiver)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            sbdm=i[0],
                                            sbmc= i[1],
                                            pcdm= i[2],
                                            location= i[3],
                                            fb_upper= i[4],
                                            fb_lower= i[5],
                                            freq= i[6],
                                            f_upper= i[7],
                                            f_lower= i[8],
                                            bw_receiver= i[9],
                                            edit_url="%s/@@update_jieshouj/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_jieshouj/%s" % (contexturl,i[0]))
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data

class Fashetxajaxsearch(Fashejajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """

    grok.name('fashetx_ajaxsearch')

    def searchview(self,viewname="fashetx_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        for i in resultDicLists:
            out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(cssbdm)s</td>
                                <td class="col-md-1 text-left"><a href="%(objurl)s">%(cssbmc)s</a></td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(gain)s</td>
                                <td class="col-md-1">%(polarization)s</td>
                                <td class="col-md-1">%(fwbskd)s</td>
                                <td class="col-md-1">%(fybskd)s</td>
                                <td class="col-md-1">%(txzxj)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            cssbdm=i[0],
                                            cssbmc= i[1],
                                            pcdm= i[2],
                                            location= i[3],
                                            gain= i[4],
                                            polarization= i[5],
                                            fwbskd= i[6],
                                            fybskd= i[7],
                                            txzxj= i[8],
                                            edit_url="%s/@@update_fashetx/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_fashetx/%s" % (contexturl,i[0]))
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data

class Jieshoutxajaxsearch(Fashejajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """

    grok.name('jieshoutx_ajaxsearch')

    def searchview(self,viewname="jieshoutx_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        for i in resultDicLists:
            out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(cssbdm)s</td>
                                <td class="col-md-1 text-left"><a href="%(objurl)s">%(cssbmc)s</a></td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(gain)s</td>
                                <td class="col-md-1">%(polarization)s</td>
                                <td class="col-md-1">%(fwbskd)s</td>
                                <td class="col-md-1">%(fybskd)s</td>
                                <td class="col-md-1">%(txzxj)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            cssbdm=i[0],
                                            cssbmc= i[1],
                                            pcdm= i[2],
                                            location= i[3],
                                            gain= i[4],
                                            polarization= i[5],
                                            fwbskd= i[6],
                                            fybskd= i[7],
                                            txzxj= i[8],
                                            edit_url="%s/@@update_jieshoutx/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_jieshoutx/%s" % (contexturl,i[0]))
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data

class Dianxingtxzyzkajaxsearch(Fashejajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """

    grok.name('dianxingtxzyzk_ajaxsearch')

    def searchview(self,viewname="dianxingtxzyzk_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        for i in resultDicLists:
            out = """<tr class="text-left">
                                <td class="col-md-1 text-left"><a href="%(objurl)s">%(type_antennas)s</a></td>
                                <td class="col-md-1">%(gain)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            type_antennas=i[0],
                                            gain= i[1],
                                            edit_url="%s/@@update_dianxingtianxianzyzk/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_dianxingtianxianzyzk/%s" % (contexturl,i[0]))
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data
#
#
#
# Delete Update Input block
class DeleteModel(form.Form):
    "delete the specify model recorder"
    implements(IPublishTraverse)
    grok.context(Iormfolder)
    grok.name('delete_model')
    grok.require('emc.kb.input_db')

    label = _(u"delete model data")
    fields = field.Fields(IModel).omit('modelId')
    ignoreContext = False

    xhdm = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.xhdm is None:
            self.xhdm = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IModelLocator)
        #to do
        #fetch the pending deleting  record
        return locator.getModelByCode(self.xhdm)

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations

        #Let z3c.form do its magic
        super(DeleteModel, self).update()


    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IModelLocator)
        try:
            funcations.DeleteByCode(self.xhdm)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/model_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')

class InputModel(form.Form):
    """input db model table data
    """

    grok.context(Iormfolder)
    grok.name('input_model')
    grok.require('emc.kb.input_db')
    label = _(u"Input model data")
    fields = field.Fields(IModel).omit('modelId')
    ignoreContext = True

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(InputModel, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit model recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IModelLocator)
        try:
            funcations.addModel(xhdm=data['xhdm'],xhmc=data['xhmc'])
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/model_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')

class UpdateModel(form.Form):
    """update model table row data
    """

    implements(IPublishTraverse)
    grok.context(Iormfolder)
    grok.name('update_model')
    grok.require('emc.kb.input_db')

    label = _(u"update model data")
    fields = field.Fields(IModel).omit('modelId','xhdm')
    ignoreContext = False
    xhdm = None
    #receive url parameters
    # reset content
    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
        return locator.getModelByCode(self.xhdm)


    def publishTraverse(self, request, name):
        if self.xhdm is None:
            self.xhdm = name
            return self
        else:
            raise NotFound()

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(UpdateModel, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IModelLocator)
        try:
            funcations.updateByCode(xhdm=self.xhdm,xhmc=data['xhmc'])
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/model_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')
##发射机数据库操作
class DeleteFashej(DeleteModel):
    "delete the specify fashej recorder"

    grok.name('delete_fashej')
    label = _(u"delete fa she ji data")
    fields = field.Fields(IFashej).omit('fashejId')


    sbdm = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.sbdm is None:
            self.sbdm = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IFashejLocator)
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.sbdm)

    def update(self):
        self.request.set('disable_border', True)

        #Let z3c.form do its magic
        super(DeleteFashej, self).update()


    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IFashejLocator)
        try:
            funcations.DeleteByCode(self.sbdm)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/fashej_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/fashej_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/fashej_listings')


class InputFashej(InputModel):
    """input db fashej table data
    """

    grok.name('input_fashej')

    label = _(u"Input fa she ji data")
    fields = field.Fields(IFashej).omit('fashejId')

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(InputFashej, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit model recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IFashejLocator)
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')


class UpdateFashej(UpdateModel):
    """update model table row data
    """
    grok.name('update_fashej')
    label = _(u"update fa she ji data")
    fields = field.Fields(IFashej).omit('fashejId')

    sbdm = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.sbdm is None:
            self.sbdm = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IFashejLocator)
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.sbdm)

    def update(self):
        self.request.set('disable_border', True)
        # Let z3c.form do its magic
        super(UpdateFashej, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IFashejLocator)

        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')

##end发射机 数据库操作

##接收机 数据库操作
class DeleteJieshouj(DeleteModel):
    "delete the specify jieshouj recorder"

    grok.name('delete_jieshouj')
    label = _(u"delete jie shou ji data")
    fields = field.Fields(IJieshouj).omit('jieshoujId')


    sbdm = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.sbdm is None:
            self.sbdm = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IJieshoujLocator)
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.sbdm)

    def update(self):
        self.request.set('disable_border', True)

        #Let z3c.form do its magic
        super(DeleteJieshouj, self).update()


    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IJieshoujLocator)
        try:
            funcations.DeleteByCode(self.sbdm)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/jieshouj_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/jieshouj_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/jieshouj_listings')

class InputJieshouj(InputModel):
    """input db jieshouj table data
    """

    grok.name('input_jieshouj')

    label = _(u"Input jie shou ji data")
    fields = field.Fields(IJieshouj).omit('jieshoujId')

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(InputJieshouj, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit model recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IJieshoujLocator)
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')

class UpdateJieshouj(UpdateModel):
    """update model table row data
    """
    grok.name('update_jieshouj')
    label = _(u"update jieshouj data")
    fields = field.Fields(IJieshouj).omit('jieshoujId')

    sbdm = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.sbdm is None:
            self.sbdm = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IJieshoujLocator)
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.sbdm)

    def update(self):
        self.request.set('disable_border', True)
        # Let z3c.form do its magic
        super(UpdateJieshouj, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IJieshoujLocator)

        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')
# end 接收机 数据库操作

## 发射天线 数据库操作
class DeleteFashetx(DeleteModel):
    "delete the specify Fashetx recorder"

    grok.name('delete_fashetx')
    label = _(u"delete fa she tian xian data")
    fields = field.Fields(IFashetx).omit('fashetxId')


    cssbdm = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.cssbdm is None:
            self.cssbdm = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IFashetxLocator)
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.cssbdm)

    def update(self):
        self.request.set('disable_border', True)

        #Let z3c.form do its magic
        super(DeleteFashetx, self).update()


    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IFashetxLocator)
        try:
            funcations.DeleteByCode(self.cssbdm)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/fashetx_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/fashetx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/fashetx_listings')

class InputFashetx(InputModel):
    """input db fashetx table data
    """

    grok.name('input_fashetx')

    label = _(u"Input fa she tian xian data")
    fields = field.Fields(IFashetx).omit('fashetxId')

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(InputFashetx, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit model recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IFashetxLocator)
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')

class UpdateFashetx(UpdateModel):
    """update model table row data
    """
    grok.name('update_fashetx')
    label = _(u"update fa she tian xian data")
    fields = field.Fields(IFashetx).omit('fashetxId')

    cssbdm = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.cssbdm is None:
            self.cssbdm = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IFashetxLocator)
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.cssbdm)

    def update(self):
        self.request.set('disable_border', True)
        # Let z3c.form do its magic
        super(UpdateFashetx, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IFashetxLocator)

        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')
# end 发射天线 数据库操作
## 接收天线 数据库操作
class DeleteJieshoutx(DeleteModel):
    "delete the specify Jieshoutx recorder"

    grok.name('delete_jieshoutx')
    label = _(u"delete jie shou tian xian data")
    fields = field.Fields(IJieshoutx).omit('jieshoutxId')


    cssbdm = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.cssbdm is None:
            self.cssbdm = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IJieshoutxLocator)
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.cssbdm)

    def update(self):
        self.request.set('disable_border', True)

        #Let z3c.form do its magic
        super(DeleteJieshoutx, self).update()


    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete jieshoutx recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IJieshoutxLocator)
        try:
            funcations.DeleteByCode(self.cssbdm)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/jieshoutx_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/jieshoutx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/jieshoutx_listings')

class InputJieshoutx(InputModel):
    """input db jieshoutx table data
    """

    grok.name('input_jieshoutx')

    label = _(u"Input jie shou tian xian data")
    fields = field.Fields(IJieshoutx).omit('jieshoutxId')

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(InputJieshoutx, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit jieshoutianxian recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IJieshoutxLocator)
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')

class UpdateJieshoutx(UpdateModel):
    """update model table row data
    """
    grok.name('update_jieshoutx')
    label = _(u"update jie shou tian xian data")
    fields = field.Fields(IJieshoutx).omit('jieshoutxId')

    cssbdm = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.cssbdm is None:
            self.cssbdm = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IJieshoutxLocator)
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.cssbdm)

    def update(self):
        self.request.set('disable_border', True)
        # Let z3c.form do its magic
        super(UpdateJieshoutx, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IJieshoutxLocator)

        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')
# end 接收天线 数据库操作
## Dianxingtxzyzk 数据库操作
class DeleteDianxingtxzyzk(DeleteModel):
    "delete the specify Dianxingtxzyzk recorder"

    grok.name('delete_Dianxingtxzyzk')
    label = _(u"delete dian xing tian xian zi ku data")
    fields = field.Fields(IDianxingtxzyzk).omit('dianxingtxzyzkId')


    type_antennas = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.type_antennas is None:
            self.type_antennas = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IDianxingtxzyzkLocator)
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.type_antennas)

    def update(self):
        self.request.set('disable_border', True)

        #Let z3c.form do its magic
        super(DeleteDianxingtxzyzk, self).update()


    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete Dianxingtxzyzk recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IDianxingtxzyzkLocator)
        try:
            funcations.DeleteByCode(self.type_antennas)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/dianxingtxzyzk_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/dianxingtxzyzk_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/dianxingtxzyzk_listings')

class InputDianxingtxzyzk(InputModel):
    """input db Dianxingtxzyzk table data
    """

    grok.name('input_dianxingtxzyzk')

    label = _(u"Input dian xing tian xian zeng yi zi ku data")
    fields = field.Fields(IDianxingtxzyzk).omit('DianxingtxzyzkId')

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(InputDianxingtxzyzk, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit Dianxingtxzyzk recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IDianxingtxzyzkLocator)
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')

class UpdateDianxingtxzyzk(UpdateModel):
    """update model table row data
    """
    grok.name('update_Dianxingtxzyzk')
    label = _(u"update dian xing tianxian zi ku data")
    fields = field.Fields(IDianxingtxzyzk).omit('dianxingtxzyzkId')

    type_antennas = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.type_antennas is None:
            self.type_antennas = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = getUtility(IDianxingtxzyzkLocator)
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.type_antennas)

    def update(self):
        self.request.set('disable_border', True)
        # Let z3c.form do its magic
        super(UpdateDianxingtxzyzk, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update Dianxingtxzyzk recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = getUtility(IDianxingtxzyzkLocator)

        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')
# end Dianxingtxzyzk 数据库操作
