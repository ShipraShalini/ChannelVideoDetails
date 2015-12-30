import requests

from django.views.generic.base import TemplateView

from FrontEnd.constants.frontendconstants import *
from FrontEnd.helper.createurl import createurl


class ChannelInfoView(TemplateView):
    template_name = CHANNELINFOHTML

    def get_context_data(self):
        if self.request.method == 'GET':
            id = self.request.GET.get('id', None)
            url = createurl(type=CHANNEL, id=id)
            response = requests.get(url)._content
            context = super(ChannelInfoView, self).get_context_data()
            context[CHANNELINFO] = response
            return context
