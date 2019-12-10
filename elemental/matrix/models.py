from django.db import models
from django.urls import reverse

"""Model representing an ATT&CK Tactic"""
class Tactic(models.Model):

    # DATABASE FIELDS
    tactic_id = models.CharField(max_length=10)
    tactic_name = models.CharField(max_length=30,primary_key=True)
    tactic_description = models.TextField()
    tactic_url = models.CharField(max_length=200)

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = 'tactic'
        verbose_name_plural = 'tactics'

    # TO STRING METHOD
    def __str__(self):
        return self.tactic_name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('tactic-detail', args=[str(self.tactic_name)])

"""Model representing platforms"""
class Platform(models.Model):

    # DATABASE FIELDS
    platform_name = models.CharField(max_length=30,primary_key=True)

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = 'platform'
        verbose_name_plural = 'platforms'

    # TO STRING METHOD
    def __str__(self):
        return self.platform_name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('platform-detail', args=[str(self.platform_name)])

"""Model representing data sources"""
class DataSource(models.Model):

    # DATABASE FIELDS
    # data_sources = models.Manager()
    data_source = models.CharField(max_length=20,primary_key=True)

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = 'data source'
        verbose_name_plural = 'data sources'

    # TO STRING METHOD
    def __str__(self):
        return self.data_source

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('datasource-detail', args=[str(self.data_source)])

"""Model representing an ATT&CK Technique"""
class Technique(models.Model):

    # DATABASE FIELDS
    technique_id = models.CharField(max_length=10, primary_key=True)
    technique_name = models.CharField(max_length=40)
    technique_description = models.TextField()
    technique_detection = models.TextField()
    technique_url = models.CharField(max_length=200)
    technique_abbreviation = models.CharField(max_length=4, blank=True, null=True)
    created = models.DateField(blank=True,null=True)
    modified = models.DateField(blank=True,null=True)
    atomic_yml = models.FileField(upload_to='atomics/',blank=True, null=True)
    atomic_md = models.FileField(upload_to='atomics/',blank=True, null=True)
    platform = models.ManyToManyField(Platform)
    data_source = models.ManyToManyField(DataSource)
    tactic_name = models.ManyToManyField(Tactic)

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = 'technique'
        verbose_name_plural = 'techniques'

    # TO STRING METHOD
    def __str__(self):
        return self.technique_name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('technique-detail', args=[str(self.technique_id)])

"""Model representing Technique Notes"""
class Note(models.Model):

    # DATABASE FIELDS
    technique = models.ForeignKey(
        Technique,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    note = models.TextField()
    date = models.DateField(blank=True,null=True)

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = 'note'
        verbose_name_plural = 'notes'

    # TO STRING METHOD
    def __str__(self):
        return self.note

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('note-detail', args=[str(self.id)])

"""Model representing Sigma Rules"""
class SigmaRule(models.Model):

    # DATABASE FIELDS
    technique = models.ManyToManyField(Technique)
    rule_file = models.FileField(upload_to='sigma_rules/')
    rule_name = models.CharField(max_length=50,primary_key=True)
    date = models.DateField(blank=True,null=True)
    detection_created = models.BooleanField(blank=True,null=True)

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = 'sigma rule'
        verbose_name_plural = 'sigma rules'

    # TO STRING METHOD
    def __str__(self):
        return self.rule_name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('sigmarules-detail', args=[str(self.rule_name)])


def display_text_file(self):
    with open(self.text.path) as fp:
        return fp.read().replace('\n', '<br>')

"""Model representing log sources"""
class LogSource(models.Model):

    #DATABASE FIELDS
    log_name = models.CharField(max_length=30,primary_key=True)
    platform = models.ManyToManyField(Platform)
    data_source = models.ManyToManyField(DataSource)

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = 'log source'
        verbose_name_plural = 'log sources'

    # TO STRING METHOD
    def __str__(self):
        return self.log_name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('logsource-detail', args=[str(self.id)])


