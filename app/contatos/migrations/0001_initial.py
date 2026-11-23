from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contato",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=120, verbose_name="Nome")),
                ("email", models.EmailField(max_length=180, verbose_name="E-mail")),
                ("mensagem", models.TextField(verbose_name="Mensagem")),
                (
                    "criado_em",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
            ],
            options={
                "verbose_name": "Contato",
                "verbose_name_plural": "Contatos",
                "ordering": ["-criado_em", "-id"],
            },
        ),
    ]
