from django import forms
from django.forms import  (
    ClearableFileInput,
    FileField,
    CharField,
    Textarea,
    TextInput, 
    EmailInput, 
    Select, 
    RadioSelect,
    DateInput,
    TimeInput,
    FileInput
)
from .models import MainInfoModel


class FileForm(forms.Form):
    copy_passport = FileField(widget=ClearableFileInput())
    copy_certificate = FileField(widget=ClearableFileInput())
    image_three_to_four = FileField(widget=ClearableFileInput())


class MainInfoForm(forms.ModelForm):

    class Meta:
        model = MainInfoModel
        # exclude = ['major_choice']
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={
                'id': 'name',
                'class': "same_input",
                "placeholder": "Имя",
                }),
            'last_name': TextInput(attrs={
                "id": "surname",
                'class': "same_input",
                "placeholder": "Фамилия",
                }),
            'middle_name': TextInput(attrs={
                "id": "f-name",
                'class': "same_input",
                "placeholder": "Отчество",
                }),
            'gender': Select(attrs={
                "id": "surname",
                'class': "same_input",
                "placeholder": "Фамилия",
                }),
            'birth_date': DateInput(
                attrs={
                    "id": "date",
                    'class': "same_input",
                    'type': 'date',
                }),
            'nationality': TextInput(attrs={
                "id": "nation",
                'class': "same_input",
                "placeholder": "Национальность",
                }),
            'birth_place': TextInput(attrs={
                "id": "place",
                'class': "same_input",
                "placeholder": "Место рождения",
                }),
            'living_place': TextInput(attrs={
                "id": "place",
                'class': "same_input",
                "placeholder": "Место проживания",
                }),
            'citizenship': TextInput(attrs={
                "id": "native",
                'class': "same_input",
                "placeholder": "Гражданство",
                }),
            'identity_document_name': TextInput(attrs={
                "id": "nat_doc",
                'class': "same_input",
                "placeholder": "Документ личности",
                }),
            'identity_document_ser': TextInput(attrs={
                "id": "seria",
                'class': "same_input",
                "placeholder": "Серия",
                "style": "max-width: 80px;"
                }),
            'identity_document_id': TextInput(attrs={
                "id": "num",
                'class': "same_input",
                "placeholder": "Номер паспорта",
                "style": "max-width: 240px;"
                }),
            'identity_document_issued_info': TextInput(attrs={
                "id": "num",
                'class': "same_input",
                }),
            'home_phone_number': TextInput(attrs={
                "id": "phone",
                'class': "same_input",
                "placeholder": "+998",
                "value": "+998"
                }),
            'own_phone_number': TextInput(attrs={
                "id": "tel",
                'class': "same_input",
                "placeholder": "+998",
                "value": "+998"
                }),
            'email': EmailInput(attrs={
                "id": "gmail",
                'class': "same_input",
                'placeholder': 'Эл.почта'
                }),
            'graduation_place': Select(attrs={
                "id": "select_edu",
                }),
            'graduation_certificate_ser': TextInput(attrs={
                "id": "diploma",
                'class': "same_input",
                }),
            'graduation_year': Select(attrs={
                "id": "year_grad",
                'class': "same_input",
                }),
            'copy_passport': ClearableFileInput(attrs={
                "id": "choose_file",
                }),
            'copy_graduation_certificate': ClearableFileInput(attrs={
                "id": "choose_file",
                }),
            'image_three_to_four': ClearableFileInput(attrs={
                "id": "choose_file",
                }),
            'major_choice': RadioSelect(attrs={
                "style": "max-width: 400px;",
                "class": "faculty_type"
            }),
            'technic_major_choice_first': Select(attrs={
                "style": "max-width: 600px; height: 40px",
                }),
            'technic_major_choice_second': Select(attrs={
                "style": "max-width: 600px; height: 40px"
                }),
            'technic_major_choice_third': Select(attrs={
                "style": "max-width: 600px; height: 40px"
                }),
            'economic_major_choice_first': Select(attrs={
                "style": "max-width: 400px; height: 40px"
                }),
            'economic_major_choice_second': Select(attrs={
                "style": "max-width: 400px; height: 40px"
                }),
        }


        # labels = {
        #     "first_name" : "Имя",
        #     "last_name" : "Фамилия",
        #     "middle_name" : "Отчество",
        #     "gender" : "Пол",
        #     'birth_date' : "Дата рождения",
        #     "nationality" : "Национальность",
        #     "birth_place" : "Место рождения",
        #     "living_place" : "Место проживания",
        #     "citizenship" : "Гражданство",
        #     "identity_document_name" : "Документ удостоверяющий личность",
        #     "identity_document_ser" : "Серия",
        #     "identity_document_id" : "№",
        #     "identity_document_issued_info" : "Когда и кем выдан",
        #     "home_phone_number" : "Телефон (дом)",
        #     "own_phone_number" : "Телефон (сот)",
        #     "email" : "Электронная почта",
        #     "graduation_place" : "Оконченное образовательное учреждение",
        #     "graduation_certificate_ser" : "Серия и номер аттестата или диплома",
        #     "graduation_year" : "Год окончания:",
        #     "copy_passport" : "Загрузите копию паспорта:",
        #     "copy_graduation_certificate" : "Загрузите копию аттестата или диплома:",
        #     "image_three_to_four" : "Загрузите фото 3x4:",
        #     "major_choice" : "Выберите одно из двух направлений:",
        #     "technic_major_choice" : "Техническое направление:",
        #     "economic_major_choice" : "Экономическое направление:"
        # }
        
