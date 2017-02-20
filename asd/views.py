import hashlib

from django.views.generic import TemplateView, ListView, FormView, DeleteView, RedirectView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout

from .models import Filename, UploadedFile
from .forms import FileForm


class LoginView(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('storage'))
        return super().dispatch(request, *args, **kwargs)


class LogoutView(RedirectView):
    def get_redirect_url(self):
        logout(self.request)
        return reverse('login')


class StorageView(ListView):
    template_name = 'storage.html'
    context_object_name = 'filenames'

    def get_queryset(self):
        return Filename.objects.filter(owner=self.request.user).select_related('uploaded_file')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_space_left'] = settings.MAX_FILE_NUMBER - len(context['filenames']) > 0
        if not context['is_space_left']:
            messages.warning(self.request, 'You reached the limits. Delete something to upload a new file')
        return context


class FileUploadView(FormView):
    template_name = 'upload.html'
    success_url = reverse_lazy('storage')
    form_class = FileForm
    fields = ['file']

    def dispatch(self, request, *args, **kwargs):
        if Filename.objects.filter(owner=self.request.user).count() >= settings.MAX_FILE_NUMBER:
            messages.error(request, 'Sorry, only {} files allowed for your storage'.format(settings.MAX_FILE_NUMBER))
            return HttpResponseRedirect(reverse('storage'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        file = form.cleaned_data['file']
        checksum = hashlib.md5(file.read()).hexdigest()
        uploaded_name = file.name
        file.name = '{}.{}'.format(checksum, file.name.split('.')[-1])
        uploaded_name = uploaded_name[:255]

        uploaded_file, uploaded = UploadedFile.objects.get_or_create(
            checksum=checksum, defaults={'file': file}
        )
        filename, created = Filename.objects.get_or_create(
            uploaded_file=uploaded_file, name=uploaded_name, owner=self.request.user
        )

        if not uploaded:
            existing_filenames = Filename.objects.filter(
                uploaded_file=uploaded_file
            ).exclude(owner=self.request.user).values_list('name', 'owner__username')
            if existing_filenames:
                messages.info(
                    self.request, 'Someone already uploaded that file:\n' +
                    '\n'.join('{} (by {})'.format(*filename_data) for filename_data in existing_filenames)
                )
            if not created:
                messages.info(self.request, 'Since you already had this file, nothing has changed')
        messages.success(self.request, 'File added to your storage!')
        return super().form_valid(form)


class DeleteFilenameView(DeleteView):
    success_url = reverse_lazy('storage')

    def get_queryset(self):
        return Filename.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        # Skip confirmation page
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'File deleted!')
        return response
