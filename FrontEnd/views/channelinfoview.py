import requests, json
from django.views.generic.base import TemplateView
from FrontEnd.constants.frontendconstants import *
from FrontEnd.helper.createurl import createurl


class ChannelInfoView(TemplateView):
    template_name = CHANNELINFOHTML

    def get_context_data(self, **kwargs):
        if self.request.method == 'GET':
            id = self.request.GET.get('id', None)
            url = createurl(type=CHANNEL, id=id)
            response = requests.get(url)._content
            response = json.loads(response)
            context = super(ChannelInfoView, self).get_context_data(**kwargs)
            context[CHANNELINFO] = response
            return context