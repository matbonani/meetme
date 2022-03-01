# Generated by Django 3.2 on 2022-02-28 23:40

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Educacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('atualizacao', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=False, verbose_name='Ativo')),
                ('ensino', models.CharField(max_length=30, verbose_name='Estudou oque')),
                ('instituicao', models.CharField(max_length=30, verbose_name='Nome da Instituição')),
                ('inicio', models.CharField(max_length=12, verbose_name='mes/ano de inicio')),
                ('fim', models.CharField(max_length=12, verbose_name='mes/ano do termino')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Educação',
                'verbose_name_plural': 'Educações',
            },
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('atualizacao', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=False, verbose_name='Ativo')),
                ('cargo', models.CharField(max_length=30, verbose_name='Cargo')),
                ('empresa', models.CharField(max_length=30, verbose_name='Nome da empresa')),
                ('inicio', models.CharField(max_length=12, verbose_name='mes/ano de inicio')),
                ('fim', models.CharField(max_length=12, verbose_name='mes/ano do termino')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencias',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('atualizacao', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=False, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=20, verbose_name='Primeiro nome')),
                ('sobrenome', models.CharField(max_length=20, verbose_name='Ultimo nome')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('perfil', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem de perfil')),
                ('experiencia', models.IntegerField(verbose_name='Anos de experiencia')),
                ('pais', models.CharField(max_length=20, verbose_name='Pais')),
                ('cidade', models.CharField(max_length=20, verbose_name='Cidade/bairro')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone1', models.CharField(max_length=20, verbose_name='Telefone 1')),
                ('telefone2', models.CharField(max_length=20, verbose_name='Telefone 2')),
                ('freelance', models.CharField(choices=[('Disponivel', 'disp'), ('Indisponivel no momento', 'indisp')], max_length=30, verbose_name='Disponibilidade')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='instagram')),
                ('linkedin', models.CharField(default='#', max_length=100, verbose_name='instagram')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('atualizacao', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=False, verbose_name='Ativo')),
                ('portifolio', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem do portifolio')),
            ],
            options={
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('atualizacao', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=False, verbose_name='Ativo')),
                ('servico', models.CharField(max_length=20, verbose_name='Serviço')),
                ('descricao', models.CharField(max_length=75, verbose_name='Descrição do serviço')),
                ('icone', models.CharField(choices=[('icon-grid', 'grid 2x2'), ('icon-layers', 'folhas'), ('icon-briefcase', 'maleta'), ('icon-bubbles', 'conversa')], max_length=15, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
    ]
