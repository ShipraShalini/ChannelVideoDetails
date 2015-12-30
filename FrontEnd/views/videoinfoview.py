import requests, json

from django.views.generic.base import TemplateView

from FrontEnd.constants.frontendconstants import *
from FrontEnd.helper.createurl import createurl


class VideoInfoView(TemplateView):
    template_name = VIDEOINFOHTML

    def get_context_data(self,**kwargs):
        if self.request.method == 'GET':
            id = self.request.GET.get('id', None)
            url = createurl(type=VIDEO, id=id)
            response = json.loads(requests.get(url)._content)
            context = super(VideoInfoView, self).get_context_data(**kwargs)
            context[VIDEOINFO] = response
            return context


