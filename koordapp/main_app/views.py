from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect



class MasterHomeView(TemplateView):
    template_name = 'master_overview/master_web.html'

class MasterAndoridHomeView(TemplateView):
    template_name = 'master_android/master_tablet.html'

class RemoveTabletView(TemplateView):
    template_name = 'master_android/remove_tablet.html'

class SetNfcScanAndroidView(TemplateView):
    template_name = 'master_android/set_nfc_scan.html'

class ChooseRoomView(TemplateView):
    template_name = 'choose_room/choose_room.html'

class CreateActivityView(TemplateView):
    template_name = 'create_activity/create_activity.html'

class HomeView(TemplateView):
    template_name = 'home/home.html'

class CheckedInView(TemplateView):
    template_name = 'checked_in/checked_in.html'

class CheckedOutView(TemplateView):
    template_name = 'checked_out/checked_out.html'

class ChangeRoomDataView(TemplateView):
    template_name = 'change_roomdata/change_roomdata.html'

class SetNfcSetView(TemplateView):
    template_name = 'set_nfc_set/set_nfc_set.html'

class OgsGroupView(TemplateView):
    template_name = 'ogs_group/ogs_group.html'

class SearchPupilView(TemplateView):
    template_name = 'search_pupil/search_pupil.html'

class SelectRoomView(TemplateView):
    template_name = 'select_room/select_room.html'