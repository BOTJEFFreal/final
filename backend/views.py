import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .form import DataInputForm
from .API.Main import execute_code

def process_data(request):
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the form data
            file_input = request.FILES['file_input'].read()  # Get file content as bytes
            text_input1 = form.cleaned_data['text_input1']
            text_input2 = form.cleaned_data['text_input2']
            text_input3 = form.cleaned_data['text_input3']
            text_input4 = form.cleaned_data['text_input4']

            # Call the execute_code function with the appropriate arguments
            execute_code(file_input, text_input1, text_input2)

            # Redirect the user to the success page
            return render(request, 'success.html')
    else:
        form = DataInputForm()

    return render(request, 'data_form.html', {'form': form})

def download_output_csv(request):
    # The code for this view remains unchanged
    output_file_path = request.GET.get('output_file_path')
    if output_file_path:
        with open(output_file_path, 'rb') as output_file:
            response = HttpResponse(output_file.read(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="output.csv"'
            return response
    else:
        return render(request, 'error.html', {'error_message': 'Output file path not provided.'})

