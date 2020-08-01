from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


class Faculty(models.Model):
    validate_color = RegexValidator(regex=r'[0-9A-F]{6}', message="Es sind nur Farben als Hexadezimal-Code erlaubt.")

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=6, validators=[validate_color])
    ask_for_phone = models.BooleanField(default=False)
    ask_for_program = models.BooleanField(default=True)
    deadline = models.DateField()

    def __str__(self):
        return self.name

    def color_as_hex(self):
        return '#' + str(self.color)


class Program(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mentor(models.Model):
    validate_email = RegexValidator(regex=r'(\w+\.)?\w+@st.ovgu.de',
                                    message="Es sind nur Adressen mit der Domain 'st.ovgu.de' erlaubt.")
    validate_phone = RegexValidator(regex=r'01\d{2}\/\d{6,7}',
                                    message="Die Mobilnummer ist nur im Format '0123/456789' erlaubt.")

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[validate_email])
    phone = models.CharField(max_length=20, validators=[validate_phone], blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
    qualification = models.BooleanField(default=True)
    supervision = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # def get_absolute_url(self):
    #     return reverse('mentor-detail', kwargs={'pk': self.pk})
