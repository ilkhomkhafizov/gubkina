from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from django.core.validators import FileExtensionValidator


def year_choices():
    return [(r, r) for r in range(2000, datetime.date.today().year + 5)]


class MainInfoModel(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'Male', 'Мужчина'
        FEMALE = 'Female', 'Женщина'

    class GraduationPlaceChoices(models.TextChoices):
        SCHOOL = "School", "Школа"
        COLLEGE = "College", "Колледж"
        LYCEUM = "Lyceum", "Лицей"

    class MajorChoices(models.TextChoices):
        TECHNIC = 'Technic', 'Техническое направление'
        ECONOMIC = 'Economic', 'Экономическое направление'

    class TechnicMinorChoices(models.TextChoices):
        GI = "GI", "Геофизические методы исследования скважин (ГИ) (специалитет)"
        GC = "GC", "Цифровой геоинжиниринг (ГЦ) (специалитет)"
        RB = "RB", "Бурение нефтяных и газовых скважин (РБ)"
        OS = "OS", "Эксплуатация и обслуживание объектов добычи нефти (РН)"
        DG = "DG", "Эксплуатация и обслуживание объектов добычи газа, газоконденсата и подземных хранилищ (РГ)"
        TS = "TS", "Сооружение и ремонт газонефтепроводов и газонефтехранилищ (ТС)"
        TP = "TP", "Эксплуатация и обслуживание объектов транспорта и хранения нефти, газа и продуктов переработки (ТП)"
        RT = "RT", "Технология бурения нефтяных и газовых скважин на суше и море (РТ) (специалитет)"
        RS = "RS", "Разработка и эксплуатация нефтяных и газовых месторождений (РС) (специалитет)"

    class EconomicMinorChoices(models.TextChoices):
        EE = "EE", "Экономика и проекты устойчивого развития энергетики (ЭЭ)"
        EM = "EM", "Управление бизнесом в энергетике (ЭМ)"

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    birth_place = models.CharField(max_length=200)
    living_place = models.CharField(max_length=200)
    citizenship = models.CharField(max_length=200)
    identity_document_name = models.CharField(max_length=100)
    identity_document_ser = models.CharField(max_length=10)
    identity_document_id = models.CharField(max_length=100)
    identity_document_issued_info = models.CharField(max_length=400)
    home_phone_number = PhoneNumberField(null=True, blank=True)
    own_phone_number = PhoneNumberField()
    email = models.EmailField()
    # graduation fields
    graduation_place = models.CharField(max_length=20,
                                        choices=GraduationPlaceChoices.choices)
    graduation_certificate_ser = models.CharField(max_length=50)
    graduation_year = models.IntegerField(choices=year_choices())
    copy_passport = models.FileField(
        upload_to='files/passports',
        validators=[FileExtensionValidator(
            allowed_extensions=["pdf", "jpg", "jpeg", "png"]
        )])
    copy_graduation_certificate = models.FileField(
        upload_to='files/gr_certificates',
        validators=[FileExtensionValidator(
            allowed_extensions=["pdf", "jpg", "jpeg", "png"]
        )])
    image_three_to_four = models.FileField(
        upload_to='files/three_to_four',
        validators=[FileExtensionValidator(
            allowed_extensions=["pdf", "jpg", "jpeg", "png"]
        )])
    # majoring fields
    major_choice = models.CharField(
        max_length=200,
        choices=MajorChoices.choices,
        default=MajorChoices.TECHNIC
    )
    technic_major_choice_first = models.CharField(
        max_length=200,
        choices=TechnicMinorChoices.choices,
        null=True, blank=True
    )
    technic_major_choice_second = models.CharField(
        max_length=200,
        choices=TechnicMinorChoices.choices,
        null=True,
        blank=True
    )
    technic_major_choice_third = models.CharField(
        max_length=200,
        choices=TechnicMinorChoices.choices,
        null=True,
        blank=True
    )
    economic_major_choice_first = models.CharField(
        max_length=200,
        choices=EconomicMinorChoices.choices,
        null=True, blank=True
    )

    economic_major_choice_second = models.CharField(
        max_length=200,
        choices=EconomicMinorChoices.choices,
        null=True, blank=True
    )
    # confirming
    first_confirm = models.BooleanField()
    second_confirm = models.BooleanField()

# {'first_name': 'Jamshid', 'last_name': 'Jabborov', 'middle_name': '123', 'gender': 'Male', 'birth_date': datetime.date(2023, 6, 14), 'nationality': '123', 'birth_place': '123', 'living_place': '123', 'citizenship': '123', 'identity_document_name': '123', 'identity_document_ser': '123', 'identity_document_id': '123', 'identity_document_issued_info': '123', 'home_phone_number': PhoneNumber(country_code=998, national_number=990315632, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=1, preferred_domestic_carrier_code=None), 'own_phone_number': PhoneNumber(country_code=998, national_number=990314532, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=1, preferred_domestic_carrier_code=None), 'email': 'jamshidjabbarov17@gmail.com', 'graduation_place': 'School', 'graduation_certificate_ser': '123', 'graduation_year': 2000, 'copy_passport': <InMemoryUploadedFile: 2023-06-01 22.27.24.jpg (image/jpeg)>, 'copy_graduation_certificate': <InMemoryUploadedFile: photo_2023-05-31 17.30.29.jpeg (image/jpeg)>, 'image_three_to_four': <InMemoryUploadedFile: photo_2023-05-31 17.30.29.jpeg (image/jpeg)>, 'technic_major_choice_first': 'GC', 'technic_major_choice_second': None, 'technic_major_choice_third': None, 'economic_major_choice_first': None, 'economic_major_choice_second': None, 'first_confirm': False, 'second_confirm': False}
