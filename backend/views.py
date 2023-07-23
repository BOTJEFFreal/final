import os
from django.shortcuts import render
from django.http import HttpResponse
from .form import DataInputForm
from .API.Main import execute_code
import csv

def process_data(request):
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the form data
            file_input = request.FILES['file_input']
            text_input1 = form.cleaned_data['text_input1']
            text_input2 = form.cleaned_data['text_input2']
            text_input3 = form.cleaned_data['text_input3']
            text_input4 = form.cleaned_data['text_input4']

            # Call the execute_code function with the appropriate arguments
            csv_content = execute_code(file_input, text_input1, text_input2)

            # Prepare the CSV response
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="output.csv"'

            # Write the CSV content to the response
            writer = csv.writer(response)
            for row in csv_content:
                writer.writerow(row)

            return response

    else:
        form = DataInputForm()

    return render(request, 'data_form.html', {'form': form})
