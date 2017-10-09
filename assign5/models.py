from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Submission(models.Model):
    eid = models.CharField(max_length=10, blank=False)
    document = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    assignment_num = models.IntegerField(default = 0)
    password = models.CharField(max_length=10, default='')

class SubResults(models.Model):
    password =  models.CharField(max_length=10, default='')
    processed_at = models.DateTimeField(auto_now_add=True)
    assignment_num = models.IntegerField(default = 0)
    pomlocation = models.CharField(max_length=500, blank=False)
    eid = models.CharField(max_length=10, blank=False)
    mvnstarted = models.BooleanField(default=False)
    mvnended = models.BooleanField(default=False)
    hadoopstarted = models.BooleanField(default=False)
    hadoopended = models.BooleanField(default=False)
    foundoutput = models.BooleanField(default=False)
    numberoflines = models.IntegerField(default=-999)
    numberofkeymatches = models.IntegerField(default=-999)
    events_sorted = models.BooleanField(default=False)
    features_sorted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    errors = models.CharField(max_length=500, default='')
    def convert_to_string(self):
        output = "<div id='output'>"
        output+= '<li> Autograder started at '+ str(self.processed_at) + ' </li>\n'
        #output+= '<li> EID: '+str(self.eid) + ' </li>\n'
        output+= '<li> mvn clean package started?: ' +str(self.mvnstarted)+'</li>\n'
        output+= '<li> mvn clean package ended?: ' +str(self.mvnended)+'</li>\n'
        output+= '<li> hadoop job started?: ' +str(self.hadoopstarted)+'</li>\n'
        output+= '<li> hadoop job ended?: ' +str(self.hadoopended)+'</li>\n'
        output+= '<li> found output file?: '+str(self.foundoutput)+ '</li>\n'
        output+= '<li> Number of lines in output is '+str(self.numberoflines)+' of xx</li>\n'
        output+= '<li> Number of matching keys in output is '+str(self.numberofkeymatches)+' of xx</li>\n'
        output+= '<li> Events sorted? : '+str(self.events_sorted)+'</li>\n'
        output+= '<li> Features sorted? : '+str(self.features_sorted)+'</li>\n'
        output+= '<li> Autograder is finished? '+str(self.completed)+'</li>\n'
        output+= '<li> ERRORS: '+str(self.errors)+'</li>\n'
        output+= '</div>'
        return output
 




    
