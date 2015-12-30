import requests

from django.views.generic.base import TemplateView

from FrontEnd.constants.frontendconstants import *
from FrontEnd.helper.createurl import createurl


class VideoInfoView(TemplateView):
    template_name = VIDEOINFOHTML

    def get_context_data(self):
        if self.request.method == 'GET':
            id = self.request.GET.get('id', None)
            url = createurl(type=VIDEO, id=id)
            response = requests.get(url)
            print "Response:", response
            context = super(VideoInfoView, self).get_context_data()
            context[VIDEOINFO] = response
            return context


