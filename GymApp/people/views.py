from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from GymApp.people.forms import AddMemberForm, SearchForm, UpdateMemberGymForm, UpdateMemberInfoForm
from GymApp.people.models import Member
from GymApp.people.notifications import get_notification_count
from GymApp.profiles.models import Profile

from GymApp.payments.models import Payments




# def members_list(request):
#     form = AddMemberForm()
#     context = {
#         'form': form,
#         'subs_end_today_count': get_notification_count()
#     }
#
#     return redirect(request, 'add_member.html', context)

def delete_member(request, id):
    print(id)
    Member.objects.filter(pk=id).delete()
    return redirect('view_member')

def update_member(request, id):
    user = get_object_or_404(Member, pk=id)

    if request.method == 'POST':
        gym_form = UpdateMemberGymForm(request.POST, instance=user)
        info_form = UpdateMemberInfoForm(request.POST, request.FILES, instance=user)

        if gym_form.is_valid():
            gym_form.save()

         # Add payments if payment is 'paid'
            if user.fee_status == 'paid':
                check = (Payments.objects.filter
                             (payment_date=user.registration_date, user__pk=user.pk).count()
                         )
                if check == 0:
                    payments = Payments(
                        user=user,
                        payment_date=user.registration_date,
                        payment_period=user.subscription_period,
                        payment_amount=user.amount)
                    payments.save()

                if Payments.objects.filter(user=user).exists():
                    messages.info(request, 'No payment records found.')
                else:
                    messages.success(request, 'Record updated successfully!')
                return redirect('people/view_member', id=user.pk)

            if info_form.is_valid():
                info_form.save()

        return render(request, 'people/view_member.html', context={'id': id, 'gym_form': gym_form, 'info_form': info_form})


@login_required
def view_members(request):
    user_profile = Profile.objects.get(user=request.user)
    profile_members = user_profile.members.order_by('first_name').all()


    search_member = SearchForm(request.GET)

    if search_member.is_valid():
        profile_members = profile_members.filter(
                    first_name__icontains=search_member.cleaned_data['first_name']
                ).order_by('first_name')

    # Paginate the members
    paginator = Paginator(profile_members, 10)
    page_number = request.GET.get('page')
    profile_members = paginator.get_page(page_number)

    context = {
        'profile_members': profile_members,
        'search_member': search_member,
        'subs_end_today_count': get_notification_count(),
    }
    return render(request, 'people/view_member.html', context)

@login_required
def add_member(request):
    user_profile = Profile.objects.get(user=request.user)
    form = AddMemberForm(request.POST or None, request.FILES or None)


    if form.is_valid():
        member = form.save(commit=False)
        if request.POST.get('fee_status') == 'pending':
            member.notification = 1
            # Link the member to the user's profile
            form.save()
            user_profile.members.add(member)
            user_profile.save()

            # Add payments if payment is 'paid'
            if member.fee_status == 'paid':
                # Assuming you have a Payments model defined
                payment = Payments(
                    user=member,
                    payment_date=member.registration_date,
                    payment_period=member.subscription_period,
                    payment_amount=member.amount
                )
                payment.save()

            context = {
                'add_success': 'Successfully Added Member',
                'form': form,
                'subs_end_today_count': get_notification_count(),
            }
            return render(request, 'people/add_member.html', context)
    context = {
        'form': form,
        'subs_end_today_count': get_notification_count(),
    }
    return render(request, 'people/add_member.html', context)
