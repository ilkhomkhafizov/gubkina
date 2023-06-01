from django.shortcuts import render
from .forms import MainInfoForm
from django.contrib import messages
from django.conf import settings
import os 
from PIL import Image
from PyPDF2 import PdfMerger
import time 
import jinja2
from pyhtml2pdf import converter
base_certificate_path = os.path.join("files", "gr_certificates")
base_passport_path = os.path.join("files", "passports")
base_three_to_four_path = os.path.join("files", "three_to_four")
# Create your views here


def convert_pdfs(instance):
    certificate_path = str(instance.copy_graduation_certificate)
    passport_path = str(instance.copy_passport)
    three_to_four_path = str(instance.image_three_to_four)
    print(certificate_path, " certificate_path")
    print(passport_path, " passport_path")
    print(three_to_four_path, " three_to_four_path")

    merger = PdfMerger()

    if certificate_path.endswith(".pdf"):
        final_certificate_path = certificate_path
    else:
        image = Image.open(certificate_path)
        converted_file = image.convert('RGB')
        now = time.time()
        final_certificate_path = os.path.join(settings.BASE_DIR, "files",
                                              "samples", f"{now}.pdf")
        converted_file.save(final_certificate_path)
    merger.append(final_certificate_path)

    if passport_path.endswith(".pdf"):
        final_passport_path = passport_path
    else:
        image = Image.open(passport_path)
        converted_file = image.convert('RGB')
        now = time.time()
        final_passport_path = os.path.join(settings.BASE_DIR, "files",
                                           "samples", f"{now}.pdf")
        converted_file.save(final_passport_path)
    merger.append(final_passport_path)

    if three_to_four_path.endswith(".pdf"):
        final_three_to_four_path = three_to_four_path
    else:
        image = Image.open(three_to_four_path)
        converted_file = image.convert('RGB')
        now = time.time()
        final_three_to_four_path = os.path.join(settings.BASE_DIR, "files",
                                                "samples", f"{now}.pdf")
        converted_file.save(final_three_to_four_path)
    merger.append(final_three_to_four_path)
    print(final_certificate_path,)
    print(final_passport_path,)
    print(final_three_to_four_path,)
    merged_file_path = "files/merged_pages.pdf"
    merger.write(merged_file_path)

    return merged_file_path


def create_pdf_form(context, merged_file_path):
    template_loader = jinja2.FileSystemLoader("./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("files/template.html")
    output_text = template.render(context)
    with open('files/new.html', 'w') as f:
        f.write(output_text)

    now = time.time()
    rendered_file_path = f'files/{now}.pdf'
    old_html_file_path = os.path.abspath('files/new.html')
    converter.convert(f'file:///{old_html_file_path}', rendered_file_path)
    # merging finally

    merger = PdfMerger()
    merger.append(rendered_file_path)
    merger.append(merged_file_path)
    now = time.time()
    final_merged_file_path = f"files/merged_files/{now}.pdf"
    merger.write(final_merged_file_path)

    # removing
    old_rendered_file_path = os.path.abspath(rendered_file_path)
    os.remove(old_rendered_file_path)
    old_merged_file_path = os.path.abspath(merged_file_path)
    os.remove(old_merged_file_path)
    os.remove(old_html_file_path)

    return final_merged_file_path


def home_form_view(request):
    context = {}
    if request.method == "GET":
        form = MainInfoForm()
        context['form'] = form
    elif request.method == "POST":
        form = MainInfoForm(request.POST, request.FILES)
        if form.is_valid():
            # some pdf action is here
            instance = form.save()
            cleaned_data = form.cleaned_data
            if cleaned_data['home_phone_number']:
                cleaned_data['home_phone_number'] = cleaned_data['home_phone_number'].as_e164
            cleaned_data['own_phone_number'] = cleaned_data['own_phone_number'].as_e164
            initial_merged_file_path = convert_pdfs(instance=instance)
            final_merged_file_path = create_pdf_form(cleaned_data,
                                                     initial_merged_file_path)
            print(final_merged_file_path, " fin")
            messages.success(request, 'Muvaffaqiyatli yaratildi!')
        else:
            errors_dict = form.errors.as_data()
            first_error_message = errors_dict[list(errors_dict.keys())[0]][0].message
            messages.warning(request, first_error_message)
        context['form'] = form

    return render(request, 'main/main.html', context=context)
