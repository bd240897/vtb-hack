# def dispatch(self, request, *args, **kwargs):
#     # if self.request.user.is_superuser:
#     #     messages.error(request, "У админа нет профиля!")
#     #     return HttpResponseRedirect(reverse("main"))
#     return super().dispatch(request, *args, **kwargs)


# form.instance.owner = User.objects.get(id=form.cleaned_data['owner'])
# form.save()