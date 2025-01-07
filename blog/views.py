from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render, get_object_or_404  
# un moyen pratique et sécurisé de récupérer des objets de la base de données, 
# en fournissant une gestion intégrée des erreurs lorsque les objets n'existent pas.
from django.forms import formset_factory
from django.core.mail import send_mail
from blog.forms import ContactUsForm
from django.db.models import Q
from itertools import chain
from django.core.paginator import Paginator

from . import forms, models


@login_required
@permission_required('blog.add_photo', raise_exception=True)
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form': form})


@login_required
@permission_required(['blog.add_photo', 'blog.add_blog'])
def blog_and_photo_upload(request):
    blog_form = forms.BlogForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        blog_form = forms.BlogForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.photo = photo
            blog.save()
            blog.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})
            return redirect('home')
    context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
}
    return render(request, 'blog/create_blog_post.html', context=context)



@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(request, 'blog/view_blog.html', {'blog': blog})


@login_required
def view_photo(request, photo_id):
    photo = get_object_or_404(models.Photo, id=photo_id)
    return render(request, 'blog/view_photo.html', {'photo': photo})

# @login_required
# def home(request):
#     photos = models.Photo.objects.all()
#     blogs = models.Blog.objects.all()
#     return render(request, 'blog/home.html', context={'photos': photos, 'blogs': blogs})

def home(request):
    follows = request.user.follows.all()  # Récupération des utilisateurs suivis par l'utilisateur actuel
    # Récupération des blogs auxquels l'utilisateur est abonné ou qui sont marqués comme favoris
    blogs = models.Blog.objects.filter(
        Q(contributors__in=follows) | Q(starred=True)
    )
    # Récupération des photos téléchargées par les utilisateurs suivis, mais qui ne sont pas liées à des blogs déjà récupérés
    photos = models.Photo.objects.filter(
        uploader__in=follows
    ).exclude(
        blog__in=blogs
    )
    # Fusion des blogs et des photos, triés par date de création
    blogs_and_photos = sorted(
        chain(blogs, photos),
        key=lambda instance: instance.date_created,
        reverse=True
    )
    
    paginator = Paginator(blogs_and_photos, 6)

    # Récupération du numéro de page à afficher à partir des paramètres de requête
    page_number = request.GET.get('page')
    
    # Obtention de l'objet de page pour le numéro de page spécifié
    page_obj = paginator.get_page(page_number)
    
    # Contexte à passer au modèle pour le rendu
    context = {'page_obj': page_obj}
    
    # Rendu de la page d'accueil avec le contexte spécifié
    return render(request, 'blog/home.html', context=context)




def photo_feed(request):
    photos = models.Photo.objects.filter(
        uploader__in=request.user.follows.all()
    ).order_by('-date_created')

    paginator = Paginator(photos, 6) 
    page_number = request.GET.get('page')  # Récupérer le numéro de page demandé, par défaut 1
    page_obj = paginator.get_page(page_number)  # Obtenir l'objet Page correspondant à la page demandée

    context = {
        'page_obj': page_obj,  # Inclure l'objet Page dans le contexte
    }

    return render(request, 'blog/photo_feed.html', context=context)



@login_required
@permission_required('blog.change_blog')
def edit_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    edit_form = forms.BlogForm(instance=blog)
    delete_form = forms.DeleteBlogForm()

    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            edit_form = forms.BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        elif 'delete_blog' in request.POST:
            delete_form = forms.DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect('home')

    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'blog/edit_blog.html', context=context)


@login_required
@permission_required('blog.add_photo')
def create_multiple_photos(request):
    PhotoFormSet = formset_factory(forms.PhotoForm, extra=5)
    formset = PhotoFormSet()
    if request.method == 'POST':
        formset = PhotoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.uploader = request.user
                    photo.save()
            return redirect('home')
    return render(request, 'blog/create_multiple_photos.html', {'formset': formset})


@login_required
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'blog/follow_users_form.html', context={'form': form})


def about(request):
    return render(request, 'blog/about.html')

from django.core.mail import send_mail
...

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["Nom"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['shileiwei200@gmail.com'],
            )
            # Rediriger vers une page de remerciement ou afficher un message de succès
            return redirect('confirmation')  # remplacez 'confirmation' par l'URL appropriée
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request, 'blog/contact.html', {'form': form})

def confirmation(request):
    return render(request, 'blog/confirmation.html')