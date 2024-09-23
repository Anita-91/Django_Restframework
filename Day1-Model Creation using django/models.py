from django.db import models

class Manager(models.Model):
    """
    To store info about Manager
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    To store info about Project
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    managers = models.ManyToManyField(Manager, related_name='projects')  # Many-to-many relationship
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='not_started')

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    To store info about Task
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=[
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ])

    def __str__(self):
        return self.title

