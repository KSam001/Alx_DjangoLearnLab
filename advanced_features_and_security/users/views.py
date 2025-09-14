from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse

@login_required
def home(request):
    return HttpResponse("<h1>Welcome to the homepage!</h1><p>You are logged in.</p>")

@permission_required('users.can_view', raise_exception=True)
def view_content(request):
    return HttpResponse("<h1>View Content Page</h1><p>You have permission to view content.</p>")

@permission_required('users.can_create', raise_exception=True)
def create_content(request):
    return HttpResponse("<h1>Create Content Page</h1><p>You have permission to create content.</p>")

@permission_required('users.can_edit', raise_exception=True)
def edit_content(request):
    return HttpResponse("<h1>Edit Content Page</h1><p>You have permission to edit content.</p>")

@permission_required('users.can_delete', raise_exception=True)
def delete_content(request):
    return HttpResponse("<h1>Delete Content Page</h1><p>You have permission to delete content.</p>")
