from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from matrix.models import Tactic, Technique, Platform, DataSource, Note, SigmaRule, LogSource
from django.conf import settings
from django.views import generic
import os
from django.urls import reverse
import datetime
from django.views.generic import TemplateView
from django import template
from markdownx.utils import markdownify
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from matrix.forms import noteForm


def index(request):
    """View function for home page of site."""

    ## Generate the number of tactics and names
    num_tactics = Tactic.objects.all().count()
    tactics = Tactic.objects.all().order_by('tactic_id')
    tactic_names = list()
    tactic_shortnames = list()
    techniques_by_tactic = {}
    for tactic in tactics:
        tactic_names.append(tactic.tactic_name)
        tactic_techniques = Technique.objects.filter(tactic_name=tactic).order_by('technique_name')
        techniques_by_tactic[tactic.tactic_name] = tactic_techniques

    ## Define the context    
    context = {
        'techniques_by_tactic': techniques_by_tactic,
    }

    ## Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)
    #return render(request, 'test.html', context)

#class SigmaRuleView(generic.ListView):
#    model = SigmaRule

def alltactics(request):
    total_tactics = Tactic.objects.all()
    context = {
        'total_tactics': total_tactics,
    }

    ## Render the HTML template index.html with the data in the context variable
    return render(request, 'matrix/tactic_list.html', context=context)

def allTechPerTactic(request):
    techfortactics = Technique.objects.filter(tactic_name='Impact')
    tactfortactics = Tactic.objects.filter(tactic_name='Impact')

    ## Define the context
    context = {
        'techfortactics': techfortactics,
        'tactfortactics': tactfortactics,
    }
    ## Render the HTML template index.html with the data in the context variable
    return render(request, 'matrix/tech_for_tactic.html', context)


class TacticDetailView(generic.DetailView):
    model = Tactic
    #template_name = 'matrix/TacticTemplate.html'

class TechniqueDetailView(generic.DetailView):
    model = Technique

def alltechniques(request):
    total_techniques = Technique.objects.all()
    context = {
        'total_techniques': total_techniques,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'matrix/technique_list.html', context)

class TacticListView(TemplateView):
    template_name = "TacticTemplate"

class TechniqueListView(generic.ListView):
    model = Technique

def atomics(request, pk):
    atomic = Technique.objects.get(pk=pk)
    atomic_file = open(settings.MEDIA_ROOT + '/atomics/' + atomic.technique_id + ".md", 'r')
    atom = atomic_file.read()
    atomic_file.close()
    context = {
    'atomic' : atomic,
    'atom' : markdownify(atom),
    }

    return render(request, 'matrix/atomic.html', context)

def addnote(request, pk):
    if request.method == "POST":
        form = noteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=True)
            note.save()
            return redirect('individualTechnique', pk=pk)

    else:
        technique = Technique.objects.get(pk=pk)
        # Get all notes for a given technique
        notes = Note.objects.filter(technique_id=pk)
        form = noteForm()
        form.fields['technique'].initial = pk 
        form.fields['date'].initial = datetime.datetime.now()

    #return render(request, 'matrix/addnote.html', context)
    #return HttpResponseRedirect(reverse('addnote', args=(technique.technique_id,)))
    return render(request, 'matrix/noteForm.html', {'form': form})


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes')


def noteCreator(request, pk):
    technique = Technique.objects.get(pk=pk)
    # Get all notes for a given technique
    notes = Note.objects.filter(technique_id=technique.technique_id)
    
    addnote = "This is a new note"

    #Define the context
    context = {
        'addnote': addnote,
        'notes': notes,
        'note': addnote,
    }

    return render(request, 'matrix/noteForm.html', context)
    #return render(request, /)


class NoteCreate(CreateView):
    model = Note
    fields = '__all__'
    initial = {'date': datetime.datetime.now(), 'note': 'notes'}

class NoteUpdate(UpdateView):
    model = Note
    fields = ['note', 'date', 'technique']

class NoteDetailView(generic.DetailView):
    model = Note
    tech = Technique

class NoteListView(generic.ListView):
    model = Note

def notesPerTech(request, pk):
    # Get all notes for a given technique
    notes = Note.objects.filter(technique_id=pk)
    all_notes = list()
    for note in notes:
        all_notes.append(note.note)

    #Define the context
    context = {
        'tech_notes': all_notes,
        'tech_id': technique,
    }

    return render(request, 'matrix/notes_for_tech.html', context)

def updateNotesPerTech(request, pk):
    #technique = get_object_or_404(Technique, pk=pk)
    note = Note.objects.get(pk=pk)
    technique = Technique.objects.get(technique_name=note.technique)
    # Get all notes for a given technique
    notes = Note.objects.filter(technique_id=pk)
    all_notes = list()
    for note in notes:
        all_notes.append(note.note)

    #Define the context
    context = {
        'tech_notes': all_notes,
        'tech_id': technique,
    }

    return render(request, 'note_update', context)

def addTechnique(request):
    platforms = Platform.objects.all()
    dataSources = DataSource.objects.all()
    tactics = Tactic.objects.all()
    context = {
        'platforms': platforms,
        'dataSources': dataSources,
        'tactics': tactics,
    }
    return render(request, 'matrix/addTechnique.html' ,context)

def addSigma(request):
    context = {
        'hi': "hi",
    }
    return render(request, 'matrix/addSigma.html' ,context)


def individualTechnique(request, pk):
    technique = Technique.objects.get(pk=pk)
    platforms = Platform.objects.filter(technique=technique.technique_id)
    data_sources = DataSource.objects.filter(technique=technique.technique_id)
    tactics = Tactic.objects.filter(technique=technique.technique_id)
    ## Get all notes for a given technique
    notes = Note.objects.filter(technique_id=technique.technique_id)
    all_notes = notes[::-1]

    ## SIGMA RULES
    sigma_rules = list()
    rules = SigmaRule.objects.filter(technique=technique.technique_id)
    rule_names = list()
    yaml_rule_list = list()
    for rule in rules:
        sigma_rules.append("/sigma_rules/" + rule.rule_name + ".yml")
        sigma = open(settings.MEDIA_ROOT + '/' + rule.rule_file.name ,'r')
        yaml_rule_list.append([rule.rule_name, sigma.read()])
        sigma.close()

    ## ATOMICS
    atomic = technique
    null_atom = ""
    try:
        atomic_file = open(settings.MEDIA_ROOT + '/atomics/' + atomic.technique_id + ".md", 'r')
        atomic_yaml = open(settings.MEDIA_ROOT + '/atomics/' + atomic.technique_id + ".yaml", 'r')
        atom = atomic_file.read()
        atom_yaml = atomic_yaml.read()
        atomic_file.close()
        atomic_yaml.close()
    except:
        null_atom = "There are currently no Atomic Red Team tests available for this technique."
        atom_yaml = ""
        atom = ""

    
    ## Define the Context
    context = {
        'technique': technique,
        'platforms': platforms,
        'data_sources': data_sources,
        'tactics': tactics,
        'technique_description': markdownify(technique.technique_description),
        'technique_url': technique.technique_url,
        'technique_id': technique.technique_id,
        'technique_detection': markdownify(technique.technique_detection),
        'technique_name': technique.technique_name,
        'atom': markdownify(atom),
        'atom_yaml': atom_yaml,
        'null_atom': null_atom,
        'tech_notes': all_notes,
        'yaml_rules': yaml_rule_list,
    }
    return render(request, 'matrix/technique.html', context = context)

