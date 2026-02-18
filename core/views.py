from django.shortcuts import render,redirect,get_object_or_404
from .models import Donor,Recipient,Hospital
from .forms import DonorForm,RecipientForm,HospitalForm


#Donor


def donor_list(request):
    donors=Donor.objects.all()
    return render (request,'donor_list.html',{'donors':donors})

def donor_create(request):
    if request.method=='POST':
        form=DonorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form=DonorForm()
    return render(request,'donor_form.html',{'form':form})

def donor_update(request,pk):
    donor=get_object_or_404(Donor,pk=pk)
    if request.method=='POST':
        form=DonorForm(request.POST,request.FILES,instance=donor)
        if form.is_valid():
            form.save()
            return redirect ('donor_list')
    else:
        form=DonorForm(instance=donor)
    return render(request,'donor_form.html',{'form':form})

def donor_delete(request,pk):
    donor=get_object_or_404(Donor,pk=pk)
    if request.method=='POST':
        donor.delete()
        return redirect('donor_list')
    return render (request,'donor_confirm_delete.html',{'donor':donor})




# Recipient 

def recipient_list(request):
    recipients=Recipient.objects.all()
    return render (request,'recipient_list.html',{'recipients':recipients})


def recipient_create(request):
    if request.method=='POST':
        form=RecipientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipient_list')
    else:
        form=RecipientForm()
    return render(request,'recipient_form.html',{'form':form})


def recipient_update(request,pk):
    recipient=get_object_or_404(Recipient,pk=pk)
    if request.method=='POST':
        form=RecipientForm(request.POST,request.FILES,instance=recipient)
        if form.is_valid():
            form.save()
            return redirect('recipient_list')
    else:
        form=RecipientForm(instance=recipient)
    return render(request,'recipient_form.html',{'form':form})



def recipient_delete(request,pk):
    recipient=get_object_or_404(Recipient,pk=pk)
    if request.method=='POST':
        recipient.delete()
        return redirect('recipient_list')
    return render(request,'recipient_confirm_delete.html',{'recipient':recipient})


#hospital

def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital_list.html', {'hospitals': hospitals})


# def hospital_create(request):
#     if request.method == 'POST':
#         form = HospitalForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('hospital_list')
#     else:
#         form = HospitalForm()
#     return render(request, 'hospital_form.html', {'form': form})



def hospital_update(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'hospital_form.html', {'form': form})


def hospital_delete(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital_list')
    return render(request, 'hospital_confirm_delete.html', {'hospital': hospital})




# -----------------------------
# Matching System
# -----------------------------
def find_matches(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk)

    matches = Donor.objects.filter(
        blood_group=recipient.blood_group,
        organ_type=recipient.required_organ,
        availability=True
    )

    if matches.exists():
        recipient.status = "Matched"
        recipient.save()

    return render(request, 'matching_results.html', {
        'recipient': recipient,
        'matches': matches
    })



def landing(request):
    return render(request, 'landing.html')

















